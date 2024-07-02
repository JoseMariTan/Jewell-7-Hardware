import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sqlite3
from assets import logo_rc
import random
import string

class StaffRegistration(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(1218, 820)
        self.setStyleSheet("background-color: #F0F0F0;")
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.widget_2 = QtWidgets.QWidget(self)
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
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")

        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(420, 50))
        self.logo.setMaximumSize(QtCore.QSize(450, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
"\n"
"border:none;")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.whiteContainer = QtWidgets.QWidget(self)
        self.whiteContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.whiteContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.whiteContainer.setAutoFillBackground(False)
        self.whiteContainer.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}")
        self.whiteContainer.setObjectName("whiteContainer")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.whiteContainer)
        self.gridLayout_2.setContentsMargins(45, 15, 45, 50)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.backButton = QtWidgets.QPushButton(self.whiteContainer)
        self.backButton.setMinimumSize(QtCore.QSize(0, 0))
        self.backButton.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(28)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
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
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 0, 0, 1, 1)

        self.firstName_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.firstName_input.setMinimumSize(QtCore.QSize(150, 55))
        self.firstName_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.firstName_input.setFont(font)
        self.firstName_input.setStyleSheet("\n"
"QLineEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding: 4px;\n"
"  border: none;\n"
"border-radius:12px;\n"
"  position: relative;\n"
"}\n"
"")
        self.firstName_input.setObjectName("firstName_input")
        self.gridLayout_2.addWidget(self.firstName_input, 1, 0, 1, 1)

        self.lastName_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.lastName_input.setMinimumSize(QtCore.QSize(150, 55))
        self.lastName_input.setMaximumSize(QtCore.QSize(500, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lastName_input.setFont(font)
        self.lastName_input.setStyleSheet("\n"
"QLineEdit {\n"
"  background-color: #c6c6c8;\n"
"  padding: 4px;\n"
"  border: none;\n"
"border-radius:12px;\n"
"  position: relative;\n"
"}\n"
"")
        self.lastName_input.setObjectName("lastName_input")
        self.gridLayout_2.addWidget(self.lastName_input, 2, 0, 1, 1)

        self.username_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.username_input.setMinimumSize(QtCore.QSize(150, 55))
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
        self.username_input.setObjectName("username_input")
        self.gridLayout_2.addWidget(self.username_input, 3, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.password_input = QtWidgets.QLineEdit(self.whiteContainer)
        self.password_input.setMinimumSize(QtCore.QSize(150, 55))
        self.password_input.setMaximumSize(QtCore.QSize(500, 55))
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
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout.addWidget(self.password_input)

        self.birthdate_edit = QtWidgets.QDateEdit(self.whiteContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdate_edit.sizePolicy().hasHeightForWidth())
        self.birthdate_edit.setSizePolicy(sizePolicy)
        self.birthdate_edit.setMinimumSize(QtCore.QSize(150, 55))
        self.birthdate_edit.setMaximumSize(QtCore.QSize(500, 55))
        self.birthdate_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birthdate_edit.setFont(font)
        self.birthdate_edit.setStyleSheet("\n"
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
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setObjectName("birthdate_edit")
        self.horizontalLayout.addWidget(self.birthdate_edit)

        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(60)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.show_password_checkbox = QtWidgets.QCheckBox(self.whiteContainer)
        self.show_password_checkbox.setMinimumSize(QtCore.QSize(150, 0))
        self.show_password_checkbox.setMaximumSize(QtCore.QSize(500, 20))
        self.show_password_checkbox.setFont(font)
        self.show_password_checkbox.setStyleSheet("QCheckBox { border: none; }")
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.horizontalLayout_2.addWidget(self.show_password_checkbox)

        self.setBirthdate_label = QtWidgets.QLabel(self.whiteContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setBirthdate_label.sizePolicy().hasHeightForWidth())
        self.setBirthdate_label.setSizePolicy(sizePolicy)
        self.setBirthdate_label.setMinimumSize(QtCore.QSize(150, 0))
        self.setBirthdate_label.setMaximumSize(QtCore.QSize(500, 20))
        self.setBirthdate_label.setFont(font)
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
        self.setBirthdate_label.setObjectName("setBirthdate_label")
        self.horizontalLayout_2.addWidget(self.setBirthdate_label)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.registerButton = QtWidgets.QPushButton(self.whiteContainer)
        self.registerButton.setMinimumSize(QtCore.QSize(150, 50))
        self.registerButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"border:none;\n"
"")
        
        self.registerButton.setObjectName("registerButton")
        self.gridLayout_2.addWidget(self.registerButton, 6, 0, 1, 1)


        self.clearButton = QtWidgets.QPushButton(self.whiteContainer)
        self.clearButton.setMinimumSize(QtCore.QSize(150, 50))
        self.clearButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("QPushButton {\n"
" background-color: #F88379;\n"
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
"border-radius: 20px;\n"
"border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #F66150;\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 8, 0, 1, 1)

        self.gridLayout_3.addWidget(self.whiteContainer, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StaffRegistration", "Staff Registration"))
        self.backButton.setText(_translate("StaffRegistration", "←"))
        self.firstName_input.setPlaceholderText(_translate("StaffRegistration", "First Name"))
        self.lastName_input.setPlaceholderText(_translate("StaffRegistration", "Last Name"))
        self.username_input.setPlaceholderText(_translate("StaffRegistration", "Username"))
        self.password_input.setPlaceholderText(_translate("StaffRegistration", "Password"))
        self.show_password_checkbox.setText(_translate("StaffRegistration", "Show Password"))
        self.setBirthdate_label.setText(_translate("StaffRegistration", "Set Birthdate"))
        self.registerButton.setText(_translate("StaffRegistration", "Register"))
        self.clearButton.setText(_translate("StaffRegistration", "Clear"))

    
        # Connect signals to slots
        self.registerButton.clicked.connect(self.register_staff)
        self.clearButton.clicked.connect(self.clear_text)
        self.backButton.clicked.connect(self.go_back)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
    
        
    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.Checked:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
            
    def go_back(self):
        QtWidgets.QApplication.instance().activeWindow().close()
        from registerSelection import Register
        self.close()
        self.previous_window = Register()
        self.previous_window.showFullScreen()

    def clear_text(self):
        self.firstName_input.clear()
        self.lastName_input.clear()
        self.username_input.clear()
        self.password_input.clear()

    def generate_staff_id(self):
        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
    
        try:
            while True:
                # Get the current date in the format YYYYMMDD
                current_date = datetime.now().strftime("%Y%m%d")
            
                # Generate a random letter from A to Z
                random_letter = random.choice(string.ascii_uppercase)
            
                # Combine the parts to form the staff ID
                staff_id = f"STAFF{current_date}{random_letter}"
            
                # Check if the staff ID already exists in the database
                cursor.execute("SELECT 1 FROM staff WHERE staff_id = ?", (staff_id,))
                if not cursor.fetchone():
                    return staff_id
        finally:
            # Ensure the database connection is closed
            conn.close()
            
    def generate_user_id(self):
        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
    
        try:
            while True:
                # Get the current date in the format YYYYMMDD
                current_date = datetime.now().strftime("%Y%m%d")
            
                # Generate a random letter from A to Z
                random_letter = random.choice(string.ascii_uppercase)
            
                # Combine the parts to form the user ID
                user_id = f"USER{current_date}{random_letter}"
            
                # Check if the user ID already exists in the database
                cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
                if not cursor.fetchone():
                    return user_id
        finally:
            # Ensure the database connection is closed
            conn.close()

    def register_staff(self):
            # Fetching data from input fields
            first_name = self.firstName_input.text().strip()
            last_name = self.lastName_input.text().strip()
            username = self.username_input.text().strip()
            password = self.password_input.text().strip()
            birthdate = self.birthdate_edit.date().toString(QtCore.Qt.ISODate)
            loa = "staff"
            user_id = self.generate_user_id()
            staff_id = self.generate_staff_id()

            # Validation: Check if any field is empty
            if not all([first_name, last_name, username, password]):
                # Displaying a message box for error
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Please fill in all the fields.")
                msg.setWindowTitle("Error")
                msg.exec_()
                return
            
            # Validation: Check if the password length is between 8 and 12 characters
            if not (8 <= len(password) <= 12):
                # Displaying a message box for error
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Password must be between 8 and 12 characters long.")
                msg.setWindowTitle("Error")
                msg.exec_()
                return
            
            # Validation: Check if names contain only alphabets
            name_pattern = re.compile("^[A-Za-z]+$")

            if not name_pattern.match(first_name) or (last_name and not name_pattern.match(last_name)):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Names can only contain alphabets.")
                msg.setWindowTitle("Error")
                msg.exec_()
                return

            current_datetime = datetime.today()
            date_log = current_datetime.strftime('%Y-%m-%d')
            time_log = current_datetime.strftime("%I:%M %p")
            log_id = self.generate_log_id()

            # Establishing connection with SQLite database
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()

            # Check if username already exists
            cursor.execute("SELECT username FROM users WHERE username=?", (username,))
            if cursor.fetchone():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Username already exists. Please choose a different username.")
                msg.setWindowTitle("Error")
                msg.exec_()
                
                conn.close()
                return

            # Inserting data into the users table
            cursor.execute('''INSERT INTO users (user_id, first_name, last_name, username, password, loa) 
                    VALUES (?, ?, ?, ?, ?, ?)''', (user_id, first_name, last_name, username, password, loa))

            # Inserting data into the staff table using the retrieved user_id
            cursor.execute('''INSERT INTO staff (staff_id, first_name, last_name, birthdate, date_started, user_id) 
                    VALUES (?, ?, ?, ?, ?, ?)''', (staff_id, first_name, last_name, birthdate, date_log, user_id))

            action = "register"
            
            # Inserting data into the user_logs table using the retrieved user_id
            cursor.execute('''INSERT INTO user_logs (log_id, user_id, action, time, date) 
                        VALUES (?, ?, ?, ?, ?)''', (log_id, user_id, action, time_log, date_log))

            # Committing the transaction and closing connection
            conn.commit()
            conn.close()

            # Displaying a message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("User Registered Successfully!")
            msg.setWindowTitle("Success")
            msg.exec_()

            from selection_screen import Selection
            self.window = QtWidgets.QMainWindow()
            self.ui = Selection()
            self.ui.setupUi(self.window)
            self.window.showFullScreen()
            self.close() 
        
    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.Checked:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
            
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
