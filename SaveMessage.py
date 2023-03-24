# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 240)
        Dialog.setMinimumSize(QtCore.QSize(400, 240))
        Dialog.setMaximumSize(QtCore.QSize(400, 240))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(lambda: self.cancel(Dialog)) # type: ignore
        self.pushButton.clicked.connect(lambda: self.ok(Dialog)) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Phone"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
    
    def ok(self, Dialog):
        text = "Con : " + "ok" + "\n"
        name = self.lineEdit.text()
        text1 = "Name : " + name + "\n"
        phone = self.lineEdit_2.text()
        text2 = "Phone : " + phone
        with open('Message.dat', 'w+') as f:
            f.write(text)
            f.write(text1)
            f.write(text2)
        print("ok")
        Dialog.close()
    
    def cancel(self, Dialog):
        text = "Con : " + "cancel" + "\n"
        name = self.lineEdit.text()
        text1 = "Name : " + name + "\n"
        phone = self.lineEdit_2.text()
        text2 = "Phone : " + phone
        with open('Message.dat', 'w+') as f:
            f.write(text)
            f.write(text1)
            f.write(text2)
        print("cancel")
        Dialog.close()