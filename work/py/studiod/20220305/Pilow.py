from tkinter import *
from PIL import Image, ImageTk, ImageFilter

window = Tk()
canvas = Canvas(window,width=500,height=500)
canvas.pack()

img = Image.open("OIP.jfif")
# out = img.rotate(90)
out = img.filter(ImageFilter.BLUR)
tk_img = ImageTk.PhotoImage(out)
canvas.create_image(250,250,image=tk_img)

window.mainloop()