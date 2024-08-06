from tkinter import *
from functools import partial

color = "black"
colors = ["red", "orange", "yellow", "lime", "green", "skyblue", "blue", "purple", "pink", "black", "white", "#F0F0F0"]

def paint(event):
    width = int(entry.get())
    x, y = event.x, event.y
    if color == "#F0F0F0":
        canvas.create_oval(x-width*4,y-width*4,x+width*4,y+width*4, fill=color, outline=color)
    else:
        canvas.create_oval(x-width/0.5,y-width/0.5,x+width/0.5,y+width/0.5, fill=color, outline=color)

def chageColor(i):
    global color
    color=colors[i]

window = Tk()
window.title("그림판")
window.geometry("500x500")

canvas=Canvas(window)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", paint)

for i in range(len(colors)):
    help = partial(chageColor,i)
    button = Button(window,text="    ", fg=colors[i], bg=colors[i], command=help)
    button.place(x=25*i,y=0)

entry = Entry(window)
entry.place(x=0,y=25)

window.mainloop()