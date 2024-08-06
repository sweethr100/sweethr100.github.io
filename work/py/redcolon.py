import turtle
import random
def createArmy():
    t = turtle.Turtle()
    t.shape("circle")
    t.color("red")
    t.speed(0)
    t.penup()
    return t
def moveArmy(t):
    t.left(random.randint(0,360))
    t.fd(random.randint(1,50))
def up():
    user.fd(10)
def down():
    user.back(10)
def left():
    user.left(45)
def right():
    user.right(45)

user = turtle.Turtle()
user.color("blue")
user.shape("turtle")
user.speed(0)
user.penup()
screan = turtle.Screen()
screan.onkeypress(up,"Up")
screan.onkeypress(down,"Down")
screan.onkeypress(left,"Left")
screan.onkeypress(right,"Right")
screan.listen()

ts = []
for i in range(10):
    t=createArmy()
    ts.append(t)

while True:
    for i in range(10):
        moveArmy(ts[i])
turtle.mainloop()