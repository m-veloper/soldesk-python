from tkinter import *

window = Tk()


def test():
    button1 = Button(window, text="파이썬 종료", fg="red", command=quit)

    button1.pack()


window.mainloop()
