import sys
from random import choice

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Случайные окружности')
        self.do_paint = False
        self.draw_button = QPushButton('Рисовать', self)
        self.draw_button.resize(100, 25)
        self.draw_button.move(260, 25)
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
        a = list(range(255))
        r, g, b = choice(a), choice(a), choice(a)
        qp.setBrush(QColor(r, g, b))
        c = list(range(10, 300))
        radius = choice(c)
        qp.drawEllipse(200, 150, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())