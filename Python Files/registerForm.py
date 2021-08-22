from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as conn
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 599)

        #to hide the form border (Close Button, Minimize Button etc)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #to hide the form backgroud
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #------------------------------------------------------------
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 611, 500))
        self.widget.setStyleSheet("QPushButton#pushButton_register{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_register:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_register:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 70, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/Compressed/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(300, 70, 301, 371))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 311, 411))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_heading = QtWidgets.QLabel(self.widget)
        self.label_heading.setGeometry(QtCore.QRect(50, 95, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setStyleSheet("color:rgba(255,255,255, 210);")
        self.label_heading.setObjectName("label_heading")
        self.label_sub_heading = QtWidgets.QLabel(self.widget)
        self.label_sub_heading.setGeometry(QtCore.QRect(50, 145, 200, 51))
        self.label_sub_heading.setStyleSheet("color:rgba(255,255,255,210);\n"
"")
        self.label_sub_heading.setObjectName("label_sub_heading")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Mountain")
        font.setPointSize(150)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgba(255, 107, 107, 255);")
        self.label_9.setObjectName("label_9")
        self.label_register = QtWidgets.QLabel(self.widget)
        self.label_register.setGeometry(QtCore.QRect(370, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_register.setFont(font)
        self.label_register.setObjectName("label_register")
        self.pushButton_register = QtWidgets.QPushButton(self.widget)
        self.pushButton_register.setGeometry(QtCore.QRect(370, 370, 185, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_register.setFont(font)
        self.pushButton_register.setStyleSheet("")
        self.pushButton_register.setObjectName("pushButton_register")
        
        # to call register function
        self.pushButton_register.clicked.connect(self.register)
        
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setGeometry(QtCore.QRect(370, 150, 185, 40))
        self.lineEdit_name.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:0px;")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username.setGeometry(QtCore.QRect(370, 200, 185, 40))
        self.lineEdit_username.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:0px;")
        self.lineEdit_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setGeometry(QtCore.QRect(370, 250, 185, 40))
        self.lineEdit_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:0px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setGeometry(QtCore.QRect(370, 300, 185, 40))
        self.lineEdit_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:0px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #to add shadow
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        #self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_register.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        #-----------------------------------------------------------------------------------------------------------

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def register(self):
            try:
                    _name = self.lineEdit_name.text()
                    _username = self.lineEdit_username.text()
                    _email = self.lineEdit_email.text()
                    _password = self.lineEdit_password.text()

                    myDB = conn.connect(
                            host = "localhost",
                            user = "root",
                            password = "",
                            database = "pyqt5"
                    )

                    myCursor = myDB.cursor()
                    selectQuery = "SELECT email, password from users WHERE username LIKE '" + _username + "' OR email LIKE '" + _email + "'";
                    myCursor.execute(selectQuery)
                    result = myCursor.fetchone()

                    if result == None:                            
                            insertQuery = "INSERT INTO USERS (name, username, email, password) VALUES ('"+ _name  +"','"+  _username + "','" + _email + "','" + _password + "')"
                            myCursor.execute(insertQuery)
                            myDB.commit()
                            
                            print("Registration Successful.")
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Registration Successful")
                            msg.setInformativeText('User has been registered. Thanks')
                            msg.setWindowTitle("Successful")
                            msg.exec_()
                    else:
                            print("Email/Username existed.")
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Registration Failed")
                            msg.setInformativeText('Username/Email already existed.')
                            msg.setWindowTitle("Failed")
                            msg.exec_()

            except conn.Error as err:
                    print("Error")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Connection Failed")
                    msg.setInformativeText('Database not exist.')
                    msg.setWindowTitle("Error")
                    msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "MohsinZiaButt"))
        self.label_sub_heading.setText(_translate("MainWindow", "Hi,\n"
"Welcome to my Github.\n"
"https://www.mohsinziabutt.com/"))
        self.label_9.setText(_translate("MainWindow", "/"))
        self.label_register.setText(_translate("MainWindow", "Register"))
        self.pushButton_register.setText(_translate("MainWindow", "Register"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Password"))

import sys

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow()
        Form = QtWidgets.QMainWindow()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
