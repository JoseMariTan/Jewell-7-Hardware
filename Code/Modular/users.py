import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class UsersTab(QtWidgets.QWidget):
    user_modified = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UsersTab, self).__init__(parent)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton("Search", self)
        self.horizontalLayout_2.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search_users)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.modifyUser_button = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.modifyUser_button.setFont(font)
        self.modifyUser_button.setObjectName("modifyUser_button")
        self.modifyUser_button.setMinimumSize(QtCore.QSize(80, 80))
        self.modifyUser_button.setSizePolicy(button_size_policy)
        self.modifyUser_button.clicked.connect(self.open_modify_user_dialog)
        self.modifyUser_button.setIcon(QtGui.QIcon("edit_icon.png"))
        self.modifyUser_button.setIconSize(QtCore.QSize(36, 36))

        self.voidProduct_button = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.voidProduct_button.setFont(font)
        self.voidProduct_button.setObjectName("voidProduct_button")
        self.voidProduct_button.setMinimumSize(QtCore.QSize(80, 80))
        self.voidProduct_button.setSizePolicy(button_size_policy)
        self.voidProduct_button.clicked.connect(self.void_user)
        self.voidProduct_button.setIcon(QtGui.QIcon("bin_icon.png"))
        self.voidProduct_button.setIconSize(QtCore.QSize(36, 36))

        self.verticalLayout_2.addWidget(self.modifyUser_button)
        self.verticalLayout_2.addWidget(self.voidProduct_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFixedHeight(self.tableWidget.verticalHeader().defaultSectionSize() * 30)
        self.scrollArea.setWidget(self.tableWidget)
        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.load_data()

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        if search_query:
            cur.execute("SELECT rowid, first_name, last_name, username, password, loa FROM users WHERE "
                        "first_name LIKE ? OR last_name LIKE ? OR username LIKE ? OR password LIKE ? OR loa LIKE ?",
                        ('%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            cur.execute("SELECT rowid, first_name, last_name, username, password, loa FROM users")

        users = cur.fetchall()
    
        self.tableWidget.setRowCount(len(users))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["RowID", "First Name", "Last Name", "Username", "Password", "LOA"])

        for i, user in enumerate(users):
            for j, value in enumerate(user):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()

        self.tableWidget.setColumnHidden(0, True)

    def resize_table(self):
        header = self.tableWidget.horizontalHeader()
        for i in range(1, self.tableWidget.columnCount() - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.Stretch)

        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def open_modify_user_dialog(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            rowid_item = self.tableWidget.item(selected_row, 0)
            if rowid_item:
                rowid = int(rowid_item.text())

                conn = sqlite3.connect('j7h.db')
                cur = conn.cursor()
                cur.execute("SELECT first_name, last_name, username, password, loa FROM users WHERE rowid = ?", (rowid,))
                user = cur.fetchone()
                conn.close()

                if user:
                    dialog = ModifyUserDialog(rowid, user)
                    dialog.exec_()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to modify.")

    def void_user(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            rowid_item = self.tableWidget.item(selected_row, 0)
            if rowid_item:
                rowid = int(rowid_item.text())

                reply = QtWidgets.QMessageBox.question(
                    None,
                    'Confirmation',
                    'Are you sure you want to void this user?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No
                )

                if reply == QtWidgets.QMessageBox.Yes:
                    conn = sqlite3.connect('j7h.db')
                    cur = conn.cursor()
                    cur.execute("DELETE FROM users WHERE rowid = ?", (rowid,))
                    conn.commit()
                    conn.close()
                    self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to void.")

    def search_users(self):
        search_query = self.lineEdit.text()
        self.load_data(search_query)


class ModifyUserDialog(QtWidgets.QDialog):
    def __init__(self, rowid, user, parent=None):
        super(ModifyUserDialog, self).__init__(parent)
        self.setWindowTitle("Modify User")
        self.setGeometry(300, 300, 400, 400)
        self.rowid = rowid

        self.layout = QtWidgets.QVBoxLayout()
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9]+"))

        self.firstName_label = QtWidgets.QLabel("First Name (required)")
        self.firstName_input = QtWidgets.QLineEdit()
        self.firstName_input.setText(user[0])
        self.firstName_input.setValidator(validator)
        self.layout.addWidget(self.firstName_label)
        self.layout.addWidget(self.firstName_input)

        self.lastName_label = QtWidgets.QLabel("Last_Name (required)")
        self.lastName_input = QtWidgets.QLineEdit()
        self.lastName_input.setText(user[1])
        self.lastName_input.setValidator(validator)
        self.layout.addWidget(self.lastName_label)
        self.layout.addWidget(self.lastName_input)

        self.username_label = QtWidgets.QLabel("Username (required)")
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setText(user[2])
        self.username_input.setValidator(validator)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QtWidgets.QLabel("Password (required)")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setValidator(validator)
        self.password_input.setText(user[3] or "")
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_user)
        self.layout.addWidget(self.modify_button)
        self.setLayout(self.layout)

    def modify_user(self):
        first_name = self.firstName_input.text()
        last_name = self.lastName_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if not first_name or not last_name or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Input Error", "All fields must be filled")
            return

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?, password = ? WHERE rowid = ?",
                    (first_name, last_name, username, password, self.rowid))
        conn.commit()
        conn.close()

        self.accept()
