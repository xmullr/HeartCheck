from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QWidget, QApplication, QVBoxLayout, QHBoxLayout
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.timer = QLabel(txt_timer)
        
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        
        self.text_starttest1 = QPushButton(txt_starttest1)
        self.text_starttest2 = QPushButton(txt_starttest2)
        self.text_starttest3 = QPushButton(txt_starttest3)
        self.text_sendresults = QPushButton(txt_sendresults)
        
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.l_line.addWidget(self.text_name)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1)
        self.l_line.addWidget(self.text_starttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2)
        self.l_line.addWidget(self.text_starttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3)
        self.l_line.addWidget(self.text_starttest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_sendresults, alignment = Qt.AlignCenter)

        self.r_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.text_sendresults.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.final_win = FinalWin()
