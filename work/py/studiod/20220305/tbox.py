from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk, ImageFilter

im = None
tk_img = None
fname = None

def open():
    global im,tk_img,fname
    fname = filedialog.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image=tk_img)
    window.update()

def save():
    global fname, im
    fname = filedialog.asksaveasfilename(filetypes=(('PNG files','*.png'),))
    im.save(fname,fname.split(".")[-1])

def quit():
    window.quit()

def rotate():
    global im,tk_img
    if im != None:
        im = im.rotate(90)
        tk_img = ImageTk.PhotoImage(im)
        canvas.create_image(250,250,image=tk_img)
        window.update()

def blur():
    global im, tk_img
    if im != None:
        im = im.filter(ImageFilter.BLUR)
        tk_img = ImageTk.PhotoImage(im)
        canvas.create_image(250,250,image=tk_img)
        window.update()

def smooth():
    global im, tk_img
    if im != None:
        im = im.filter(ImageFilter.SMOOTH)
        tk_img = ImageTk.PhotoImage(im)
        canvas.create_image(250,250,image=tk_img)
        window.update()

def edge_enhace():
    global im, tk_img
    if im != None:
        im = im.filter(ImageFilter.EDGE_ENHANCE)
        tk_img = ImageTk.PhotoImage(im)
        canvas.create_image(250,250,image=tk_img)
        window.update()

def reset():
    global im,tk_img,fname
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image=tk_img)
    window.update()

window = Tk()

menu = Menu(window)
window.config(menu=menu)
window.title("메롱")

filemenu = Menu(menu)

filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="저장",command=save)
filemenu.add_command(labe="종료",command=quit)
menu.add_cascade(label="파일", menu=filemenu)

imgmenu = Menu(menu)

imgmenu.add_command(label="회전",command=rotate)
imgmenu.add_command(label="흐리게",command=blur)
imgmenu.add_command(label="부드럽게",command=smooth)
imgmenu.add_command(label="엣지 어쩌고 저쩌고",command=edge_enhace)
imgmenu.add_command(label="원상복귀",command=reset)
menu.add_cascade(label="영상처리",menu=imgmenu)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

window.mainloop()