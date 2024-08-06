from tkinter import *
import time
import random

class Ball:
    def __init__(self):
        self.color="red"
        self.size=30
        self.y=0
        self.x=0
        self.xspeed = 0
        self.yspeed = 0

    def __init__(self, canvas, color, size, x, y, xspeed, yspeed):
        self.canvas=canvas
        self.color=color
        self.size=size
        self.y=y
        self.x=x
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.id = canvas.create_oval(x,y,x+size,y+size,fill=color)

    def move(self):
        # self.x+=self.xspeed
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1,y1,x2,y2) = self.canvas.coords(self.id)
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH:
            self.xspeed =- self.xspeed
        if y1 <= 0 or y2 >= HEIGHT:
            self.yspeed =- self.yspeed

# ballA = Ball("red",30,0,0,0,0)
#
# print("공의 색상=",ballA.color)
# print("공의 크시=", ballA.size)
# print("공의 x좌표=", ballA.x)
# print("")
#
# ballB = Ball("blue",100,50,50,10,10)
# print("공의 색상=",ballB.color)
# print("공의 크시=", ballB.size)
# print("공의 x좌표=", ballB.x)
# print("")

WIDTH = 800
HEIGHT = 400

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
# ball = Ball(canvas, "red",30,0,0,2.5,0)
# ball2 = Ball(canvas, "green",30,0,0,0,2.5)

ball_list = []
color_code="0123456789ABCDEF"
for i in range(50):
    color="#"
    for c in range(6):
        color+=random.choice(color_code)
    size = random.randint(10,100)
    x=random.randint(size, WIDTH-size)
    y=random.randint(size,HEIGHT-size)
    xspeed=random.randint(0,10)
    yspeed=random.randint(0,10)
    ball = Ball(canvas, color, size, x, y, xspeed, yspeed)
    ball_list.append(ball)

while True:
    for ball in ball_list:
        ball.move()
    window.update()
    time.sleep(0.03)

window.mainloop()