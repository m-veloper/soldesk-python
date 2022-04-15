import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from lib.you_viewer_layout import Ui_MainWindow
from PyQt5 import QtWebEngineWidgets
import re
import datetime

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #UI
        self.setupUi(self) #lib.you_viewer_layout 호출
        self.initAuthLock() #인증버튼들 메소드 호출

    #기본 UI 비활성화
    def initAuthLock(self):
         self.previewButton.setEnabled(False)
         self.fileNavButton.setEnabled(False)
         self.streamCombobox.setEnabled(False)
         self.startButton.setEnabled(False)
         self.calendarWidget.setEnabled(False)
         self.urlTextEdit.setEnabled(False)
         self.pathTextEdit.setEnabled(False)
         self.showStatusMsg('인증안됨')

    #기본 UI 비활성화
    def initAuthActive(self):
         self.previewButton.setEnabled(True)
         self.fileNavButton.setEnabled(True)
         self.streamCombobox.setEnabled(True)
         self.startButton.setEnabled(True)
         self.calendarWidget.setEnabled(True)
         self.urlTextEdit.setEnabled(True)
         self.pathTextEdit.setEnabled(True)
         self.showStatusMsg('인증완료')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    you_viewer_main = Main() #화면의 객체
    you_viewer_main.show()
    app.exec_()
