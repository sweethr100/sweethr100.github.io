from tkinter import *
from tkinter import messagebox, filedialog, scrolledtext
import subprocess

filename=""
code=""

def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        if messagebox.askokcancel("Quit", "정말로 종료하시겠습니까?"):
            if messagebox.askokcancel("Quit", "진짜 정말로 종료하시겠습니까?"):
                window.destroy()

def saveFile():
    global filename
    global code

    txt = codeview.get("1.0", END)
    code = txt

    if filename == "":
        file = filedialog.asksaveasfile(parent=window,mode='w', filetypes=(('All files','*'),))
        if file != None:
            filename=file.name
            file.write(txt)
            file.close()
    else:
        file = open(filename,"w")
        file.write(txt)
        file.close()

def openFile():
    global filename
    global code
    file = filedialog.askopenfile(parent=window,mode='r', filetypes=(
            ('Text files','*.txt'),('Python files','*.py'),('All files','*')
        ))
    if file != None:
        filename=file.name
        txt = file.read()
        code=txt
        codeview.delete("1.0", END)
        codeview.insert("1.0", txt)
        file.close()

def pyrun():
    if filename == "":
        if messagebox.askokcancel("Save","저장하시겠습니까?"):
            saveFile()
        else:
            return
    if code != codeview.get("1.0",END):
        if messagebox.askokcancel("Save","번경사항을 저장하시겠습니까?"):
            saveFile()
    re=""
    try:
        re = subprocess.check_output(['python', filename],text=True,stderr=subprocess.STDOUT)
    except Exception as e:
        re = e
    codeoutput.delete("1.0", END)
    codeoutput.insert("1.0", re)

def shutdown():
    pass


window = Tk()
window.title("메모장 v2")
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
filemenu.add_command(label="열기", command=openFile)
filemenu.add_command(label="저장", command=saveFile)
filemenu.add_command(label="종료", command=exit)
menu.add_cascade(label="파일", menu=filemenu)
runmenu = Menu(menu)
runmenu.add_command(label="파이썬으로 실행", command=pyrun)
runmenu.add_command(label="컴퓨터 끄기", command=shutdown)
menu.add_cascade(label="실행", menu=runmenu)

codeview= scrolledtext.ScrolledText(window)
codeview.config(width=200,height=25,font=("궁서", 20), fg="#FFF", bg="#00001B")
codeview.pack()

codeoutput= scrolledtext.ScrolledText(window)
codeoutput.config(width=200,height=25,font=("ms outlook", 20), fg="#FFF", bg="#000")
codeoutput.pack()

window.mainloop()