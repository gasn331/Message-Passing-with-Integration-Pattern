# coding=utf-8
import sys
import os
import cv2  # Somente para testes

from PyQt5 import QtCore, QtGui, QtQuick
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import numpy as np
import serial
import glob
import interface.icons_rc

class MainCliente(QMainWindow):
    """ Interface do programa. Instancia Hades e chama seus métodos ao receber disparos de eventos. """

    def __init__(self):
        super(MainCliente, self).__init__()

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'interface/mainwindowClient.ui')
        loadUi(filename, self)

        self.stringText = ""

        #Login
        self.pushButtonLogin.clicked.connect(self.pushButtonLoginClicked)

        #Program
        self.pushButtonSend.clicked.connect(self.pushButtonSendClicked)

    def pushButtonLoginClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def pushButtonSendClicked(self):
        self.stringText = self.stringText + self.lineEditSend.text() + "\n"
        self.labelMessages.setText(self.stringText)
        self.lineEditSend.clear()   

def main():
    app = QApplication(sys.argv)
    window = MainCliente()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
