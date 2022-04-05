from tkinter import *

window = Tk()


# 함수
def myFunc():
    if var.get() == 1:
        label1.configure(text='Python')
    elif var.get() == 2:
        label1.configure(text='Spring')
    else:
        label1.configure(text="BigData")


# 메인
var = IntVar()
rb1 = Radiobutton(window, text="Python", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="Spring", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="BigData", variable=var, value=3, command=myFunc)

label1 = Label(window, text="선택한 강좌 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
