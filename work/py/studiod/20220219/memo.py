from tkinter import *
from tkinter import messagebox, filedialog
import os

def open():
    file = filedialog.askopenfile(parent=window,mode="r", filetypes=(
            ('Text files','*.txt'),('Python files','*.py'),('All files','*')
        )
    )
    if file != None:
        lines= file.read()
        text.insert('1.0', lines)
        file.close()

def save():
    file = filedialog.asksaveasfile(parent=window,mode="w")
    if file != None:
        lines= text.get("1.0",END)
        file.write(lines)
        file.close()
def close():
    flag = messagebox.askokcancel("Quit","종료하시겠습니까?")
    if flag:
        window.destroy()
def info():
    messagebox.showinfo("About","ㅁㅔ모장 프로그램")
def run():
    lines = text.get("1.0",END)
    lines = lines.replace("\n",";")
    lines = lines.replace("\"","\\\"")
    lines = lines.replace("\'","\\\'")
    cmd = 'python -c "'+lines+'"'
    os.system(cmd)
    pass

window = Tk()
window.title("수제 메모장")

text = Text(window,width=80,height=20)
text.pack()

result = Text(window,width=80,height=10)
result.pack()

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장", command=save)
filemenu.add_command(label="실행", command=run)
filemenu.add_command(label="종료", command=close)

helpmenu = Menu(menu)
helpmenu.add_command(label="프로그램 정보", command=info)
menu.add_cascade(label="도움말", menu=helpmenu)


window.mainloop()