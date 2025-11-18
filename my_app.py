from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QVBoxLayout
from instr import *

class Main_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(win_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
app = QApplication([])
main_win = Main_win()
app.exec_()