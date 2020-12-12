import sys
from random import choice
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Жёлтые окружности')
        self.do_paint = False
        self.draw_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
    
    def draw_circle(self, qp):
        qp.setBrush(QColor(225, 225, 0))
        a = list(range(10, 300))
        radius = choice(a)
        qp.drawEllipse(300, 150, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())