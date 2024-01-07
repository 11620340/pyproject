from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import os
import threading


class main_window:
    def __init__(self):
        self.ui = QUiLo4ader().load('ui/stats.ui')
        self.ui.pushButton.clicked.connect(self.dayin)
        self.ui.pushButton_2.clicked.connect(self.B)

    def dayin(self):
        self.ui.textBrowser.append("123")
        os.startfile('cpuz_x64.exe')

    def B(self):
        os.startfile('bi.url')
        self.ui.textBrowser.append("bi")




app = QApplication([])
stats = main_window()
stats.ui.show()
app.exec_()