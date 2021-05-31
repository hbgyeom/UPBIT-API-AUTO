import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyupbit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("UPbit HTS v1.0")
        self.setWindowIcon(QIcon("doge.png"))
        
        self.access = QTextEdit("", self)
        self.access.move(10, 10)

        self.secret = QTextEdit("", self)
        self.secret.move(10, 45)

        self.run = QPushButton("Run", self)
        self.run.move(115, 10)
        self.run.resize(40, 65)
        self.run.clicked.connect(self.run_clicked)

    def run_clicked(self):
        print(self.access.toPlainText())
        print(self.secret.toPlainText())

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()