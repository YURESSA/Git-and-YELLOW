import sys
from random import choice, randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui import Ui_MainWindow

class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.drawing(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawing(self, qp):
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.qp.setBrush(QColor(choice(self.colors)))
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
