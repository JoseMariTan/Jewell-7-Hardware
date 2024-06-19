import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import sqlite3
from main import Ui_MainWindow
from selection_screen import Selection
from forgotPassword import Ui_ForgotPassword
import logo_rc

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_window = None

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1218, 820)
        Login.setStyleSheet("background-color: #FCFEFE;")
        Login.setAnimated(True)
        Login.setDocumentMode(False)
        
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(500, 600))
        self.widget_2.setStyleSheet("QWidget {\n"
                                    "    background-color: #81cdc6;\n"
                                    "    border-style: solid;\n"
                                    "    border-color: black;\n"
                                    "    border-width: 1px;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(420, 50))
        self.logo.setMaximumSize(QtCore.QSize(450, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
                                "border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(200, 0))
        self.widget.setMaximumSize(QtCore.QSize(500, 600))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget {\n"
                                  "    background-color: #fff;\n"
                                  "    border-style: solid;\n"
                                  "    border-color: black;\n"
                                  "    border-width: 1px;\n"
                                  "}")
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(45, -1, 45, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        self.back_button.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color:#3d3d3d    ;\n"
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
        self.back_button.setText("←")
        self.back_button.clicked.connect(self.go_back)
        self.verticalLayout.addWidget(self.back_button)
        
        self.welcomeLabel = QtWidgets.QLabel(self.widget)
        self.welcomeLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.welcomeLabel.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("border:none;")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout.addWidget(self.welcomeLabel)
        
        self.username_input = QtWidgets.QLineEdit(self.widget)
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
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        
        self.password_input = QtWidgets.QLineEdit(self.widget)
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
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        
        self.show_password_checkbox = QtWidgets.QCheckBox(self.widget)
        self.show_password_checkbox.setMinimumSize(QtCore.QSize(150, 0))
        self.show_password_checkbox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.show_password_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_password_checkbox.setStyleSheet("border-color:white;")
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.verticalLayout.addWidget(self.show_password_checkbox)
        
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setMinimumSize(QtCore.QSize(150, 50))
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
                                       "   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
                                       "}\n"
                                       "border:none;")
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login_user)
        self.verticalLayout.addWidget(self.loginButton)
        
        self.forgotButton = QtWidgets.QPushButton(self.widget)
        self.forgotButton.setMinimumSize(QtCore.QSize(150, 0))
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
        self.forgotButton.clicked.connect(self.forgot_password)
        
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        Login.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.welcomeLabel.setText(_translate("Login", "                  Welcome Back!"))
        self.username_input.setPlaceholderText(_translate("Login", "Username"))
        self.password_input.setPlaceholderText(_translate("Login", "Password"))
        self.show_password_checkbox.setText(_translate("Login", "Show Password"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.forgotButton.setText(_translate("Login", "Forgot your Password?"))

    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

    def login_user(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not all([username, password]):
            self.show_error_message("Please fill in all the fields.")
            return

        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            query = "SELECT user_id, password FROM users WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
        
            if result is None:
                self.show_error_message("Invalid username or password.")
                return

            user_id, stored_password = result
            current_datetime = datetime.today()
            date_log = current_datetime.strftime('%Y-%m-%d')
            time_log = current_datetime.strftime("%I:%M %p")
            
            if stored_password == password:
                action = "login"
                cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                            VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))
                conn.commit()
                self.open_main_window(user_id)  # Pass user_id to the main window

            else:
                action = "login attempt"
                cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                            VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))
                conn.commit()
                self.show_error_message("Invalid username or password.")
        except sqlite3.Error as e:
            self.show_error_message(f"Database error: {e}")
        finally:
            conn.close()

    def open_main_window(self, user_id):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(user_id)
        self.ui.setupUi(self.main_window)
        self.main_window.showFullScreen()
        self.close()

    def forgot_password(self):
        self.forgotPasswordWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ForgotPassword()
        self.ui.setupUi(self.forgotPasswordWindow)
        self.forgotPasswordWindow.show()
        self.close()

    def show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def go_back(self):
        self.new_window = Selection()  
        self.new_window.showFullScreen()
        self.close()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Login = Login()
    Login.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Login = Login()
    Login.show()
    sys.exit(app.exec_())
