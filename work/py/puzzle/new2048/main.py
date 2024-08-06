import sys
import os
import random
import time
from tkinter import *
from tkinter import messagebox
import pygame
from game2048 import *

MAP_SIZE = 400


def eventGame(game2048,events):
	for event in events:
		if pygame.QUIT == event.type:
			pygame.quit()
			sys.exit(1)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("LEFT")
				game2048.leftPush()
				game2048.merge()
				game2048.leftPush()

			if event.key == pygame.K_RIGHT:
				print("RIGHT")
				game2048.lotate()
				game2048.lotate()

				game2048.leftPush()
				game2048.merge()
				game2048.leftPush()

				game2048.lotate()
				game2048.lotate()
			
			if event.key == pygame.K_UP:
				print("UP")
				game2048.lotate()
				game2048.lotate()
				game2048.lotate()

				game2048.leftPush()
				game2048.merge()
				game2048.leftPush()

				game2048.lotate()

			if event.key == pygame.K_DOWN:
				print("DOWN")
				game2048.lotate()

				game2048.leftPush()
				game2048.merge()
				game2048.leftPush()

				game2048.lotate()
				game2048.lotate()
				game2048.lotate()

def printGame(game2048,dc):
	dc.fill((255, 255, 255))

	# game2048.map = [
	# 	[0,2,4,8],
	# 	[16,32,64,128],
	# 	[256,512,1024,2048],
	# 	[0,2,4,8],
	# ]

	for y in range(game2048.size):
		for x in range(game2048.size):
			# x, y, MAP_SIZE, game2048.size
			size = MAP_SIZE//game2048.size
			val = game2048.map[y][x]
			pygame.draw.rect(dc,blockcolor[val],[size*x,size*y,size,size])
			pygame.draw.rect(dc,(255,255,255),[size*x,size*y,size,size],1)

			if len(str(val)) == 1:
				fontsize=60
				font = pygame.font.SysFont('바탕',fontsize)
				if val > 4:
					text = font.render(str(val), True, (255,255,255))
				else:
					text = font.render(str(val), True, (119,110,101))
				padding = size//3
				if val !=0:
					dc.blit(text,(size*x+padding,size*y+padding))
			elif len(str(val)) == 2:
				fontsize=50
				font = pygame.font.SysFont('바탕',fontsize)
				text = font.render(str(val), True, (255,255,255))
				padding = size//3
				dc.blit(text,(size*x+padding,size*y+padding))
			elif len(str(val)) == 3:
				fontsize=50
				font = pygame.font.SysFont('바탕',fontsize)
				text = font.render(str(val), True, (255,255,255))
				padding = size//3
				dc.blit(text,(size*x+padding-10,size*y+padding))
			else:
				fontsize=40
				font = pygame.font.SysFont('바탕',fontsize)
				text = font.render(str(val), True, (255,255,255))
				padding = size//2 - fontsize//3
				dc.blit(text,(size*x+padding-15,size*y+padding))

			# fontsize=30
			# font = pygame.font.SysFont('바탕',fontsize)
			# text = font.render(str(val), True, (255,0,0))
			# padding = size//2 - fontsize//3
			# dc.blit(text,(size*x+padding,size*y+padding))
			
def main():
	pygame.font.init()
	pygame.init()
	pygame.display.set_caption("2048")
	dc = pygame.display.set_mode((MAP_SIZE, MAP_SIZE))
	clock = pygame.time.Clock()
	time = pygame.time.get_ticks()
	game2048 = Game2048()

	while True:
		game2048.blockAdd()
		game2048.blockAdd()
		printGame(game2048,dc)
		if (game2048.isSuccess()):
			messagebox.showinfo("Game2048","Success")
			break
		if (game2048.isFail()):
			messagebox.showinfo("Game2048","Fail")
			break
		eventGame(game2048,pygame.event.get())




		clock.tick(60)
		pygame.display.update()
	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	main()

scoreboard.mainloop()