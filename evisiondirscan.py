import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QTextBrowser, QGridLayout, QTextEdit, QDesktopWidget

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt

import os
import re
from pprint import pprint

class MyApp(QWidget):

def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
		self.setWindowTitle('EVI$ION SCANNER PROJECT')
        self.setWindowIcon(QIcon('evision-logo.png'))
        self.setGeometry(500,300,500,500)

#pixmap
		pixmap = QPixmap('evision-slogan.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)

        self.move(300, 300)

#textbrowser
        self.le = QLineEdit()
        self.le.setPlaceholderText('Please enter root directory to scan') 
        vbox.addWidget(self.le, 0)
        self.le.returnPressed.connect(self.check) #enter key use
        self.btn = QPushButton('Input Check')
        self.btn.clicked.connect(self.check)
        vbox.addWidget(self.btn, 0)

        self.setLayout(vbox)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def check(self):
        QMessageBox.about(self, "Check", "Success")
