import turtle
import random



def draw1(t):
    t.pu()
    t.goto(-200,-200)
    t.pd()
    t.left(90)
    t.fd(350)
def draw2(t):
    t.right(90)
    t.fd(250)
def draw3(t):
    t.right(90)
    t.fd(100)
    t.left(90)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
def draw4(t):
    t.right(90)
    t.fd(100)
    t.back(50)
def draw5(t):
    t.right(90)
    t.fd(50)
    t.back(100)
    t.fd(50)
    t.left(90)
def draw6(t):
    t.fd(50)
    t.right(30)
    t.fd(70)
    t.back(70)
    t.left(60)
    t.fd(70)



def random_word(fname):
    file = open(fname,"r",encoding="utf8")
    keywords = file.readlines()
    file.close()
    keyword = random.choice(keywords)
    return keyword.rstrip()

def update(answer,view,user):
    view = list(view)
    for i in range(len(answer)):
        if answer[i] == user:
            view[i] = user
    return "".join(view)

def isEnd(view):
    if "_" in view:
        return False

    return True

def draw(t,life):
    if life == 6:
        draw1(t)
    elif life == 5:
        draw2(t)
    elif life == 4:
        draw3(t)
    elif life == 3:
        draw4(t)
    elif life == 2:
        draw5(t)
    elif life == 1:
        draw6(t)
    elif life == 0:
        t.speed(0)
        t.pu()
        t.home()
        t.pd()
        draw1(t)
        t.speed(1)
        draw2(t)
        t.color("red")
        draw3(t)
        draw4(t)
        draw5(t)
        draw6(t)



if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(10)

    answer = random_word("dict.txt")
    view = "_"*len(answer)
    life = 7

    while True:
        tmp = list(view)
        tmp = " ".join(tmp)
        user = turtle.textinput("알파벳입력",view)[0]
        tview = view
        view = update(answer,view,user)
        if view == tview:
            life-=1
            draw(t,life)
        if isEnd(view) == True:
            print(answer)
            print("End")
            break
        if life <= 0:
            break

    turtle.mainloop()