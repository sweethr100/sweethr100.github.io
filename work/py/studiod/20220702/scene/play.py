import random
from scene.default import *
import pygame
import config
import sys

background_x=0
background_x2=config.map_width
background_speed =2

user_x = 30
user_y = 0
user_speed = 3

bullet_list = []
fireball_list = []
fireball_get = 13

class Play(Default):
    def __init__(self):
        self.scene_name = config.scene_play


    def print(self,dc):
        dc.fill((255,255,255))
        global background_x, background_x2
        img = pygame.image.load('resource/background.png')
        img = pygame.transform.scale(img,(config.map_width,config.map_height))
        dc.blit(img,(background_x,0))
        background_x-=background_speed
        if background_x <= -config.map_width:
            background_x = config.map_width
        dc.blit(img,(background_x2,0))
        background_x2-=background_speed
        if background_x2 <= -config.map_width:
            background_x2 = config.map_width

        img = pygame.image.load('resource/plane.png')
        dc.blit(img,(user_x,user_y))

        for i in range(26):
            if i < fireball_get:
                pygame.draw.rect(dc,(255,228,0),(config.map_width-(30-i)*10-30,config.map_height-70,10,30))
            else:
                pygame.draw.rect(dc,(255,0,0),(config.map_width-(30-i)*10-30,config.map_height-70,10,30))

        img = pygame.image.load('resource/bullet.png')
        i=0
        while i<len(bullet_list):
            dc.blit(img,bullet_list[i])
            bullet_list[i][0]+=10
            if bullet_list[i][0] > config.map_width:
                del bullet_list[i]
                continue
            i+=1
        img = pygame.image.load('resource/fireball.png')
        i=0
        while i<len(fireball_list):
            dc.blit(img,fireball_list[i])
            fireball_list[i][0]+=20
            if fireball_list[i][0] > config.map_width:
                del fireball_list[i]
                continue
            i+=1


    def trigger(self,events):
        global user_x,user_y, user_speed
        x,y = pygame.mouse.get_pos()
        
        if user_y > y:
            user_y -= user_speed
        if user_y < y and user_y < config.map_height-165:
            user_y += user_speed
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if event.button == 1:
                    bullet_list.append([user_x+75,user_y+20])
                if event.button == 2:
                    global fireball_get
                    fireball_get-=1
                if event.button == 3:
                    fireball_list.append([user_x+75,user_y+20])
                    


    def next(self):
        return self.scene_name