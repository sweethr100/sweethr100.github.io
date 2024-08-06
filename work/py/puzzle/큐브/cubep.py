import random
import os

def createMap(cnt=3):
	data = []
	i=1
	for y in range(cnt):
		tmp = []
		for x in range(cnt):
			tmp.append(i)
			i+=1
		data.append(tmp)
	return data

def showMap(data=[],cnt=3):
	for j in data:
		for i in j:
			if i != cnt*cnt:
				print("%4d"%i,end="")
			else:
				print("    ",end="")
		print("")

def userinput():
	user = input("입력 : ")
	return user
def getXY(data,cnt):
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == cnt*cnt:
				return x,y

def move(data,cnt,x,y,tx,ty):
	if ty < 0 or tx <0 or ty >=cnt or tx >= cnt:
		return

	data[y][x],data[ty][tx] = data[ty][tx], data[y][x]

def movement(data,level,x,y,user):
	if user == "w":
		move(data, level, x, y, x, y-1)
	elif user=="s":
		move(data, level, x, y, x, y+1)
	elif user=="a":
		move(data, level, x, y, x-1, y)
	elif user=="d":
		move(data, level, x, y, x+1, y)

def mix(data,level):
	flags = ['w','a','s','d']
	for i in range(mx):
		r = random.choice(flags)
		x,y = getXY(data,level)
		movement(data, level, x, y, r)
	return data

def isEnd(data,level):
	l = 1
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == l:
				pass
			else:
				return False
			l+=1
	return True

mx = int(input("난이도를 설정해 주세요 (기본값 : 500) : "))

if __name__ == "__main__":
	for level in range(2,11):
		data = createMap(level)
		data = mix(data,level)
		while True:
			os.system("cls")
			showMap(data,level)
			if isEnd(data,level):
				break
			x, y = getXY(data, level)
			user = userinput()
			movement(data, level, x, y, user)
		