import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import random, string
from assets import logo_rc

class ForgotPassword(object):
    def setupUi(self, forgotPassword):
        forgotPassword.setObjectName("forgotPassword")
        forgotPassword.resize(1218, 820)
        forgotPassword.setStyleSheet("background-color: #FCFEFE;")
        forgotPassword.setAnimated(True)
        forgotPassword.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(forgotPassword)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(420, 50))
        self.logo.setMaximumSize(QtCore.QSize(450, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
"\n"
"border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.whiteContainer = QtWidgets.QWidget(self.centralwidget)
        self.whiteContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.whiteContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.whiteContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.whiteContainer.setAutoFillBackground(False)
        self.whiteContainer.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}")
        self.whiteContainer.setInputMethodHints(QtCore.Qt.ImhNone)
        self.whiteContainer.setObjectName("whiteContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.whiteContainer)
        self.gridLayout_2.setContentsMargins(45, 10, 45, 50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newPassword_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.newPassword_input.setMinimumSize(QtCore.QSize(150, 55))
        self.newPassword_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.newPassword_input.setFont(font)
        self.newPassword_input.setStyleSheet("\n"
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
        self.newPassword_input.setText("")
        self.newPassword_input.setFrame(True)
        self.newPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword_input.setObjectName("newPassword_input")
        self.horizontalLayout.addWidget(self.newPassword_input)
        self.confirmPassword_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.confirmPassword_input.setMinimumSize(QtCore.QSize(150, 55))
        self.confirmPassword_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.confirmPassword_input.setFont(font)
        self.confirmPassword_input.setStyleSheet("\n"
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
        self.confirmPassword_input.setText("")
        self.confirmPassword_input.setFrame(True)
        self.confirmPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword_input.setObjectName("confirmPassword_input")
        self.horizontalLayout.addWidget(self.confirmPassword_input)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 9, 0, 1, 1)
        self.changePassword_button = QtWidgets.QPushButton(self.whiteContainer)
        self.changePassword_button.setMinimumSize(QtCore.QSize(150, 50))
        self.changePassword_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.changePassword_button.setFont(font)
        self.changePassword_button.setMouseTracking(True)
        self.changePassword_button.setTabletTracking(True)
        self.changePassword_button.setStyleSheet("QPushButton {\n"
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
        self.changePassword_button.setObjectName("changePassword_button")
        self.gridLayout_2.addWidget(self.changePassword_button, 10, 0, 1, 1)
        self.setBirthdate_label = QtWidgets.QLabel(self.whiteContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setBirthdate_label.sizePolicy().hasHeightForWidth())
        self.setBirthdate_label.setSizePolicy(sizePolicy)
        self.setBirthdate_label.setMinimumSize(QtCore.QSize(150, 0))
        self.setBirthdate_label.setMaximumSize(QtCore.QSize(500, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.setBirthdate_label.setFont(font)
        self.setBirthdate_label.setMouseTracking(True)
        self.setBirthdate_label.setStyleSheet("QLabel {\n"
"  background-color: #fff;\n"
"  padding: 4px;\n"
"  border: none;\n"
"  border-radius: 12px; /* Adjusted border-radius */\n"
"  position: relative;\n"
"  z-index: 0; /* We force a stacking context */\n"
"  color: black;\n"
"}\n"
"")
        self.setBirthdate_label.setLineWidth(0)
        self.setBirthdate_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setBirthdate_label.setIndent(0)
        self.setBirthdate_label.setObjectName("setBirthdate_label")
        self.gridLayout_2.addWidget(self.setBirthdate_label, 5, 0, 1, 1)
        self.Title = QtWidgets.QLabel(self.whiteContainer)
        self.Title.setMinimumSize(QtCore.QSize(0, 10))
        self.Title.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("border:none;")
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 1, 0, 1, 1)
        self.show_password_checkbox = QtWidgets.QCheckBox(self.whiteContainer)
        self.show_password_checkbox.setMinimumSize(QtCore.QSize(150, 0))
        self.show_password_checkbox.setMaximumSize(QtCore.QSize(500, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.show_password_checkbox.setFont(font)
        self.show_password_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_password_checkbox.setStyleSheet("border-color:white;\n"
"")
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.gridLayout_2.addWidget(self.show_password_checkbox, 8, 0, 1, 1)
        self.back_Button = QtWidgets.QPushButton(self.whiteContainer)
        self.back_Button.setMinimumSize(QtCore.QSize(0, 0))
        self.back_Button.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.back_Button.setFont(font)
        self.back_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back_Button.setStyleSheet("QPushButton {\n"
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
        self.back_Button.setIconSize(QtCore.QSize(16, 16))
        self.back_Button.setFlat(True)
        self.back_Button.setObjectName("back_Button")
        self.gridLayout_2.addWidget(self.back_Button, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.birthdate_input = QtWidgets.QDateEdit(self.whiteContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdate_input.sizePolicy().hasHeightForWidth())
        self.birthdate_input.setSizePolicy(sizePolicy)
        self.birthdate_input.setMinimumSize(QtCore.QSize(150, 55))
        self.birthdate_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.birthdate_input.setFont(font)
        self.birthdate_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birthdate_input.setStyleSheet("\n"
"QDateEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding: 4px;\n"
"  border: none;\n"
"border-radius:12px;\n"
"  position: relative;\n"
"  z-index: 0; /* We force a stacking context */\n"
"color:#636364;\n"
"}\n"
"")
        self.birthdate_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.birthdate_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.birthdate_input.setSpecialValueText("")
        self.birthdate_input.setCalendarPopup(True)
        self.birthdate_input.setObjectName("birthdate_input")
        self.horizontalLayout_2.addWidget(self.birthdate_input)
        self.middleName_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.middleName_input.setMinimumSize(QtCore.QSize(150, 55))
        self.middleName_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.middleName_input.setFont(font)
        self.middleName_input.setStyleSheet("\n"
"QLineEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding: 4px;\n"
"  border: none;\n"
"border-radius:12px;\n"
"  position: relative;\n"
"  z-index: 0; /* We force a stacking context */\n"
"}\n"
"")
        self.middleName_input.setText("")
        self.middleName_input.setFrame(True)
        self.middleName_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.middleName_input.setObjectName("middleName_input")
        self.horizontalLayout_2.addWidget(self.middleName_input)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.whiteContainer, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        forgotPassword.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(forgotPassword)
        self.statusbar.setObjectName("statusbar")
        forgotPassword.setStatusBar(self.statusbar)

        self.retranslateUi(forgotPassword)
        self.back_Button.clicked.connect(self.go_back)
        QtCore.QMetaObject.connectSlotsByName(forgotPassword)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        self.changePassword_button.clicked.connect(self.change_password)

    def retranslateUi(self, forgotPassword):
        _translate = QtCore.QCoreApplication.translate
        forgotPassword.setWindowTitle(_translate("forgotPassword", "forgotPassword"))
        self.newPassword_input.setPlaceholderText(_translate("forgotPassword", "New Password"))
        self.confirmPassword_input.setPlaceholderText(_translate("forgotPassword", "Confirm Password"))
        self.changePassword_button.setText(_translate("forgotPassword", "Change Password"))
        self.setBirthdate_label.setText(_translate("forgotPassword", "Set Birthdate"))
        self.Title.setText(_translate("forgotPassword", "                  Forgot Password"))
        self.show_password_checkbox.setText(_translate("forgotPassword", "Show Password"))
        self.back_Button.setText(_translate("forgotPassword", "←"))
        self.middleName_input.setPlaceholderText(_translate("forgotPassword", "Middle Name"))

    def change_password(self):
        birthdate = self.birthdate_input.date().toString(QtCore.Qt.ISODate)
        middle_name = self.middleName_input.text().strip()
        new_password = self.newPassword_input.text().strip()
        confirm_password = self.confirmPassword_input.text().strip()

        # Validation: Check if any field is empty
        if not all([birthdate, new_password, confirm_password]):
            self.show_error_message("Please fill in all the fields.")
            return

        # Validation: Check if the password length is between 8 and 12 characters
        if not (8 <= len(new_password) <= 12):
            # Displaying a message box for error
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Password must be between 8 and 12 characters long.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return


        # Validation: Check if new password and confirm password match
        if new_password != confirm_password:
            self.show_error_message("New password and confirm password do not match.")
            return

        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            # SQL query to verify the birthdate and middle name
            query = "SELECT user_id FROM admin WHERE birthdate = ? AND middle_name = ?"
            cursor.execute(query, (birthdate, middle_name))
            result = cursor.fetchone()

            # Check if the query returned a result
            if result is None:
                self.show_error_message("Invalid birthdate or middle name.")
                return

            # If the details are correct, update the password in the database
            user_id = result[0]
            # Get the current date and time
            current_datetime = datetime.today()
            date_log = current_datetime.strftime('%Y-%m-%d')
            time_log = current_datetime.strftime("%I:%M %p")
            log_id = self.generate_log_id()

            # Inserting data into the user_logs table
            action = "changed password"
            cursor.execute('''INSERT INTO user_logs (log_id, user_id, action, time, date) 
                      VALUES (?, ?, ?, ?, ?)''', (log_id, user_id, action, time_log, date_log))
    
            # Update the password in the users table
            cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (new_password, user_id))

            conn.commit()

            # Display success message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Password changed successfully!")
            msg.setWindowTitle("Success")
            msg.exec_()

            self.go_back()
        except sqlite3.Error as e:
            self.show_error_message(f"Database error: {e}")

    def generate_log_id(self):
        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            while True:
                # Get the current date in the format YYYYMMDD
                current_date = datetime.now().strftime("%Y%m%d")
            
                # Generate three random letters from A to Z
                random_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            
                # Combine the parts to form the transaction ID
                log_id = f"LOG{current_date}{random_letters}"
            
                # Check if the transaction ID already exists in the database
                cursor.execute("SELECT 1 FROM user_logs WHERE log_id = ?", (log_id,))
                if not cursor.fetchone():
                    return log_id
        finally:
            # Ensure the database connection is closed
            conn.close()    
            
    def show_error_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def close_window(self):
        QtWidgets.QApplication.instance().activeWindow().close()

    def go_back(self):
        QtWidgets.QApplication.instance().activeWindow().close()
        from user_login import Login
        self.previous_window = Login()
        self.previous_window.showFullScreen()

    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.Checked:
            self.newPassword_input.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.confirmPassword_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.newPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
            self.confirmPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ForgotPassword()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
