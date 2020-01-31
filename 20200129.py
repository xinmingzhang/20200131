import sys
from PyQt5.QtWidgets import QDialog,QApplication,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap,QPainter,QPainterPath,QPen
from PyQt5.QtCore import QPointF,QRect,QPropertyAnimation,QEvent,Qt
from uitest import *

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.pixmap = QPixmap()
        self.pixmap.load('game_map.png')
        self.item = QGraphicsPixmapItem(self.pixmap)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.pushButton.clicked.connect(self.startanimation)
        self.path = QPainterPath()
        self.path.moveTo(30,30)
        self.path.cubicTo(30,30,80,180,180,170)
        self.ui.label.pos = QPointF(20,20)
        self.pos1 = [0,0]
        self.pos2 = [0,0]

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0] = event.x()
            self.pos1[1] = event.y()

    def mouseReleaseEvent(self, event):
        self.pos2[0] = event.x()
        self.pos2[1] = event.y()
        self.update()

    def paintEvent(self, event):
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]
        rect = QRect(self.pos1[0],self.pos1[1],width,height)
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.red,3)
        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawArc(rect,0,360*16)
        qp.end()



    # def paintEvent(self,e):
    #     qp = QPainter()
    #     qp.begin(self)
    #     qp.drawPath(self.path)
    #     qp.end()

    def startanimation(self):
        self.anim = QPropertyAnimation(self.ui.label, b'pos')
        self.anim.setDuration(4000)
        self.anim.setStartValue(QPointF(20,20))
        pos = [n/80 for n in range(0,50)]
        for i in pos:
            self.anim.setKeyValueAt(i,self.path.pointAtPercent(i))
            self.anim.setEndValue(QPointF(160,150))
        self.anim.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec())