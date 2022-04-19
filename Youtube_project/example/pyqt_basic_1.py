import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)
label = QLabel("PyQT First Test!")
label.show()

print("Before Loop")
app.exec_() #mainloop() 실행처럼 이전까지의 실행이 반복됨 
print("After Loop") #  실행이 종료되면 loop에서 벗어나면서 출력
