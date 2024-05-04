from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # перевірка типів значень, що вводяться
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
 
     
class MainWin(QWidget):
    def __init__(self):
        ''' вікно, в якому розташовується привітання '''
        super().__init__()
 
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
 
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
 
        #Встановлює зв'язки між елементами
        self.connects()

        # старт:
        self.show()
 
    def initUI(self):
        ''' створює графічні елементи '''
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
 
 
    def next_click(self):
        self.tw = TestWin()
        self.hide()
 
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
 
    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()
 
main()
