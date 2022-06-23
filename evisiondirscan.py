import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QTextBrowser, QGridLayout, QTextEdit, QDesktopWidget

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt

import os
import subprocess
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
        #경로 설정할 수 있는 방법이 있을까봐 일단 주석으로 넣어둠
        #rootdir = self.le.text() #사용자 입력 경로 저장
        #os.chdir(rootdir) #사용자가 입력한 경로로 path 이동
        #path=os.getcwd()
        #print(path)
        
        self.tb.append("scanning ... ")
        # traverse the software list
        #지금은 편의상 putty넣어둠 나중에 파일명 바꾸면 됨!
        # result=os.popen('wmic product where name="PuTTY release 0.75 (64-bit)" get name, version').read()
        program = self.le.text()
        get_ver = 'wmic product where name="' + program + '" get version'
        get_name_ver = 'wmic product where name="' + program + '" get name, version'
        ver_result=os.popen(get_ver).read()
        print(type(ver_result))
        total_result = os.popen(get_name_ver).read()
        print(total_result)
        print(ver_result)

        # resultV = os.popen('wmic product where name="Cyberduck" get version').read()
        self.tb.append("Scan Completed\n ----------------------------")
        self.tb.append(total_result)
        if program == 'Cyberduck':
            result = ver_result[:11]
            if result == '8.3.3.37544':
                self.tb.append("----------------------------\n You are using latest version of " + program)
            else:
                self.tb.append("-----------------------------\n" + program + " needs to be updated")
        elif program == 'Node.js':
            result = ver_result[-13:-6]
           # print('.'+result + '.')
            if result == '14.17.6':
                self.tb.append("----------------------------\n You are using latest version of " + program)
            else:
                self.tb.append("-----------------------------\n" + program + " needs to be updated")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
