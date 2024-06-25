
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Selection(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 820)
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
        
        self.LogoContainer = QtWidgets.QWidget(self.centralwidget)
        self.LogoContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.LogoContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.LogoContainer.setStyleSheet("QWidget {\n"
                                         "    background-color: #81cdc6;\n"
                                         "    border-style: solid;\n"
                                         "    border-color: black;\n"
                                         "    border-width: 1px;\n"
                                         "}")
        self.LogoContainer.setObjectName("LogoContainer")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LogoContainer)
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.logo = QtWidgets.QLabel(self.LogoContainer)
        self.logo.setMinimumSize(QtCore.QSize(450, 50))
        self.logo.setMaximumSize(QtCore.QSize(350, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
                                "border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        
        self.gridLayout.addWidget(self.LogoContainer, 0, 0, 1, 1)
        
        self.Container = QtWidgets.QWidget(self.centralwidget)
        self.Container.setMinimumSize(QtCore.QSize(200, 0))
        self.Container.setMaximumSize(QtCore.QSize(500, 16777215))
        self.Container.setAutoFillBackground(False)
        self.Container.setStyleSheet("QWidget {\n"
                                     "    background-color: #fff;\n"
                                     "    border-style: solid;\n"
                                     "    border-color: black;\n"
                                     "    border-width: 1px;\n"
                                     "}")
        self.Container.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Container.setObjectName("Container")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Container)
        self.gridLayout_3.setContentsMargins(45, -1, 45, -1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.SignupLabel = QtWidgets.QLabel(self.Container)
        self.SignupLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.SignupLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.SignupLabel.setFont(font)
        self.SignupLabel.setStyleSheet("border:none;")
        self.SignupLabel.setObjectName("SignupLabel")
        self.gridLayout_3.addWidget(self.SignupLabel, 0, 0, 1, 1)
        
        self.registerButton = QtWidgets.QPushButton(self.Container)
        self.registerButton.setMinimumSize(QtCore.QSize(200, 50))
        self.registerButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.registerButton.setFont(font)
        self.registerButton.setMouseTracking(True)
        self.registerButton.setTabletTracking(True)
        self.registerButton.setStyleSheet("QPushButton {\n"
                                          "    background-color: #10cc94;\n"
                                          "    border-radius: 12px;\n"
                                          "    color: #fff;\n"
                                          "}\n"
                                          "QPushButton#quit_button {\n"
                                          "    background-color: green;\n"
                                          "}\n"
                                          "QPushButton::pressed {\n"
                                          "    background-color: #fff;\n"
                                          "}\n"
                                          "QpushButton{\n"
                                          "    border: 2px solid #555;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "    border-width: 200px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: #0a9c73;\n"
                                          "    transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
                                          "}\n"
                                          "\n"
                                          "border:none;\n"
                                          "")
        self.registerButton.setObjectName("registerButton")
        self.gridLayout_3.addWidget(self.registerButton, 2, 0, 1, 1)
        
        self.loginButton = QtWidgets.QPushButton(self.Container)
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
                                       "    background-color: #10cc94;\n"
                                       "    border-radius: 12px;\n"
                                       "    color: #fff;\n"
                                       "}\n"
                                       "QPushButton#quit_button {\n"
                                       "    background-color: green;\n"
                                       "}\n"
                                       "QPushButton::pressed {\n"
                                       "    background-color: #fff;\n"
                                       "}\n"
                                       "QpushButton{\n"
                                       "    border: 2px solid #555;\n"
                                       "    border-radius: 20px;\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 200px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #0a9c73;\n"
                                       "    transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
                                       "}\n"
                                       "\n"
                                       "border:none;\n"
                                       "")
        self.loginButton.setObjectName("loginButton")
        self.gridLayout_3.addWidget(self.loginButton, 1, 0, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        
        self.gridLayout.addWidget(self.Container, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Create instances of LoginWidget and RegisterWidget
        from login import Login
        from registerSelection import Register
        self.login_widget = Login()
        self.register_widget = Register()
        
        # Connect buttons to functions
        self.loginButton.clicked.connect(self.switch_to_login)
        self.registerButton.clicked.connect(self.switch_to_register)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jewell 7 Hardware"))
        self.SignupLabel.setText(_translate("MainWindow", "        Login or Create an Account!"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        
    def switch_to_login(self):
        # Switch to LoginWidget
        self.MainWindow.setCentralWidget(self.login_widget)
        
    def switch_to_register(self):
        # Switch to RegisterWidget
       self.MainWindow.setCentralWidget(self.register_widget)


import logo_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Selection()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
