import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TestForm(QMainWindow):  # QMainWindow상속
    def __init__(self):
        super().__init__()  # 상위클래스 생성자
        self.setupUI()  # 구현

    def setupUI(self):
        self.setWindowTitle("PyQT Test")  # 창제목
        self.setGeometry(800, 400, 500, 300)  # 창크기

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("Click3", self)

        btn_1.move(20, 20)
        btn_2.move(20, 60)
        btn_3.move(20, 100)

        btn_1.clicked.connect(self.btn_1_clicked)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)

    def btn_1_clicked(self):
        QMessageBox.about(self, "message", "clciked")

    def btn_2_clicked(self):
        print(self, "Button Clciked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
