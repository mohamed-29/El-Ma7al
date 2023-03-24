# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Return.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mobile_shop"
)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 1261, 176))
        self.listWidget.setObjectName("listWidget")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 400, 1261, 199))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Pro_Id = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Pro_Id.setFont(font)
        self.lineEdit_Pro_Id.setObjectName("lineEdit_Pro_Id")
        self.gridLayout.addWidget(self.lineEdit_Pro_Id, 2, 3, 1, 1)
        self.lineEdit_CNumber = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_CNumber.setFont(font)
        self.lineEdit_CNumber.setObjectName("lineEdit_CNumber")
        self.gridLayout.addWidget(self.lineEdit_CNumber, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 6, 1, 1)
        self.lineEdit_Rec_Id = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Rec_Id.setFont(font)
        self.lineEdit_Rec_Id.setText("")
        self.lineEdit_Rec_Id.setObjectName("lineEdit_Rec_Id")
        self.gridLayout.addWidget(self.lineEdit_Rec_Id, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.lineEdit_CName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_CName.setFont(font)
        self.lineEdit_CName.setText("")
        self.lineEdit_CName.setObjectName("lineEdit_CName")
        self.gridLayout.addWidget(self.lineEdit_CName, 4, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 2, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 6, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 4, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineEdit_Reason = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Reason.setFont(font)
        self.lineEdit_Reason.setText("")
        self.lineEdit_Reason.setMaxLength(510)
        self.lineEdit_Reason.setObjectName("lineEdit_Reason")
        self.gridLayout.addWidget(self.lineEdit_Reason, 6, 0, 1, 7)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 630, 1201, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Search = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.pushButton_Down = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Down.setFont(font)
        self.pushButton_Down.setObjectName("pushButton_Down")
        self.horizontalLayout.addWidget(self.pushButton_Down)
        self.pushButton_Up = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Up.setFont(font)
        self.pushButton_Up.setObjectName("pushButton_Up")
        self.horizontalLayout.addWidget(self.pushButton_Up)
        self.pushButton_Edit = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Edit.setFont(font)
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.horizontalLayout.addWidget(self.pushButton_Edit)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 225, 1261, 171))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(10, 200, 61, 21))
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.label.setObjectName("label")
        
        self.listWidget.itemClicked.connect(self.Select)
        self.listWidget.itemDoubleClicked.connect(self.PRecet)
        self.listWidget_2.itemClicked.connect(self.Select)
        self.pushButton_Search.clicked.connect(self.Search)
        self.pushButton_Down.clicked.connect(self.MoveDown)
        self.pushButton_Up.clicked.connect(self.MoveUp)
        self.pushButton_Edit.clicked.connect(self.Edit)
        
        yearBefore = datetime.now() - relativedelta(months=1)
        self.dateTimeEdit.setDateTime(yearBefore)
        dayBefore = datetime.now()
        self.dateTimeEdit_2.setDateTime(dayBefore)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add or Edit Return Data"))
        self.lineEdit_Pro_Id.setPlaceholderText(_translate("Dialog", "Product Id"))
        self.lineEdit_CNumber.setPlaceholderText(_translate("Dialog", "01090614615"))
        self.label_2.setText(_translate("Dialog", "Receipt Id"))
        self.label_11.setText(_translate("Dialog", "Date and Time"))
        self.lineEdit_Rec_Id.setPlaceholderText(_translate("Dialog", "Receipt Id"))
        self.label_3.setText(_translate("Dialog", "Product Id"))
        self.label_7.setText(_translate("Dialog", "Customer Number"))
        self.lineEdit_CName.setPlaceholderText(_translate("Dialog", "Mohamed Hassan"))
        self.label_13.setText(_translate("Dialog", "to"))
        self.label_5.setText(_translate("Dialog", "Customer Name"))
        self.label_4.setText(_translate("Dialog", "Reason For Return"))
        self.lineEdit_Reason.setPlaceholderText(_translate("Dialog", "اصل صاحبى قالى انه بيبوظ بسرعه"))
        self.pushButton_Search.setText(_translate("Dialog", "Search"))
        self.pushButton_Down.setText(_translate("Dialog", "Move Down"))
        self.pushButton_Up.setText(_translate("Dialog", "Move Up"))
        self.pushButton_Edit.setText(_translate("Dialog", "Edit"))
        self.label_14.setText(_translate("Dialog", "Returns"))
        self.label.setText(_translate("Dialog", "Receipt"))
    
    def Search(self):
        
        self.listWidget.clear()
        
        elements = ["Receipt Id"+" "*(20-len("Receipt Id")),"Product Id"+" "*(20-len("Product Id")),"Customer Name"+" "*(20-len("Customer Name")),"Customer Number"+" "*(20-len("Customer Number")),"Price on you"+" "*(20-len("Price on you")),"Profit"+" "*(20-len("Profit")),"Number"+" "*(10-len("Number")),"Date and Time"+" "*(20-len("Date and Time"))]
        y = " | ".join(elements)
        listWidgetItem = QtWidgets.QListWidgetItem(y)
        listWidgetItem.setFlags(QtCore.Qt.NoItemFlags)
        self.listWidget.addItem(listWidgetItem)
        self.listWidget.setFont(QtGui.QFont('Roboto Mono', 10))
        
        recId = self.lineEdit_Rec_Id.text()
        proId = self.lineEdit_Pro_Id.text()
        cName = self.lineEdit_CName.text()
        cNum = self.lineEdit_CNumber.text()
        time = str(self.dateTimeEdit.dateTime())[23:][:-1]
        timeData = time.split(", ")
        dateFrom = timeData[0] + "-" + "{:02d}".format(int(timeData[1])) + "-" + "{:02d}".format(int(timeData[2]))  + " " + "{:02d}".format(int(timeData[3])) + ":" + "{:02d}".format(int(timeData[4]))
        time2 = str(self.dateTimeEdit_2.dateTime())[23:][:-1]
        timeData2 = time2.split(", ")
        dateTo = timeData2[0] + "-" + "{:02d}".format(int(timeData2[1])) + "-" + "{:02d}".format(int(timeData2[2])) + " " + "{:02d}".format(int(timeData2[3])) + ":" + "{:02d}".format(int(timeData2[4])+1)
        
        
        if not recId:
           recId = "%"
        if not proId:
           proId = "%"
        if not cName:
           cName = "%"
        if not cNum:
           cNum = "%"
        
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM receipt WHERE rec_id LIKE '%{}%' AND pro_id LIKE '%{}%' AND cos_name LIKE '%{}%' AND cos_num LIKE '%{}%' AND release_date BETWEEN '{}' AND '{}'".format(recId,proId,cName,cNum,dateFrom,dateTo)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.reconnect()
        
        
        for element in myresult:
            x = 0
            listOfColumns=[]
            for eachElement in element:
                x +=1
                eachElement = str(eachElement).title()
                if x == 7:
                    eachElement = eachElement + (" " * (10-len(eachElement)))
                    listOfColumns.append((str(eachElement)))
                    continue
                eachElement = eachElement + (" " * (20-len(eachElement)))
                listOfColumns.append((str(eachElement)))
            Result = " | ".join(listOfColumns)
            print(Result)
            listWidgetItem = QtWidgets.QListWidgetItem(Result)
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setFont(QtGui.QFont('Roboto Mono', 10))
        
        
        self.listWidget_2.clear()
        
        elements = ["Receipt Id"+" "*(20-len("Receipt Id")),"Product Id"+" "*(20-len("Product Id")),"Customer Name"+" "*(20-len("Customer Name")),"Customer Number"+" "*(20-len("Customer Number")),"Price on you"+" "*(20-len("Price on you")),"Profit"+" "*(20-len("Profit")),"Number"+" "*(10-len("Number")),"Reason Why ?"+" "*(20-len("Reason Why ?")),"Date and Time"+" "*(20-len("Date and Time"))]
        y = " | ".join(elements)
        listWidgetItem = QtWidgets.QListWidgetItem(y)
        listWidgetItem.setFlags(QtCore.Qt.NoItemFlags)
        self.listWidget_2.addItem(listWidgetItem)
        self.listWidget_2.setFont(QtGui.QFont('Roboto Mono', 10))
        
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM returned WHERE rec_id LIKE '%{}%' AND pro_id LIKE '%{}%' AND cos_name LIKE '%{}%' AND cos_num LIKE '%{}%' AND release_date BETWEEN '{}' AND '{}'".format(recId,proId,cName,cNum,dateFrom,dateTo)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.reconnect()
        
        
        for element in myresult:
            x = 0
            listOfColumns=[]
            for eachElement in element:
                x +=1
                eachElement = str(eachElement).title()
                if x == 7:
                    eachElement = eachElement + (" " * (10-len(eachElement)))
                    listOfColumns.append((str(eachElement)))
                    continue
                eachElement = eachElement + (" " * (20-len(eachElement)))
                listOfColumns.append((str(eachElement)))
            Result = " | ".join(listOfColumns)
            print(Result)
            listWidgetItem = QtWidgets.QListWidgetItem(Result)
            self.listWidget_2.addItem(listWidgetItem)
            self.listWidget_2.setFont(QtGui.QFont('Roboto Mono', 10))
            
        
    def Select(self,item,lis=1):
        if not item.text()[:3] == "Rec":            
            
            self.lineEdit_Reason.clear()
           
            translator = self.listWidget_2.item(0).text()
            translatorComponant = translator.split(" | ")
            
            itemSelected = item.text()
            itemSelectedComponant = itemSelected.split(" | ")
            
            dec = {}
            j=0
            for i in translatorComponant:
                i = i.strip()
                try:
                    item = itemSelectedComponant[j]
                except:
                    continue
                dec[i]=item
                j +=1
            
            self.lineEdit_Rec_Id.setText(str(dec["Receipt Id"]).strip())
            self.lineEdit_Pro_Id.setText(str(dec["Product Id"]).strip())
            self.lineEdit_CName.setText(str(dec["Customer Name"]).strip())
            self.lineEdit_CNumber.setText(str(dec["Customer Number"]).strip())
            if len(itemSelectedComponant) == 9:
                self.lineEdit_Reason.setText(str(dec["Reason Why ?"]).strip())
                self.listWidget.setCurrentRow(0)
            else:
                self.listWidget_2.setCurrentRow(0)
    def MoveDown(self):
        try:
            translator = self.listWidget.item(0).text()
        except:
            return 0
        translatorComponant = translator.split(" | ")
        
        isCan = self.listWidget.currentRow()
        
        if isCan < 0:
            return 0
        
        item = self.listWidget.currentItem()
        itemSelected = item.text()
        itemSelectedComponant = itemSelected.split(" | ")
        
        dec = {}
        j=0
        for i in translatorComponant:
            i = i.strip()
            item = itemSelectedComponant[j]
            dec[i]=item
            j +=1
        time2 = str(self.dateTimeEdit_2.dateTime())[23:][:-1]
        timeData2 = time2.split(", ")
        dateTo = timeData2[0] + "-" + "{:02d}".format(int(timeData2[1])) + "-" + "{:02d}".format(int(timeData2[2])) + " " + "{:02d}".format(int(timeData2[3])) + ":" + "{:02d}".format(int(timeData2[4]))
        
        recId = str(dec["Receipt Id"]).strip()
        proId = str(dec["Product Id"]).strip()
        cName = str(dec["Customer Name"]).strip()
        cNum = str(dec["Customer Number"]).strip()
        pIn = str(dec["Price on you"]).strip()
        profit = str(dec["Profit"]).strip()
        num = str(dec["Number"]).strip()
        
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "SELECT num FROM ids WHERE id = '{}'".format(proId)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.reconnect()
        try:
            proNum = myresult[0][0]
        except:
            return 0
        
        reason = self.lineEdit_Reason.text()
        
        try:
            num = int(num)
        except:
            return 0
        print(num)
        if num-1 > 0 :
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "UPDATE receipt SET num = {} WHERE rec_id = {} AND pro_id = '{}'".format(num-1, int(recId), proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record(s) UPDATE")
            mydb.reconnect()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "SELECT num FROM returned WHERE rec_id = {} AND pro_id = '{}' ".format(int(recId),proId)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            mydb.reconnect()
            
            
            if not myresult:
                
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "INSERT INTO returned (rec_id, pro_id, cos_name, cos_num, price_in, profit, num, note, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (int(recId), proId, cName, cNum, pIn, profit, 1, reason, dateTo)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) INSERT")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
            else:

                try:
                    num1 = int(myresult[0][0])
                except:
                    return 0
                print(num1)
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "UPDATE returned SET num = {} WHERE rec_id = '{}' AND pro_id = '{}'".format(num1+1, recId, proId)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) UPDATE")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
        else:
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "DELETE FROM receipt WHERE rec_id = '{}' AND pro_id = '{}'".format(recId, proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record(s) DELETE")
            mydb.reconnect()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "SELECT num FROM returned WHERE rec_id LIKE '%{}%' AND pro_id LIKE '%{}%' ".format(recId,proId)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            mydb.reconnect()
            
            
            if not myresult:
                
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "INSERT INTO returned (rec_id, pro_id, cos_name, cos_num, price_in, profit, num, note, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (recId, proId, cName, cNum, pIn, profit, 1, reason, dateTo)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) INSERT")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
            else:

                try:
                    num1 = int(myresult[0][0])
                except:
                    return 0
                print(num1)
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "UPDATE returned SET num = {} WHERE rec_id = '{}' AND pro_id = '{}'".format(num1+1, recId, proId)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) UPDATE")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
        
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "UPDATE ids SET num = {} WHERE id = '{}'".format(proNum+1, proId)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) UPDATE")
        mydb.reconnect()
            
    def MoveUp(self):
        try:
            translator = self.listWidget_2.item(0).text()
        except:
            return 0
        translatorComponant = translator.split(" | ")
        isCan = self.listWidget_2.currentRow()
        
        if isCan < 0:
            return 0
        
        item = self.listWidget_2.currentItem()
        itemSelected = item.text()
        itemSelectedComponant = itemSelected.split(" | ")
        
        dec = {}
        j=0
        for i in translatorComponant:
            i = i.strip()
            item = itemSelectedComponant[j]
            dec[i]=item
            j +=1
        time2 = str(self.dateTimeEdit_2.dateTime())[23:][:-1]
        timeData2 = time2.split(", ")
        dateTo = timeData2[0] + "-" + "{:02d}".format(int(timeData2[1])) + "-" + "{:02d}".format(int(timeData2[2])) + " " + "{:02d}".format(int(timeData2[3])) + ":" + "{:02d}".format(int(timeData2[4]))
        
        
        recId = str(dec["Receipt Id"]).strip()
        proId = str(dec["Product Id"]).strip()
        cName = str(dec["Customer Name"]).strip()
        cNum = str(dec["Customer Number"]).strip()
        pIn = str(dec["Price on you"]).strip()
        profit = str(dec["Profit"]).strip()
        num = str(dec["Number"]).strip()
        
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "SELECT num FROM ids WHERE id = '{}'".format(proId)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.reconnect()
        try:
            proNum = myresult[0][0]
        except:
            return 0
        try:
            num = int(num)
        except:
            return 0
        print(num)
        
        if num-1 > 0 :
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "UPDATE returned SET num = {} WHERE rec_id = '{}' AND pro_id = '{}'".format(num-1, recId, proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record(s) UPDATE")
            mydb.reconnect()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "SELECT num FROM receipt WHERE rec_id LIKE '%{}%' AND pro_id LIKE '%{}%' ".format(recId,proId)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            mydb.reconnect()
            
            
            if not myresult:
                
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "INSERT INTO receipt (rec_id, pro_id, cos_name, cos_num, price_in, profit, num, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (recId, proId, cName, cNum, pIn, profit, 1, dateTo)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) INSERT")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
            else:

                try:
                    num1 = int(myresult[0][0])
                except:
                    return 0
                print(num1)
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "UPDATE receipt SET num = {} WHERE rec_id = '{}' AND pro_id = '{}'".format(num1+1, recId, proId)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) UPDATE")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
        else:
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "DELETE FROM returned WHERE rec_id = '{}' AND pro_id = '{}'".format(recId, proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record(s) DELETE")
            mydb.reconnect()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "SELECT num FROM receipt WHERE rec_id LIKE '%{}%' AND pro_id LIKE '%{}%' ".format(recId,proId)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            mydb.reconnect()
            
            
            if not myresult:
                
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "INSERT INTO receipt (rec_id, pro_id, cos_name, cos_num, price_in, profit, num, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (recId, proId, cName, cNum, pIn, profit, 1, dateTo)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) INSERT")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
            
            else:

                try:
                    num1 = int(myresult[0][0])
                except:
                    return 0
                print(num1)
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "UPDATE receipt SET num = {} WHERE rec_id = '{}' AND pro_id = '{}'".format(num1+1, recId, proId)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) UPDATE")
                mydb.reconnect()
                self.lineEdit_CName.clear()
                self.lineEdit_CNumber.clear()
                self.lineEdit_Reason.clear()
                self.Search()
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "UPDATE ids SET num = {} WHERE id = '{}'".format(proNum-1, proId)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) UPDATE")
        mydb.reconnect()
    
    def Edit(self):
        
        cName = self.lineEdit_CName.text()
        cNum = self.lineEdit_CNumber.text()
        reason = self.lineEdit_Reason.text()
        
        try:
            curent1 = self.listWidget.currentRow()
        except:
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Can't make the Edit", "What You Want To Edit ?").exec()
            return 0
        try:
            curent2 = self.listWidget_2.currentRow()
        except:
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Can't make the Edit", "What You Want To Edit ?").exec()
            return 0    
        print(curent1)
        if curent1 >= 0:
            
            translator = self.listWidget.item(0).text()
            translatorComponant = translator.split(" | ")
            
            item = self.listWidget.currentItem()
            itemSelected = item.text()
            itemSelectedComponant = itemSelected.split(" | ")
            
            dec = {}
            j=0
            for i in translatorComponant:
                i = i.strip()
                item = itemSelectedComponant[j]
                dec[i]=item
                j +=1
            
            recId = str(dec["Receipt Id"]).strip()
            proId = str(dec["Product Id"]).strip()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "UPDATE receipt SET cos_name = '{}' , cos_num = '{}' WHERE rec_id = '{}' AND pro_id = '{}'".format(cName, cNum, recId, proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "receipt(s) UPDATE")
            mydb.reconnect()
            self.lineEdit_CName.clear()
            self.lineEdit_CNumber.clear()
            self.Search()
        elif curent2 >= 0:
            
            translator = self.listWidget.item(0).text()
            translatorComponant = translator.split(" | ")
            
            item = self.listWidget_2.currentItem()
            itemSelected = item.text()
            itemSelectedComponant = itemSelected.split(" | ")
            
            dec = {}
            j=0
            for i in translatorComponant:
                i = i.strip()
                item = itemSelectedComponant[j]
                dec[i]=item
                j +=1
            
            
            recId = str(dec["Receipt Id"]).strip()
            proId = str(dec["Product Id"]).strip()
            
            mydb.reconnect()
            mycursor = mydb.cursor()
            sql = "UPDATE returned SET cos_name = '{}' , cos_num = '{}' , note = '{}' WHERE rec_id = '{}' AND pro_id = '{}'".format(cName, cNum, reason, recId, proId)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "returned(s) UPDATE")
            mydb.reconnect()
            self.lineEdit_CName.clear()
            self.lineEdit_CNumber.clear()
            self.lineEdit_Reason.clear()
            self.Search()
        
    def PRecet(self,item):
        RId = item.text().split(" | ")[0].strip()
        print(RId)
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM receipt WHERE rec_id = '{}'".format(RId)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.reconnect()
        
        with open('Receipt.txt', 'w') as f:
            Cname = myresult[0][2]
            Cnum = myresult[0][3]
            Sdate = myresult[0][7]
            x = f.write("Reprinted receipt \n\n")
            x = f.write("Date and Time : {}".format(Sdate) + "\n")
            x = f.write("Receipt ID : {}".format(RId) + "\n")
            x = f.write("Welcome : {}".format(Cname) + "\n")
            x = f.write("Phone : {}".format(Cnum) + "\n")
            total = 0
            for element in myresult:
                
                Tprice = (element[4] + element[5]) * element[6]
                Sprice = element[4] + element[5]
                proId = element[1]
                Snum = element[6]
                
                total = total + Tprice 
                
                mydb.reconnect()
                mycursor = mydb.cursor()
                sql = "SELECT brand,model,battary,gb,ram,color,is_used FROM mobile_devices WHERE serial_id = '{}'".format(proId)
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                mydb.reconnect()
                
                if not myresult:
                    mydb.reconnect()
                    mycursor = mydb.cursor()
                    sql = "SELECT acc_name,brand,kind,color FROM accessories WHERE acc_id = '{}'".format(proId)
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()
                    mydb.reconnect()
                
                
                for items in myresult:
                   
                    items = list(items)
                    items[0] = items[0] + " " + items[1]
                    items.pop(1)
                    prolist = []
                    if len(items) > 3:
                        items[2] = str(items[2]) + "GB"
                        items[3] = str(items[3]) + "GB"
                        if Snum > 1:
                            if items[5]:
                                prolist.append(proId)
                                prolist.append(items[0])
                                prolist.append(str(items[1]) + "%")
                                prolist.append(str(items[2]))
                                prolist.append(str(items[3]))
                                prolist.append(str(items[4]))
                                prolist.append("Used")
                                prolist.append(str(Sprice))
                                prolist.append("x {}".format(Snum))
                            else:
                                prolist.append(proId)
                                prolist.append(items[0])
                                prolist.append(str(items[2]))
                                prolist.append(str(items[3]))
                                prolist.append(str(items[4]))
                                prolist.append(str(Sprice))
                                prolist.append("x {}".format(Snum))
                        else:
                            if items[5]:
                                prolist.append(proId)
                                prolist.append(items[0])
                                prolist.append(str(items[1]) + "%")
                                prolist.append(str(items[2]))
                                prolist.append(str(items[3]))
                                prolist.append(str(items[4]))
                                prolist.append("Used")
                                prolist.append(str(Sprice))
                            else:
                                prolist.append(proId)
                                prolist.append(items[0])
                                prolist.append(str(items[2]))
                                prolist.append(str(items[3]))
                                prolist.append(str(items[4]))
                                prolist.append(str(Sprice))
                    else:
                        if Snum > 1:
                            prolist.append(proId)
                            prolist.append(items[0])
                            prolist.append(str(items[1]))
                            prolist.append(str(items[2]))
                            prolist.append(str(Sprice))
                            prolist.append("x {}".format(Snum))
                        else:
                            prolist.append(proId)
                            prolist.append(items[0])
                            prolist.append(str(items[1]))
                            prolist.append(str(items[2]))
                            prolist.append(str(Sprice))
                
                x = f.write("\n" + " | ".join(prolist)+"\n")
            x = f.write("\n \nTotal : {}".format(total) + "\n")
            x = f.write("\n \nSee You Sooon")
            os.startfile('Receipt.txt', "print")
        





