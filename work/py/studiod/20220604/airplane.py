# ----Options----
FPS = 24 #1초에 업데이트 되는 수
Stone_delay = 3 #바위가 몇초마다 나오는지 정하는 수
Stone_number = 2 #한번에 나오는 바위는 몇개일지 정하는 수
skil = 1 #스킬 유형
# ---------------






import sys
import os
import random
from tkinter import *
from tkinter import messagebox
import pygame
from threading import Thread
import time

MAP_WIDTH = 480
MAP_HEIGHT = 640

score = 0

userData = {'obj':None,'x': MAP_WIDTH*0.45, 'y':MAP_HEIGHT*0.875,'speed':5*60/FPS} #5
missileData = {'pos':[],'speed': 10*60/FPS} #10
rockData= []

def interval(cnt,t):
	while True:
		for i in range(cnt):
			rockImg = pygame.image.load("resource/rock%02d.png"% random.randint(1, 30))
			r = random.randint(35,120)
			rockImg = pygame.transform.scale(rockImg,(r,r))
			rock = {
				"obj": rockImg,
				"pos": {"x":random.randint(0,MAP_WIDTH)-rockImg.get_width(),"y":0},
				"speed": 3*60/FPS,
				"rot" : 0,
			}
			rockData.append(rock)
		time.sleep(t)


def eventGame(events):
	for event in events:
		if pygame.QUIT == event.type:
			pygame.quit()
			sys.exit(1)
		elif pygame.KEYDOWN == event.type:
			if event.key == pygame.K_SPACE:
				m = {'x':userData['x']+15,'y':userData['y'],'obj': pygame.image.load('resource/missile.png')}
				missileData['pos'].append(m)
				missileSound = pygame.mixer.Sound('resource/missile.wav')
				missileSound.play()

			if event.key == pygame.K_LSHIFT:
				if skil == 1:
					img = pygame.image.load('resource/missile.png')
					for i in range(50):
						m = {'x':i*10-10,'y':userData['y']+15,'obj':img}
						missileData['pos'].append(m)
						time.sleep(0.03)
					missileSound = pygame.mixer.Sound('resource/missile.wav')
					missileSound.play()
					
				

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		userData['x'] -= userData['speed']
	if keys[pygame.K_RIGHT]:
		userData['x'] += userData['speed']
	# if keys[pygame.K_SPACE]:
	# 	m = {'x':userData['x']+15,'y':userData['y'],'obj': pygame.image.load('resource/missile.png')}
	# 	missileData['pos'].append(m)

def printGame(dc):
	global score

	background = pygame.image.load('resource/background.png')
	dc.blit(background,(0,0))

	for rock in rockData:
		rock['rot'] = (rock['rot']+random.randint(1,4)) % 360
		img = pygame.transform.rotate(rock['obj'],rock['rot'])
		dc.blit(img,(rock['pos']['x'],rock['pos']['y']))

	for missile in missileData['pos']:
		dc.blit(missile['obj'],(missile['x'],missile['y']))

	

	i=0
	while i < len(missileData['pos']):
		missile = missileData['pos']
		j = 0
		while j < len(rockData):
			if checkCrash(missile[i], rockData[j]):
				explosion = pygame.image.load('resource/explosion.png')
				explosionSound = pygame.mixer.Sound("resource/explosion%02d.wav"% random.randint(1, 4))
				explosionSound.play()
				dc.blit(explosion,(rockData[j]['pos']['y'],rockData[j]['pos']['y']))
				score+=1
				del rockData[j]
				break
			j+=1
		i+=1

	user = pygame.image.load("resource/fighter.png")
	userData['obj']=user
	dc.blit(user,(userData['x'],userData['y']))

	font = pygame.font.SysFont("resource/NanumGothic.ttf",75,False,False)
	text = font.render("1", False, (0,127,255))
	dc.blit(text,(200,50))

def play():
	i=0
	while i < len(missileData['pos']):
		missileData['pos'][i]['y'] -= missileData['speed']
		if missileData['pos'][i]['y'] < 0:
			del missileData['pos'][i]
			continue
		i+=1

	i = 0
	while i < len(rockData):
		rockData[i]['pos']['y'] += rockData[i]['speed']
		if rockData[i]['pos']['y'] > MAP_HEIGHT:
			del rockData[i]
			gameoverSound = pygame.mixer.Sound("resource/gameover.wav")
			gameoverSound.play()
			time.sleep(1)
			pygame.quit()
			sys.exit(1)
			continue
		i+=1

def checkCrash(a,b):
	s1 = pygame.sprite.Sprite()
	s1.rect=a['obj'].get_rect()
	s1.mask = pygame.mask.from_surface(a['obj'])
	try:
		s1.x=a['x']
		s1.y=a['y']
	except:
		s1.x=a['pos']['x']
		s1.y=a['pos']['y']
	s1.rect.center = (s1.x+s1.rect[2]/2,s1.y+s1.rect[3]/2)



	s2 = pygame.sprite.Sprite()
	s2.rect=b['obj'].get_rect()
	s2.mask = pygame.mask.from_surface(b['obj'])
	try:
		s2.x=b['x']
		s2.y=b['y']
	except:
		s2.x=b['pos']['x']
		s2.y=b['pos']['y']
	s2.rect.center = (s2.x+s2.rect[2]/2,s2.y+s2.rect[3]/2)

	# print(
	# 	pygame.sprite.collide_rect(s1,s2),
	# 	pygame.sprite.collide_circle(s1,s2),
	# 	pygame.sprite.collide_mask(s1,s2),
	# )
	
	return pygame.sprite.collide_mask(s1,s2)

def main():
	pygame.font.init()
	pygame.init()
	pygame.mixer.init()
	pygame.display.set_caption("airplane")
	dc = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
	clock = pygame.time.Clock()
	time = pygame.time.get_ticks()
	Thread(target=interval,args=(Stone_number,Stone_delay)).start() #갯수,초
	pygame.mixer.music.load("resource/music.wav")
	pygame.mixer.music.play()

	while True:
		printGame(dc)
		eventGame(pygame.event.get())
		play()
		clock.tick(FPS)
		# print(clock.get_fps())
		pygame.display.update()
	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	main()