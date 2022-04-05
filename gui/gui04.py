from tkinter import *
import tkinter.messagebox

window = Tk()


# 함수
def myFunc():
    if chk.get() == 0:
        tkinter.messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else:
        tkinter.messagebox.showinfo("", "체크버튼이  켜졌어요")


# 메인
chk = IntVar()  # 정수값 반환 DoubleVar() StringVar()
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

cb1.pack()
window.mainloop()
