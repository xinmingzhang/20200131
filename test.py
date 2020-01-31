#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from PyQt5.QtCore import QEasingCurve, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from Lib.UiImageSlider import Ui_Form  # @UnresolvedImport


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ImageSliderWidget(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(ImageSliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # 初始化动画曲线类型
        curve_types = [(n, c) for n, c in QEasingCurve.__dict__.items()
                       if isinstance(c, QEasingCurve.Type)]
        curve_types.sort(key=lambda ct: ct[1])
        curve_types = [c[0] for c in curve_types]
        self.comboBoxEasing.addItems(curve_types)

        # 绑定信号槽
        self.spinBoxSpeed.valueChanged.connect(self.stackedWidget.setSpeed)
        self.comboBoxEasing.currentTextChanged.connect(self.setEasing)
        self.radioButtonHor.toggled.connect(self.setOrientation)
        self.radioButtonVer.toggled.connect(self.setOrientation)
        self.pushButtonPrev.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButtonNext.clicked.connect(self.stackedWidget.slideInNext)
        self.pushButtonStart.clicked.connect(self.autoStart)
        self.pushButtonStop.clicked.connect(self.autoStop)

        # 添加图片页面
        for name in os.listdir('Data/Images'):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            label.setPixmap(QPixmap('Data/Images/' + name))
            self.stackedWidget.addWidget(label)

    def autoStart(self):
        self.pushButtonNext.setEnabled(False)
        self.pushButtonPrev.setEnabled(False)
        self.stackedWidget.autoStart()

    def autoStop(self):
        self.pushButtonNext.setEnabled(True)
        self.pushButtonPrev.setEnabled(True)
        self.stackedWidget.autoStop()

    def setEasing(self, name):
        self.stackedWidget.setEasing(getattr(QEasingCurve, name))

    def setOrientation(self, checked):
        hor = self.sender() == self.radioButtonHor
        if checked:
            self.stackedWidget.setOrientation(
                Qt.Horizontal if hor else Qt.Vertical)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ImageSliderWidget()
    w.show()
    sys.exit(app.exec_())