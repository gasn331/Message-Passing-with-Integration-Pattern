# coding=utf-8
import sys
import os
import cv2  # Somente para testes

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import numpy as np
import serial
import glob
import interface.icons_rc

class MainServer(QMainWindow):
    """ Interface do programa. Instancia Hades e chama seus métodos ao receber disparos de eventos. """

    def __init__(self):
        super(MainServer, self).__init__()

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'interface/mainwindow.ui')
        loadUi(filename, self)

        print("MainServer summoned")


def main():
    app = QApplication(sys.argv)
    window = MainServer()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
