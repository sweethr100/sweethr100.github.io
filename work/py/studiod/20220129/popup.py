from tkinter import *

def process():
    f = float(e1.get())

    c = (f-32)*5/9
    e2.delete(0, 'end')

    e2.insert(0, str(c))

def process2():
    c = float(e2.get())

    f = c*9/5+32
    e1.delete(0, 'end')

    e1.insert(0, str(f))

window = Tk()

l1 = Label(window, text="화씨", font='nirmalaui 16 italic')
l2 = Label(window, text="섭씨", font='nimalaui 16 italic')
l1.grid(row=0, column=0)
l2.grid(row=1,column=0)

e1 = Entry(window, bg="yellow", fg="white")
e2 = Entry(window, bg="yellow", fg="white")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=process)
b2 = Button(window, text="섭씨->화씨", command=process2)
b1.grid(row=2, column=0)
b2.grid(row=2,column=1)

window.mainloop()
