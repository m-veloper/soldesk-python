import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from pyqt_basic_ui import Ui_MainWindow

#form_class=uic.loadUiType('D:/Python_2022/ui/Python_basic.ui')[0]
#QMainWindow => [0] #QtWidgets.QMainWindow [1]
class TestForm(QMainWindow, Ui_MainWindow): #from_class의 loadUiType()를 이용하여 실행:TestForm(QMainWindow, form_class)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
