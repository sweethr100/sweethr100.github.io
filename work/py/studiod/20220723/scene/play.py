from scene.default import *
import pygame
import config
import random

background_x=0
background_x2=config.map_width
background_speed=2

user_x = 30
user_y = 0
user_speed=3

bullet_list = []
fireball_list = []
fireball_get = 0

bat_list = []
bat_last_time=0

score = 0
life=3

class Play(Default):
    def __init__(self,dc,events):
        self.scene_name = config.scene_play
        self.dc=dc
        self.events=events

    def print(self):
        dc=self.dc
        events = self.events
        dc.fill((255,255,255))
        global background_x, background_x2
        global life
        img = pygame.image.load("resource/background.png")
        img = pygame.transform.scale(img,(config.map_width,config.map_height))
        dc.blit(img,(background_x,0))
        background_x -=background_speed
        if background_x <= -config.map_width:
            background_x = config.map_width
        dc.blit(img,(background_x2,0))
        background_x2 -=background_speed
        if background_x2 <= -config.map_width:
            background_x2 = config.map_width

        for i in range(30):
            if i < fireball_get:
                pygame.draw.rect(dc,(255,228,0),(config.map_width-(30-i)*10-30,config.map_height-70,10,30))
            else:
                pygame.draw.rect(dc,(255,0,0),(config.map_width-(30-i)*10-30,config.map_height-70,10,30))
                
        img = pygame.image.load("resource/bat.png")
        i=0
        while i<len(bat_list):
            dc.blit(img,bat_list[i])
            
            bat_list[i][0]-=5
            bat_list[i][1]+=random.randint(-5, 5)
            if bat_list[i][1] < 0:
                bat_list[i][1]=0
            elif bat_list[i][1] > config.map_height-155:
                bat_list[i][1]=config.map_height-155

            if bat_list[i][0] < 0:
                del bat_list[i]
                life-=1
                if life <= 0:
                    self.scene_name=config.scene_end
                continue
            i+=1

        img = pygame.image.load("resource/heart.png")
        img = pygame.transform.scale(img,(50,50))
        for i in range(1,life+1):
            dc.blit(img,[config.map_width-i*50,0])

        img = pygame.image.load("resource/bullet.png")
        i=0
        while i<len(bullet_list):
            dc.blit(img,bullet_list[i])
            bullet_list[i][0]+=10
            if bullet_list[i][0] > config.map_width:
                del bullet_list[i]
                continue
            i+=1

        img = pygame.image.load("resource/fireball.png")
        i=0
        while i<len(fireball_list):
            dc.blit(img,fireball_list[i])
            fireball_list[i][0]+=20
            if fireball_list[i][0] > config.map_width:
                del fireball_list[i]
                continue
            i+=1

        img = pygame.image.load("resource/plane.png")
        dc.blit(img,(user_x,user_y))

        font = pygame.font.Font(None, 40)
        text = font.render("score : "+str(score), True, (255,255,255))
        dc.blit(text, (20, config.map_height-80))

    def trigger(self):
        dc=self.dc
        events = self.events
        global user_x,user_y,user_speed
        global fireball_get
        global bat_last_time
        global score
        x,y = pygame.mouse.get_pos()
        if user_y > y:
            user_y -=user_speed
        if user_y < y and user_y < config.map_height-155:
            user_y +=user_speed

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet_list.append([user_x+25,user_y+20])
                if event.button == 2:
                    fireball_get+=1
                if event.button == 3:
                    if fireball_get >= 5:
                        fireball_list.append([user_x+25,user_y+20])
                        fireball_get-=5

        level = 250
        msec = pygame.time.get_ticks()
        if msec > bat_last_time + level:
            bat_last_time=msec
            y = random.randint(0, config.map_height-155)
            bat_list.append([config.map_width,y])

        
        bullet = pygame.image.load("resource/bullet.png")
        bat = pygame.image.load("resource/bat.png")
        fireball = pygame.image.load("resource/fireball.png")
        i=0
        flag=False
        while i < len(bullet_list):
            j=0
            while j < len(bat_list):
                if self.checkCrash(bullet, bullet_list[i], bat, bat_list[j]):
                    score +=1
                    del bat_list[j]
                    fireball_get+=1/(1500/level)
                    if fireball_get > 30:
                        fireball_get=30
                    flag=True
                    break
                j+=1
            if flag:
                del bullet_list[i]
                break
            i+=1

        i=0
        while i < len(fireball_list):
            j=0
            while j < len(bat_list):
                if self.checkCrash(fireball, fireball_list[i], bat, bat_list[j]):
                    score +=1
                    del bat_list[j]
                    continue
                j+=1
            i+=1

    def next(self):
        return self.scene_name

    def checkCrash(self,obj1,pos1,obj2,pos2):
        s1 = pygame.sprite.Sprite()
        s1.rect=obj1.get_rect()
        s1.mask = pygame.mask.from_surface(obj1)
        s1.x=pos1[0]
        s1.y=pos1[1]
        s1.rect.center = (s1.x+s1.rect[2]/2, s1.y+s1.rect[3]/2)

        s2 = pygame.sprite.Sprite()
        s2.rect=obj2.get_rect()
        s2.mask = pygame.mask.from_surface(obj2)
        s2.x=pos2[0]
        s2.y=pos2[1]
        s2.rect.center = (s2.x+s2.rect[2]/2,s2.y+s2.rect[3]/2)

        return pygame.sprite.collide_mask(s1,s2)