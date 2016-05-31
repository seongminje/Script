import sys
import GUI
import urllib
import define

from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication, QMessageBox, QPushButton, QMainWindow
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit

class MainWindow(QDialog, GUI.Ui_Dialog):
    list = define.Parsing(define.API("openapi.jejutour.go.kr:8080", "/openapi/service/TourCourseService/getTourCosList?ServiceKey=mcVXPBIgozkl0CsuSqONRV9GmUuPgjVX5CxQ%2Fey6BPQ51vtKXCZtpy%2FeEmRtDjkUgP3CM0DjJvHQBavYImW18w%3D%3D&numOfRows=999&pageSize=999&pageNo=1&startPage=1")) 
    def closeEvent(self, event):
        ans = QMessageBox.question(self, '제주도 여행기', "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        for i in range(30) :
            self.listWidget_1.addItem(self.list[i])
        self.pushButton_3.clicked.connect(self.searchList)
        
    def searchList(self, event):
        if self.textEdit.toPlainText()=="":
            QMessageBox.information(self, '경고', "검색어를 입력해 주세요.", QMessageBox.Yes)
        else :
            find = False    
            keyword = self.textEdit.toPlainText()
            if self.pushButton_3.clicked:
                self.listWidget_2.clear()
                for i in range(30):
                    if(self.list[i].find(keyword)>=0):
                        self.listWidget_2.addItem(self.list[i])
                        find = True
                if find == False:
                    QMessageBox.information(self, '경고', "검색 결과가 없습니다.", QMessageBox.Yes)
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())