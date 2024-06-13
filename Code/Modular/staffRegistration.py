import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sqlite3

class StaffRegistration(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("StaffRegistration")
        self.resize(816, 715)
        self.setStyleSheet("background-color:#D9D9D9;")
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 60, 601, 585))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.Jewell7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Jewell7.setFont(font)
        self.Jewell7.setAlignment(QtCore.Qt.AlignCenter)
        self.Jewell7.setObjectName("Jewell7")
        self.verticalLayout.addWidget(self.Jewell7)
        
        self.Hardware = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Hardware.setFont(font)
        self.Hardware.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Hardware.setAlignment(QtCore.Qt.AlignCenter)
        self.Hardware.setObjectName("Hardware")
        self.verticalLayout.addWidget(self.Hardware)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.firstName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.firstName_label.setFont(font)
        self.firstName_label.setObjectName("firstName_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstName_label)
        
        self.firstName_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.firstName_input.setFont(font)
        self.firstName_input.setStyleSheet("background-color:#FFFFFF;")
        self.firstName_input.setText("")
        self.firstName_input.setPlaceholderText("")
        self.firstName_input.setObjectName("firstName_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstName_input)
        
        self.lastName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lastName_label.setFont(font)
        self.lastName_label.setObjectName("lastName_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastName_label)
        
        self.lastName_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lastName_input.setFont(font)
        self.lastName_input.setStyleSheet("background-color:#FFFFFF;")
        self.lastName_input.setText("")
        self.lastName_input.setPlaceholderText("")
        self.lastName_input.setObjectName("lastName_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastName_input)
        
        self.username_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.username_label)
        
        self.username_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("background-color:#FFFFFF;")
        self.username_input.setText("")
        self.username_input.setPlaceholderText("")
        self.username_input.setObjectName("username_input")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_input)
        
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.password_label)
        
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background-color:#FFFFFF;")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("")
        self.password_input.setObjectName("password_input")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_input)

        self.show_password_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.show_password_checkbox)

        self.birthdate_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_label.setFont(font)
        self.birthdate_label.setObjectName("birthdate_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.birthdate_label)
        
        self.birthdate_edit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_edit.setFont(font)
        self.birthdate_edit.setMouseTracking(False)
        self.birthdate_edit.setStyleSheet("background-color:#FFFFFF;")
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setObjectName("birthdate_edit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.birthdate_edit)
        
        self.loa_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loa_label.setFont(font)
        self.loa_label.setObjectName("loa_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.loa_label)
        
        self.loa_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loa_input.setFont(font)
        self.loa_input.setStyleSheet("background-color:#D9D9D9; border: none;")
        self.loa_input.setReadOnly(True)
        self.loa_input.setPlaceholderText("")
        self.loa_input.setObjectName("loa_input")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.loa_input)
        
        self.verticalLayout.addLayout(self.formLayout_2)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.registerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("background-color:#53C851;")
        self.registerButton.setDefault(True)
        self.registerButton.setFlat(False)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.registerButton)
        
        self.clearButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color:#E14545;\n"
        "")
        self.clearButton.setDefault(True)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.setStatusBar(QtWidgets.QStatusBar(self))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StaffRegistration", "Staff Registration"))
        self.Jewell7.setText(_translate("StaffRegistration", "Jewell 7"))
        self.Hardware.setText(_translate("StaffRegistration", "Hardware"))
        self.firstName_label.setText(_translate("StaffRegistration", "First Name:"))
        self.lastName_label.setText(_translate("StaffRegistration", "Last Name:"))
        self.username_label.setText(_translate("StaffRegistration", "Username:"))
        self.password_label.setText(_translate("StaffRegistration", "Password:"))
        self.show_password_checkbox.setText(_translate("Login", "Show Password"))
        self.birthdate_label.setText(_translate("StaffRegistration", "Birthdate:"))
        self.loa_label.setText(_translate("StaffRegistration", "LOA:"))
        self.loa_input.setText(_translate("StaffRegistration", "staff"))
        self.registerButton.setText(_translate("StaffRegistration", "Register"))
        self.clearButton.setText(_translate("StaffRegistration", "Clear"))

        # Connect signals to slots
        self.registerButton.clicked.connect(self.register_staff)
        self.clearButton.clicked.connect(self.clear_text)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)

    def clear_text(self):
        self.firstName_input.clear()
        self.lastName_input.clear()
        self.username_input.clear()
        self.password_input.clear()

    def register_staff(self):
        # Fetching data from input fields
        first_name = self.firstName_input.text().strip()
        last_name = self.lastName_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        birthdate = self.birthdate_edit.date().toString(QtCore.Qt.ISODate)
        loa = self.loa_input.text().strip()

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
        cursor.execute('''INSERT INTO users (first_name, last_name, username, password, loa) 
                  VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, username, password, loa))

        # Retrieve the user_id of the newly inserted user
        user_id = cursor.lastrowid  # This fetches the last inserted row id, which is the user_id

        # Inserting data into the staff table using the retrieved user_id
        cursor.execute('''INSERT INTO staff (first_name, last_name, birthdate, date_started, user_id) 
                  VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, birthdate, date_log, user_id))

        action = "register"
        
        # Inserting data into the user_logs table using the retrieved user_id
        cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                      VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))

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
        self.window.show()
        self.close() 
        
    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.Checked:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StaffRegistration()
    window.show()
    sys.exit(app.exec_())