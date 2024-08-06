from tkinter import *
import time
import random
# import turtle
#
#
# turtle = Turtle()
# turtle.fd(10)
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
        self.life = 3

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

clickTime = 0
def fire(event):
    global clickTime
    ctime = time.time()
    if clickTime+1.1 <= ctime:
        clickTime = ctime
        bullets.append(Ball(canvas, "green", 10, 25, event.y, 10, 0))
canvas.bind("<Button-1>",fire)

def remove():
    i=0
    while i<len(bullets):
        flag = False
        j=0
        while j<len(ball_list):
            (ax1, ay1, ax2, ay2) = canvas.coords(ball_list[j].id)
            (ux1, uy1, ux2, uy2) = canvas.coords(bullets[i].id)

            if ax1 < ux1 and ay1 < uy1 and ax2 > ux2 and ay2 > uy2:
                flag=True
                ball_list[j].life -=1
                if ball_list[j].life <= 0:
                    canvas.delete(ball_list[j].id)
                    del ball_list[j]
                    j-=1
            j+=1

        if bullets[i].x > 750:
            flag=True
        if flag:
            canvas.delete(bullets[i].id)
            del bullets[i]
        else:
            i+=1

def createBall():
    if len(ball_list) < 4:

        color_code = "0123456789ABCDEF"
        for i in range(50):
            color = "#"
            for c in range(6):
                color += random.choice(color_code)
            size = random.randint(45, 55)
            x = random.randint(450, 750)
            y = random.randint(20, 380)
            yspeed = random.randint(1, 20)

        ball = Ball(canvas, color, size, x, y, 0, yspeed)
        ball_list.append(ball)

ball_list = []
bullets = []

while True:
    createBall()
    for ball in ball_list:
        ball.move()
    for ball in bullets:
        ball.move()
    remove()
    window.update()
    time.sleep(0.03)

window.mainloop()