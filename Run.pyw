import subprocess
import sys
try:
    import PyQt5
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])
try:
    from dateutil.relativedelta import relativedelta
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dateutil"])
try:
    import mysql.connector
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector-python"])

from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from PyQt5 import QtGui,QtCore
#from PyQt5.uic import loadUi

from Main import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont("RobotoMono.ttf")
    app_icon = QtGui.QIcon()
    app_icon.addFile('Icons/store (5).png', QtCore.QSize(16,16))
    app_icon.addFile('Icons/sstore (4).png', QtCore.QSize(24,24))
    app_icon.addFile('Icons/sstore (3).png', QtCore.QSize(32,32))
    app_icon.addFile('Icons/sstore (2).png', QtCore.QSize(48,48))
    app_icon.addFile('Icons/sstore (1).png', QtCore.QSize(256,256))
    app_icon.addFile('Icons/sstore.png', QtCore.QSize(512,512))
    app.setWindowIcon(app_icon)
    win = Window()
    win.show()
    sys.exit(app.exec())
