# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 622)
        self.search = QtWidgets.QTabWidget(Dialog)
        self.search.setGeometry(QtCore.QRect(20, 20, 381, 581))
        self.search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search.setObjectName("search")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_1 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_1.setGeometry(QtCore.QRect(0, 11, 371, 541))
        self.listWidget_1.setObjectName("listWidget_1")
        self.search.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 10, 81, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 50, 371, 501))
        self.listWidget_2.setObjectName("listWidget_2")
        self.search.addTab(self.widget, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_3.setGeometry(QtCore.QRect(5, 51, 361, 501))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 10, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.search.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_6)
        self.graphicsView.setGeometry(QtCore.QRect(0, 10, 371, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.search.addTab(self.tab_6, "")

        self.retranslateUi(Dialog)
        self.search.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search.setTabText(self.search.indexOf(self.tab_2), _translate("Dialog", "관광지 목록"))
        self.widget.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "검색하기"))
        self.search.setTabText(self.search.indexOf(self.widget), _translate("Dialog", "검색"))
        self.pushButton_2.setText(_translate("Dialog", "새로고침"))
        self.search.setTabText(self.search.indexOf(self.tab_5), _translate("Dialog", "랭킹"))
        self.search.setTabText(self.search.indexOf(self.tab_6), _translate("Dialog", "지도"))
