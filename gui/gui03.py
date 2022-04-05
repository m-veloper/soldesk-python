from tkinter import *
import tkinter.messagebox


# 함수
def myFunc():
    tkinter.messagebox.showinfo("강아지 버튼", "사랑스런 강아지~~")


# 메인
window = Tk()

photo = PhotoImage(file="E:/Python/GIF/dog2.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()
window.mainloop()
