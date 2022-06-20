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
        self.setGeometry(500,300,500,300)

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
        self.btn = QPushButton('Scanning start')
        self.btn.clicked.connect(self.dirscan)
        vbox.addWidget(self.btn, 0)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        vbox.addWidget(self.tb, 300)

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

    def dirscan(self):
        rootdir = self.le.text() #사용자 입력 경로 저장
        os.chdir(rootdir) #사용자가 입력한 경로로 path 이동
        path=os.getcwd()

        if path == "":
            QMessageBox.about(self,"Notice","please enter the root dir")

        else:
            print(path)
            self.tb.append("scanning ... ")
            try:
                filenames = os.listdir(path)
                for filename in filenames:
                    full_filename = os.path.join(dirname, filename)
                    print(full_filename)
            except:
                self.tb.append("         "+"         "+"there's no directory")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())