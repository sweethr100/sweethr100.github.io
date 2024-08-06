from tkinter import *
from tkinter import messagebox, filedialog, scrolledtext
import subprocess

filename=""
code=""

def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
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

def saveasFile():
    global filename
    global code

    txt = codeview.get("1.0", END)
    code = txt
    file = filedialog.asksaveasfile(parent=window,mode='w', filetypes=(('All files','*'),))
    if file != None:
        filename=file.name
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
    if messagebox.askokcancel("Shutdown","컴퓨터를 종료하시겠습니까?"):
        subprocess.Popen("shutdown /s /t 0")


window = Tk()
window.title("메모장 v2")
window.geometry("1800x900")
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
filemenu.add_command(label="열기", command=openFile)
filemenu.add_command(label="저장", command=saveFile)
filemenu.add_command(label="다른 이름으로 저장", command=saveasFile)
filemenu.add_command(label="종료", command=exit)
menu.add_cascade(label="파일", menu=filemenu)
runmenu = Menu(menu)
runmenu.add_command(label="파이썬으로 실행", command=pyrun)
runmenu.add_command(label="컴퓨터 끄기", command=shutdown)
menu.add_cascade(label="실행", menu=runmenu)

codeview= scrolledtext.ScrolledText(window)
codeview.config(width=300,height=25,font=("맑은 고딕", 15), fg="#FFF", bg="#40444b")
codeview.pack()

codeoutput= scrolledtext.ScrolledText(window)
codeoutput.config(width=300,height=100,font=("ms outlook", 15), fg="#FFF", bg="#202225")
codeoutput.pack()

window.mainloop()