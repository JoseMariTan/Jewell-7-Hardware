# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 819)
        MainWindow.setStyleSheet("background-color: #FCFEFE;")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(500, 600))
        self.widget_2.setStyleSheet("QWidget {\n"
"    background-color: #81cdc6;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(420, 50))
        self.logo.setMaximumSize(QtCore.QSize(350, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
"\n"
"border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(200, 0))
        self.widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}")
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(45, 0, 45, 25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcomeLabel = QtWidgets.QLabel(self.widget)
        self.welcomeLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.welcomeLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("border:none;")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout.addWidget(self.welcomeLabel)
        self.password_input = QtWidgets.QLineEdit(self.widget)
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
        self.username_input = QtWidgets.QLineEdit(self.widget)
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
        self.show_password_checkbox = QtWidgets.QCheckBox(self.widget)
        self.show_password_checkbox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.show_password_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_password_checkbox.setStyleSheet("border-color:white;\n"
"")
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.verticalLayout.addWidget(self.show_password_checkbox)
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setMinimumSize(QtCore.QSize(200, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.loginButton.setFont(font)
        self.loginButton.setMouseTracking(True)
        self.loginButton.setTabletTracking(True)
        self.loginButton.setStyleSheet("QPushButton {\n"
" background-color: #10cc94;\n"
"border-radius:12px;\n"
"color:#fff;\n"
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
"\n"
"border:none;\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.forgotButton = QtWidgets.QPushButton(self.widget)
        self.forgotButton.setMinimumSize(QtCore.QSize(100, 0))
        self.forgotButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.forgotButton.setFont(font)
        self.forgotButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color:#4169E1;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #265C42;\n"
"}\n"
"")
        self.forgotButton.setObjectName("forgotButton")
        self.verticalLayout.addWidget(self.forgotButton)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", " Welcome Back!"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.show_password_checkbox.setText(_translate("MainWindow", "Show Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.forgotButton.setText(_translate("MainWindow", "Forgot your password?"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
