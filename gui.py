import sys
from PyQt5.QtCore import forcepoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyupbit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("upbit hts v1.0")
        self.setWindowIcon(QIcon("doge.png"))
        
        self.access = QLineEdit("", self)
        self.access.move(10, 10)
        self.access.resize(100, 20)
        self.access.setEchoMode(QLineEdit.Password)

        self.secret = QLineEdit("", self)
        self.secret.move(10, 35)
        self.secret.resize(100, 20)
        self.secret.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("run", self)
        self.button.move(115, 9)
        self.button.resize(40, 48)
        self.button.clicked.connect(self.run_clicked)

        self.error_message = QLabel("", self)
        self.error_message.move(10, 50)
        self.error_message.setStyleSheet("color: red;")
        
    def run_clicked(self):
        if self.button.text() == "run":
            access_key = self.access.text()
            secret_key = self.secret.text()
            if len(access_key) != 40 and len(secret_key) != 40:
                self.access.clear()
                self.secret.clear()
                self.error_message.setText("wrong key")
            elif len(access_key) == 40 and len(secret_key) != 40:
                self.secret.clear()
                self.error_message.setText("wrong key")
            elif len(access_key) != 40 and len(secret_key) == 40:
                self.access.clear()
                self.error_message.setText("wrong key")
            else:
                self.error_message.clear()
                upbit = pyupbit.Upbit(access_key, secret_key)
                print(upbit.get_balance("KRW"))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()