# 입력
# 첫째 줄에 다섯 자리인 양의 정수 n이 주어진다. 
# 출력
# 첫째 줄에 각 자릿수의 다섯제곱의 합을 출력하라.

# def soultion(num):
# 	s=0
# 	for i in str(num):
# 		s+= int(i)**5
# 	return s


# if __name__ == "__main__":

# 	for i in range(10000,100000):
# 		if i == soultion(i):
# 			print(i)



from turtle import *
import random
import math
class Ball:
	def __init__(self,color,size):
		self.x=0
		self.y=0

		self.size=size
		self.color = color

		turtle = Turtle()
		turtle.shape("circle")
		turtle.color(color,color)
		turtle.resizemode("user")
		turtle.shapesize(size,size,10)
		turtle.penup()
		self.turtle=turtle


	def move(self):
		speed=30
		self.x+=random.randint(-speed, speed)
		self.y+=random.randint(-speed, speed)
		if self.x < -450:
			self.x = -450
		elif self.x > 450:
			self.x=450
		if self.y <-375:
			self.y = -375
		elif self.y>375:
			self.y=375
		self.turtle.goto(self.x,self.y)

	def usermove(self):
		if self.x < -450:
			self.x = -450
		elif self.x > 450:
			self.x=450
		if self.y <-375:
			self.y = -375
		elif self.y>375:
			self.y=375
		self.turtle.goto(self.x,self.y)


def check(red):
	if distinct(user.x,user.y,red.x,red.y) < 50:
		print("충돌")
		print(distinct(user.x,user.y,red.x,red.y))
		return True

def distinct(x,y,tx,ty):
	c = (x-tx)**2 + (y-ty)**2
	return math.sqrt(c)
def up():
	user.y+=user.speed
	user.usermove()
	for red in reds:
		if check(red):
			end()
def down():
	user.y-=user.speed
	user.usermove()
	for red in reds:
		if check(red):
			end()
def left():
	user.x-=user.speed
	user.usermove()
	for red in reds:
		if check(red):
			end()
def right():
	user.x+=user.speed
	user.usermove()
	for red in reds:
		if check(red):
			end()

def end():
	user.turtle.pendown()
	user.turtle.color("#AAB8B8")
	user.size+=1
	user.turtle.shapesize(user.size,user.size,10)



user = Ball("#CEFBC9", 2)
user.speed = 40
user.turtle.speed(0)
user.x = -450
user.y=-375
user.turtle.goto(user.x,user.y)

reds = []
if __name__ == "__main__":
	# print(distinct(13,14,10,10))
	# print(distinct(-5,5,-8,9))
	screen = Screen()
	screen.bgcolor("#F8FFFF")
	screen.onkeypress(left, "Left")
	screen.onkeypress(right, "Right")
	screen.onkeypress(up, "Up")
	screen.onkeypress(down, "Down")
	screen.listen()


	for i  in range(10):
		reds.append(Ball("#FFA7A7", 2))
	reds.append(Ball("#3e4546", 3))
	while True:
		for red in reds:
			red.move()
			if check(red):
				end()

	mainloop()


