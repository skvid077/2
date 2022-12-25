import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.point = None
        self.mouseCoord = None
        self.setMouseTracking(True)
        self.btn = ''
        self.x, self.y = 0, 0

    def getRandomSize(self):
        return random.randint(10, 300)

    def getRandomColor(self):
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.point:
            return
        else:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.btn = "левая"
            self.point = event.pos()
            self.x, self.y = event.x(), event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.point = None

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        x = random.randrange(1, 500)
        if self.btn == 'левая':
            qp.setBrush(self.getRandomColor())
            qp.drawEllipse(self.x, self.y, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
