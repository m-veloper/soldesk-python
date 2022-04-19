import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TestForm(QMainWindow): #QMainWindow상속
    def __init__(self):
        super().__init__() # 상위클래스 생성자
        self.setupUI() # 구현

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800,400,500,500)

        label_1 = QLabel("입력테스트",self)
        label_2 = QLabel("출력테스트",self)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit = QLineEdit("", self)
        self.plainEdit = QPlainTextEdit(self)

        self.lineEdit.move(90,20)
        self.plainEdit.setGeometry(QRect(20,90,361,231))

        self.lineEdit.textChanged.connect(self.lineEditChanged)
        #enter
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        #상태바
        self.statusBar = QStatusBar(self) #선언
        self.setStatusBar(self.statusBar) #장착


    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text()) #insertPlainText : 줄바꿈 되지 않음
        self.lineEdit.clear() #Enter 후 clear

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
