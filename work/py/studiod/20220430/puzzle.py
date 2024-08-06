import random
import os

class Puzzle():
	def __init__(self,size=2):
		self.data = []
		self.size = size

		cnt=1
		for y in range(size):
			tmp=[]
			for x in range(size):
				tmp.append(cnt)
				cnt+=1
			self.data.append(tmp)

	def run(self):
		self.random()
		while True:
			self.print()
			if self.isEnd():
				break
			key = self.input()
			self.move(key)

	def isEnd(self):
		cnt = 1
		for y in range(self.size):
			for x in range(self.size):
				if self.data[y][x] != cnt:
					return False
				cnt+=1
		return True

	def random(self):
		for i in range(self.size**2*100):
			r = random.randint(0,3)
			self.move(r)

	def move(self,rot):
		x,y = self.getPos()
		if rot==0:
			self.swap(x, y, x, y-1)
		elif rot==1:
			self.swap(x, y, x-1, y)
		elif rot==2:
			self.swap(x, y, x, y+1)
		elif rot==3:
			self.swap(x, y, x+1, y)


	def swap(self,x,y,tx,ty):
		if tx < 0 or tx >= self.size or ty < 0 or ty >= self.size:
			return
		self.data[y][x],self.data[ty][tx] = self.data[ty][tx],self.data[y][x]

	def getPos(self):
		for y in range(len(self.data)):
			for x in range(len(self.data[y])):
				if self.data[y][x] == self.size**2:
					return x,y
		return None,None

	def input(self):
		user = input(">:")
		if user == "w":
			return 0
		elif user == "a":
			return 1
		elif user == "s":
			return 2
		elif user == "d":
			return 3
		else:
			return -1

	def print(self):
		os.system("cls")
		for y in self.data:
			for x in y:
				if x == self.size**2:
					print("   ",end="")
				else:
					print("%3d"%x,end="")
			print("")


if __name__ == "__main__":
	for i in range(2,10):
		puzzle = Puzzle(i)
		puzzle.run()
		os.system("pause")