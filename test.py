import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPixmap,QPainter,QBitmap
from PyQt5.QtCore import QCoreApplication,QPropertyAnimation
from PyQt5.Qt import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.pix = QPixmap("bg2.jpg")
        desktop = QApplication.desktop()
        screen = desktop.screenGeometry()
        self.h = screen.height()
        self.w = screen.width()
        self.resize(self.w,self.h)
        # self.animation = QPropertyAnimation(self,b'windowOpacity')
        # self.animation.setDuration(5000)
        # self.animation.setStartValue(0)
        # self.animation.setEndValue(0.5)
        # self.animation.start()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self\
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QCoreApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())


