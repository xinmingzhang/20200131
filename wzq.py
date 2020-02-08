import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QWidget,QMessageBox
from PyQt5.QtGui import QColor,QPainter,QFont
from PyQt5.QtCore import QPoint,pyqtSignal,QCoreApplication


class Board(QWidget):

    ending_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_game()

    def init_game(self):
        self.win = None
        self.turn = 'black'
        self.black_piece_pos = []
        self.white_piece_pos = []
        self.ending_signal.connect(self.show_ending_message)
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255,215,0))
        qp.drawRect(0,0,self.width()-1,self.height()-1)
        points_list =[x for x in range(32,962,62)]
        for i in points_list:
            qp.drawLine(i,32,i,900)
            qp.drawLine(32,i,900,i)
        qp.setPen(QColor('black'))
        qp.setFont(QFont('SimSun',10))
        string_1 = [str(x) for x in range(1,16)]
        string_2 = 'abcdefghijklmno'
        for i,j in zip(points_list,string_1):
            qp.drawText(i,933,j)
        for i,j in zip(points_list,string_2):
            qp.drawText(930,i,j)
        qp.setBrush(QColor('black'))
        for pos in self.black_piece_pos:
            qp.drawEllipse(pos,30,30)
        qp.setBrush(QColor('white'))
        for pos in self.white_piece_pos:
            qp.drawEllipse(pos,30,30)
        qp.end()

    def mousePressEvent(self, e):
        if e.pos().x() < 962 and e.pos().y() < 962:
            pos = self.cal_pos(e.pos())
            if (pos not in self.black_piece_pos) and (pos not in self.white_piece_pos):
                if self.turn == 'black':
                    self.black_piece_pos.append(pos)
                    self.check_win(pos)
                elif self.turn == 'white':
                    self.white_piece_pos.append(pos)
                    self.check_win(pos)

        self.update()

    def change_turn(self):
        if self.turn == 'black':
            self.turn = 'white'
        elif self.turn == 'white':
            self.turn = 'black'

    def check_win(self,pos):
        x, y= pos.x(),pos.y()
        condition= {}
        condition[1] = [QPoint(x+62,y),QPoint(x+62*2,y),QPoint(x+62*3,y),QPoint(x+62*4,y)]
        condition[2] = [QPoint(x+62,y),QPoint(x+62*2,y),QPoint(x+62*3,y),QPoint(x-62,y)]
        condition[3] = [QPoint(x + 62, y), QPoint(x + 62 * 2, y), QPoint(x -62, y), QPoint(x - 62 * 2, y)]
        condition[4] = [QPoint(x + 62, y), QPoint(x - 62, y), QPoint(x - 62 * 2, y), QPoint(x - 62 * 3, y)]
        condition[5] = [QPoint(x - 62*4, y), QPoint(x - 62 * 3, y), QPoint(x - 62 * 2, y), QPoint(x - 62 * 1, y)]
        condition[6] = [QPoint(x,y+62),QPoint(x,y+62*2),QPoint(x,y+62*3),QPoint(x,y+62*4)]
        condition[7] = [QPoint(x,y+62),QPoint(x,y+62*2),QPoint(x,y+62*3),QPoint(x,y-62)]
        condition[8] = [QPoint(x , y+ 62), QPoint(x , y+ 62 * 2), QPoint(x , y-62), QPoint(x , y- 62 * 2)]
        condition[9] = [QPoint(x , y+ 62), QPoint(x, y - 62), QPoint(x, y - 62 * 2), QPoint(x , y- 62 * 3)]
        condition[10] = [QPoint(x , y- 62*4), QPoint(x , y- 62 * 3), QPoint(x , y- 62 * 2), QPoint(x , y- 62 * 1)]
        condition[11] = [QPoint(x+62,y+62),QPoint(x+62*2,y+62*2),QPoint(x+62*3,y+62*3),QPoint(x+62*4,y+62*4)]
        condition[12] = [QPoint(x+62,y+62),QPoint(x+62*2,y+62*2),QPoint(x+62*3,y+62*3),QPoint(x-62,y-62)]
        condition[13] = [QPoint(x + 62, y+ 62), QPoint(x + 62 * 2, y + 62 * 2), QPoint(x -62, y-62), QPoint(x - 62 * 2, y- 62 * 2)]
        condition[14] = [QPoint(x + 62, y+ 62), QPoint(x - 62, y- 62), QPoint(x - 62 * 2, y- 62 * 2), QPoint(x - 62 * 3, y- 62 * 3)]
        condition[15] = [QPoint(x - 62*4, y- 62*4), QPoint(x - 62 * 3, y- 62 * 3), QPoint(x - 62 * 2, y- 62 * 2), QPoint(x - 62 * 1, y - 62 * 1)]
        condition[16] = [QPoint(x-62,y+62),QPoint(x-62*2,y+62*2),QPoint(x-62*3,y+62*3),QPoint(x-62*4,y+62*4)]
        condition[17] = [QPoint(x-62,y+62),QPoint(x-62*2,y+62*2),QPoint(x-62*3,y+62*3),QPoint(x+62,y-62)]
        condition[18] = [QPoint(x -62, y+ 62), QPoint(x - 62 * 2, y + 62 * 2), QPoint(x +62, y-62), QPoint(x + 62 * 2, y- 62 * 2)]
        condition[19] = [QPoint(x - 62, y+ 62), QPoint(x + 62, y- 62), QPoint(x + 62 * 2, y- 62 * 2), QPoint(x + 62 * 3, y- 62 * 3)]
        condition[20] = [QPoint(x + 62*4, y- 62*4), QPoint(x + 62 * 3, y- 62 * 3), QPoint(x + 62 * 2, y- 62 * 2), QPoint(x + 62 * 1, y - 62 * 1)]
        for k,i in condition.items():
            count = 0
            if self.turn == 'black':
                for piece in i:
                    if piece in self.black_piece_pos:
                        count += 1
                if count == 4:
                    self.win = 'black'
            elif self.turn == 'white':
                for piece in i:
                    if piece in self.white_piece_pos:
                        count += 1
                if count == 4:
                    self.win = 'white'
        if not self.win:
            self.change_turn()
        elif self.win == 'black':
            self.ending_signal.emit('black win!')
        elif self.win == 'white':
            self.ending_signal.emit('white win!')


    def show_ending_message(self,ms):
        msg = QMessageBox(QMessageBox.Information,'Game over!',ms,QMessageBox.NoButton,self)
        msg.addButton('&Replay',QMessageBox.AcceptRole)
        msg.addButton('&Exit',QMessageBox.RejectRole)
        if msg.exec() == QMessageBox.AcceptRole:
            self.init_game()
        else:
            QCoreApplication.quit()

    @staticmethod
    def cal_pos(pos):
        a,b = pos.x(),pos.y()
        if a % 62-32 <31:
            a = a // 62 *62+32
        else:
            a = (a //62+1)*62+32
        if b % 62-32 <31:
            b = b// 62 *62+32
        else:
            b = (b //62+1)*62+32

        return QPoint(a,b)




class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()

        l = QVBoxLayout()
        l.addWidget(self.board)
        w = QWidget()
        w.setLayout(l)
        w.setFixedHeight(1000)
        w.setFixedWidth(1000)
        self.setCentralWidget(w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())