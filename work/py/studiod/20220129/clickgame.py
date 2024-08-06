from tkinter import *
import sys
cnt = 0
flag = True

def click():
    global cnt
    cnt+=1
    count.delete(0, 'end')
    count.insert(0,str(cnt))
    if cnt >= 777:
        print("10000 클릭 OK")
        sys.exit(1)

def event():
    global flag
    if flag:
        click()
        flag=False
def event2():
    global flag
    if not flag:
        click()
        flag=True

window = Tk()
title = Label(window, text="클릭게임")
title.pack()
count = Entry(window, font="궁서체 16 bold", fg="green", bg="yellow")
count.insert(0, str(cnt))
count.pack()
b1 = Button(window,text="Click Me", command=event, width="30", bg="RED")
b1.pack()
b2 = Button(window,text="Click Me2", command=event2, width="30", bg="BLUE")
b2.pack()

window.mainloop()