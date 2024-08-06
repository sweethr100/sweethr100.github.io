import sys
import pygame
from puzzle import *
import os
import random
from tkinter import *
from tkinter import messagebox

def selectImage():
	images =[]
	for fname in os.listdir("image"):
		image = os.path.join("image",fname)
		if os.path.isfile(image):
			images.append(image)

	return random.choice(images)

MAP_SIZE = 500

def printGame(puzzle,dc):
	global img
	dc.fill((255,255,255))	
	# img = pygame.image.load("texture.png")
	img = pygame.transform.scale(img,(MAP_SIZE,MAP_SIZE))

	crops=[]
	for y in range(puzzle.size):
		for x in range(puzzle.size):
			crop = img.subsurface((MAP_SIZE/puzzle.size*x,MAP_SIZE/puzzle.size*y,MAP_SIZE/puzzle.size,MAP_SIZE/puzzle.size))
			crops.append(crop)

	for y in range(puzzle.size):
		for x in range(puzzle.size):
			if puzzle.data[y][x] != puzzle.size**2:
				dc.blit(crops[puzzle.data[y][x]-1],(MAP_SIZE/puzzle.size*x,MAP_SIZE/puzzle.size*y))
	# dc.blit(img,(0,0))
	for y in range(puzzle.size):
		for x in range(puzzle.size):
			pygame.draw.rect(dc,(127,127,127),[MAP_SIZE//puzzle.size*x,MAP_SIZE//puzzle.size*y,MAP_SIZE//puzzle.size,MAP_SIZE//puzzle.size],1)

def eventGame(puzzle,events):
	for event in events:
		if pygame.QUIT == event.type:
			pygame.quit()
			sys.exit(1)
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			rx,ry = event.pos
			x=int(rx/(MAP_SIZE/puzzle.size))
			y=int(ry/(MAP_SIZE/puzzle.size))

			rot = -1
			try:
				if puzzle.data[y-1][x] == puzzle.size**2:
					rot = 2
			except:
				pass
			try:
				if puzzle.data[y+1][x] == puzzle.size**2:
					rot = 0
			except:
				pass
			try:
				if puzzle.data[y][x-1] == puzzle.size**2:
					rot = 3
			except:
				pass	
			try:
				if puzzle.data[y][x+1] == puzzle.size**2:
					rot = 1
			except:
				pass
					
			puzzle.move(rot)
			#print(x,y)

def isend(puzzle):
	return puzzle.isEnd()

def main():
	global img

	pygame.font.init()
	pygame.init()
	pygame.display.set_caption("슬라이드퍼즐")
	dc = pygame.display.set_mode((MAP_SIZE, MAP_SIZE))
	clock = pygame.time.Clock()
	time = pygame.time.get_ticks()
	first = True

	for level in range(2,100):
		if not first:
			pygame.display.update()
			Tk().wm_withdraw()
			messagebox.showinfo("END","다음 스테이지?")
		first=False
		puzzle = Puzzle(level)
		img = pygame.image.load(selectImage())
		puzzle.random()

		while True:
			eventGame(puzzle,pygame.event.get())
			printGame(puzzle,dc)
			if isend(puzzle):
				print("Clear!")
				break

				pygame.quit()
				sys.exit()

			clock.tick(60)
			pygame.display.update()

if __name__ == "__main__":
	main()