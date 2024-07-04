import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class AdminLoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Admin Login')
        self.setGeometry(200, 200, 300, 180)

        self.layout = QtWidgets.QVBoxLayout(self)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.help_label = QtWidgets.QLabel("An admin is required to perform this task, please contact an admin.", self)
        self.help_label.setStyleSheet("QLineEdit {\n"
                                          "  background-color: #c6c6c8;\n"
                                          "  padding: 4px;\n"
                                          "  border: none;\n"
                                          "  border-radius: 12px;\n"
                                          "  position: relative;\n"
                                          "  z-index: 0;\n"
                                          "}")
        self.help_label.setFont(font)
        self.layout.addWidget(self.help_label)

        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setMinimumSize(QtCore.QSize(150, 55))
        self.username_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit {\n"
                                          "  background-color: #c6c6c8;\n"
                                          "  padding: 4px;\n"
                                          "  border: none;\n"
                                          "  border-radius: 12px;\n"
                                          "  position: relative;\n"
                                          "  z-index: 0;\n"
                                          "}")
        self.username_input.setText("")
        self.username_input.setFrame(True)
        self.username_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_input.setPlaceholderText('Username')
        self.layout.addWidget(self.username_input)
        

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setMinimumSize(QtCore.QSize(150, 55))
        self.password_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("QLineEdit {\n"
                                          "  background-color: #c6c6c8;\n"
                                          "  padding: 4px;\n"
                                          "  border: none;\n"
                                          "  border-radius: 10px;\n"
                                          "  position: relative;\n"
                                          "  z-index: 0;\n"
                                          "}")
        self.password_input.setText("")
        self.password_input.setFrame(True)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton('Login', self)
        self.login_button.setMinimumSize(QtCore.QSize(150, 50))
        self.login_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.login_button.setFont(font)
        self.login_button.setMouseTracking(True)
        self.login_button.setTabletTracking(True)
        self.login_button.setStyleSheet("QPushButton {\n"
                                       " background-color: #10cc94;\n"
                                       " border-radius: 12px;\n"
                                       " color: #fff;\n"
                                       "}\n"
                                       "QPushButton#quit_button {\n"
                                       "   background-color: green;\n"
                                       "}\n"
                                       "QPushButton::pressed {\n"
                                       "   background-color: #fff;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "   background-color: #0a9c73;\n"
                                       "}\n"
                                       "border:none;")
        self.login_button.setObjectName("loginButton")
        self.layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.check_credentials)

    def check_credentials(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not all([username, password]):
            QtWidgets.QMessageBox.warning(self, 'Login Failed', 'Please fill in all the fields.')
            return

        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            query = "SELECT user_id FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                if self.is_admin(user_id):
                    self.accept()  # Close dialog with accept status if credentials are correct and user is admin
                else:
                    QtWidgets.QMessageBox.warning(self, 'Login Failed', 'You are not authorized as an admin.')
            else:
                QtWidgets.QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, 'Database Error', f'Database error: {e}')

        finally:
            conn.close()

    def is_admin(self, user_id):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            query = "SELECT 1 FROM admin WHERE user_id = ?"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            return result is not None

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, 'Database Error', f'Database error: {e}')

        finally:
            conn.close()

    @staticmethod
    def get_credentials(parent=None):
        dialog = AdminLoginDialog(parent)
        result = dialog.exec_()
        return result == QtWidgets.QDialog.Accepted
    
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
        from select_registration import Register
        from user_login import Login
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
        if AdminLoginDialog.get_credentials(self.MainWindow):
            self.MainWindow.setCentralWidget(self.register_widget)

from assets import logo_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Selection()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
