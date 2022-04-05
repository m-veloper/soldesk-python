from tkinter import *
import tkinter.messagebox

'''
def clickLeft(event):
    tkinter.messagebox.showinfo("마우스", "왼쪽 마우스가 클릭됨")

#메인
window=Tk()
window.bind("<Button-1>", clickLeft)
'''
'''
def clickImage(event):
    tkinter.messagebox.showinfo("마우스", "토끼사진에서  마우스가 클릭됨")

#메인
window=Tk()
window.geometry("400x400")
photo=PhotoImage(file="E:/Python/GIF/rabbit.gif")
label1=Label(window, image=photo)

label1.bind("<Button>", clickImage)
label1.pack(expand=1, anchor=CENTER)

'''


def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("

    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label1.configure(text=txt)


# 메인
window = Tk()
window.geometry("400x400")
label1 = Label(window, text="바로여기 => 이곳에 바뀜")

window.bind("<Button>", clickMouse)
label1.pack(expand=1, anchor=CENTER)

window.mainloop()
