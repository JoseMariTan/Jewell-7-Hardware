# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 750)
        MainWindow.setStyleSheet("background-color: #f1f1f3;")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 50))
        self.label.setMaximumSize(QtCore.QSize(500, 290))
        self.label.setStyleSheet("image: url(:/images/received_836614531712349.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setMinimumSize(QtCore.QSize(200, 55))
        self.username_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("\n"
"QLineEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding: 4px;\n"
"  border: none;\n"
"border-radius:12px;\n"
"  position: relative;\n"
"  z-index: 0; /* We force a stacking context */\n"
"}\n"
"")
        self.username_input.setText("")
        self.username_input.setFrame(True)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setMinimumSize(QtCore.QSize(200, 55))
        self.password_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("\n"
"QLineEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding:4px;\n"
"  border: none;\n"
"border-radius:10px;\n"
"\n"
"  position: relative;\n"
"  z-index: 0; /* We force a stacking context */\n"
"}\n"
"\n"
"QLineEdit::before {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  z-index: -2;\n"
"  inset: -5px;\n"
"  transform: translate(10px, 8px);\n"
"  background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(198,198,200), stop: 1 rgb(204,204,206));\n"
"  filter: blur(10px);\n"
"}\n"
"\n"
"QLineEdit::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  z-index: -1;\n"
"  inset: 0;\n"
"  background: inherit;\n"
"  border: inherit;\n"
"  box-shadow: inherit;\n"
"}")
        self.password_input.setText("")
        self.password_input.setFrame(True)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        self.show_password_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.show_password_checkbox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.show_password_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.verticalLayout.addWidget(self.show_password_checkbox)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setMinimumSize(QtCore.QSize(200, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {\n"
"  background-color: #10cc94;\n"
"border-radius:12px;\n"
"\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #0a9c73;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.forgotButton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotButton.setMinimumSize(QtCore.QSize(100, 50))
        self.forgotButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.forgotButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.forgotButton.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"\n"
"text-decoration: underline;\n"
"color:#4169E1;\n"
"\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #FFF;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}")
        self.forgotButton.setCheckable(False)
        self.forgotButton.setFlat(False)
        self.forgotButton.setObjectName("forgotButton")
        self.verticalLayout.addWidget(self.forgotButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.show_password_checkbox.setText(_translate("MainWindow", "ShowPassword"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.forgotButton.setText(_translate("MainWindow", "Forgot Password?"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
