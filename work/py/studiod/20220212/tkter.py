from tkinter import *
from functools import partial
from random import *
img=[]
button_list = ["가위","바위","보"]

def run(user):
    com = choice(button_list)
    re = ""
    if user == com:
        re = "비김"
    elif (com=="가위" and user == "바위") or (com=="바위" and user == "보") or (com=="보" and user == "가위"):
        re="승리"
    else:
        re = "패배"
    entry.delete(0, 'end')
    entry.insert(0, re)
    img = PhotoImage(file = com+".png")
    combutton.configure(image = img)
    combutton.image = img

window = Tk()
window.title("가위바위보")
x = 0

for b in button_list:
    help = partial(run,b)
    img.append(PhotoImage(file=b+".png"))

    button = Button(image=img[x], command=help)
    button.grid(row=0,column=x)
    x+=1

entry = Entry(width="40", font="바탕 15 bold",justify="center")
entry.grid(row=1, column=0, columnspan=3)
comimg = PhotoImage(file="com.png")
combutton= Button(image=comimg)
combutton.grid(row=2, column=1)

window.mainloop()