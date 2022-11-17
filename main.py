import sys
from random import choice, randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.qp = QPainter()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.drawing(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawing(self, qp):
        self.qp.setBrush(QColor('yellow'))
        print(1)
        a = randint(1, 200)
        b = randint(50, 400)
        self.qp.drawEllipse(a, b, b, b)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
