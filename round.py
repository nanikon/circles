import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.krugs = []
        self.pushButton.clicked.connect(self.run)

    def run(self):
        r = randint(1, 100)
        x = randint(r, 800 - r)
        y = randint(r, 600 - r)
        self.krugs.append([x, y, r, r])

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draf(qp)
        qp.end()

    def draf(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in self.krugs:
            qp.drawEllipse(*i)
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())