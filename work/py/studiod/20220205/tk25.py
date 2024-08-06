from tkinter import *
from PIL import Image, ImageTk

def change_img():
    path = inputBox.get()

    inputBox.delete(0, 'end')

    try:
        img = PhotoImage(file=path)
        imageLabel.configure(image=img)
        imageLabel.image = img
    except:
        img = PhotoImage(file="kod.png")
        imageLabel.configure(image = img)
        imageLabel.image = img



window = Tk()

photo = PhotoImage(file="poket_picha.png")
imageLabel= Label(window,image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button= Button(window, text="Submit", command=change_img)
button.pack()

window.mainloop()