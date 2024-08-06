from tkinter import *
from functools import partial

window =Tk()
window.title("My Calculator")
display = Entry(window, width=33,bg="yellow")
display.grid(row=0, column=0, columnspan=5)

def run(data):
    if data=='c':
        display.delete(0,'end')
    elif data == '=':
        fun = display.get()
        re=""
        try:
            re = eval(fun)
        except:
            re="err"
        print(re)
        display.delete(0,'end')
        display.insert('end', re)

    else:
        display.insert('end', data)

button_lst =[
    ['7','8','9','/','c'],
    ['4','5','6','*',''],
    ['1','2','3','-',''],
    ['0','.','=','+','']
]

for y in range(len(button_lst)):
    for x in range(len(button_lst[y])):
        help = partial(run, button_lst[y][x])
        button = Button(window, text=button_lst[y][x], width=5, command=help)
        button.grid(row=y+1, column=x)

window.mainloop()