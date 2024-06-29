import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class UsersTab(QtWidgets.QWidget):
    user_modified = QtCore.pyqtSignal()

    def __init__(self, user_id, parent=None):
        super(UsersTab, self,).__init__(parent)
        self.setupUi(self)
        self.user_id = user_id
        self.search_button.clicked.connect(self.search_users)
        self.modify_button.clicked.connect(self.open_modify_user_dialog)
        self.changeStatus_button.clicked.connect(self.deactivate_user)
        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)
        self.load_data()

    def setupUi(self, UsersTab):
        UsersTab.setObjectName("UsersTab")
        UsersTab.resize(1332, 747)
        UsersTab.setStyleSheet("background-color:#fff;")
        self.gridLayout = QtWidgets.QGridLayout(UsersTab)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search_button = QtWidgets.QPushButton(UsersTab)
        self.search_button.setMinimumSize(QtCore.QSize(50, 50))
        self.search_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.search_button.setFont(font)
        self.search_button.setMouseTracking(True)
        self.search_button.setTabletTracking(True)
        self.search_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:25px;\n"
"color:black;\n"
";\n"
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
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"shoppingbag:hover{\n"
"color:#fff;\n"
"background-repeat:no-repeat;\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/search/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(20, 20))
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_2.addWidget(self.search_button)
        self.search_input = QtWidgets.QLineEdit(UsersTab)
        self.search_input.setMinimumSize(QtCore.QSize(300, 50))
        self.search_input.setMaximumSize(QtCore.QSize(600, 75))
        self.search_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_input.setStyleSheet("border-radius:25px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"background-color:#f6f4f4;\n"
"")
        self.search_input.setText("")
        self.search_input.setCursorPosition(0)
        self.search_input.setDragEnabled(False)
        self.search_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_2.addWidget(self.search_input)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(UsersTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #88ccc4; }")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(300, -1, 300, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.modify_button = QtWidgets.QPushButton(UsersTab)
        self.modify_button.setMinimumSize(QtCore.QSize(175, 50))
        self.modify_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.modify_button.setFont(font)
        self.modify_button.setMouseTracking(True)
        self.modify_button.setTabletTracking(True)
        self.modify_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.modify_button.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modify_button.setIcon(icon1)
        self.modify_button.setIconSize(QtCore.QSize(22, 22))
        self.modify_button.setObjectName("modify_button")
        self.horizontalLayout.addWidget(self.modify_button)
        self.changeStatus_button = QtWidgets.QPushButton(UsersTab)
        self.changeStatus_button.setMinimumSize(QtCore.QSize(175, 50))
        self.changeStatus_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.changeStatus_button.setFont(font)
        self.changeStatus_button.setMouseTracking(True)
        self.changeStatus_button.setTabletTracking(True)
        self.changeStatus_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.changeStatus_button.setStyleSheet("QPushButton {\n"
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
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #E5676B;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.changeStatus_button.setIcon(icon1)
        self.changeStatus_button.setIconSize(QtCore.QSize(22, 22))
        self.changeStatus_button.setObjectName("changeStatus_button")
        self.horizontalLayout.addWidget(self.changeStatus_button)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(UsersTab)
        QtCore.QMetaObject.connectSlotsByName(UsersTab)

    def retranslateUi(self, UsersTab):
        _translate = QtCore.QCoreApplication.translate
        UsersTab.setWindowTitle(_translate("UsersTab", "Users"))
        self.search_input.setPlaceholderText(_translate("UsersTab", "  Search Users..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UsersTab", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UsersTab", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("UsersTab", "Username"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("UsersTab", "Password"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("UsersTab", "Level of Access"))
        self.modify_button.setText(_translate("UsersTab", "Modify"))
        self.changeStatus_button.setText(_translate("UsersTab", "Activate / Deactivate"))

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        try:
            if search_query:
                search_param = f'%{search_query}%'
                exact_search_param = f'{search_query}'
                cur.execute("""
                    SELECT rowid, first_name, last_name, username, password, loa, status 
                    FROM users
                    WHERE 
                        (first_name LIKE ? COLLATE NOCASE OR first_name = ?) OR
                        (last_name LIKE ? COLLATE NOCASE OR last_name = ?) OR
                        (username LIKE ? COLLATE NOCASE OR username = ?) OR
                        (password LIKE ? COLLATE NOCASE OR password = ?) OR
                        (loa LIKE ? COLLATE NOCASE OR loa = ?) OR
                        (status LIKE ? COLLATE NOCASE OR status = ?)""",
                    (search_param, exact_search_param, search_param, exact_search_param,
                    search_param, exact_search_param, search_param, exact_search_param,
                    search_param, exact_search_param, search_param, exact_search_param))
            else:
                cur.execute("""
                    SELECT rowid, first_name, last_name, username, password, loa, status 
                    FROM users """)

            users = cur.fetchall()
            if not users:
                QtWidgets.QMessageBox.information(self, "No Data Found", "No data found.")
                return

            self.tableWidget.setRowCount(len(users))
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderLabels(["Row Id", "First Name", "Last Name", "Username", "Password", "Level of Access", "Status"])
            self.tableWidget.setColumnHidden(0, True)

            for i, user in enumerate(users):
                for j, value in enumerate(user):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        except sqlite3.Error as e:
            print("SQLite error:", e)
            QtWidgets.QMessageBox.critical(self, "Database Error", "Failed to load data. Please try again.")

        finally:
            conn.close()

    def search_users(self):
        search_query = self.search_input.text()
        self.load_data(search_query)

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

    def deactivate_user(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            first_name_item = self.tableWidget.item(selected_row, 1)
            last_name_item = self.tableWidget.item(selected_row, 2)
            username_item = self.tableWidget.item(selected_row, 3)

            if first_name_item and last_name_item and username_item:
                first_name = first_name_item.text()
                last_name = last_name_item.text()
                username = username_item.text()

                conn = sqlite3.connect('j7h.db')
                cur = conn.cursor()
                cur.execute("SELECT user_id, status FROM users WHERE first_name = ? AND last_name = ? AND username = ?", 
                            (first_name, last_name, username))
                user_data = cur.fetchone()

                if user_data:
                    user_id, status = user_data

                    if user_id == self.user_id:
                        QtWidgets.QMessageBox.warning(
                            None,
                            "Error",
                            "Cannot deactivate the logged-in user."
                        )
                        conn.close()
                        return

                    new_status = 'Deactivated' if status == 'Active' else 'Active'
                    action = 'deactivate' if new_status == 'Deactivated' else 'activate'

                    reply = QtWidgets.QMessageBox.question(
                        None,
                        'Confirmation',
                        f'Are you sure you want to {action} this user?',
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                        QtWidgets.QMessageBox.No
                    )

                    if reply == QtWidgets.QMessageBox.Yes:
                        cur.execute("UPDATE users SET status = ? WHERE user_id = ?", (new_status, user_id))
                        conn.commit()
                        self.load_data()
                conn.close()
            else:
                QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to deactivate.")
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to deactivate.")


    def on_selection_changed(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item:
                    item.setSelected(True)

class ModifyUserDialog(QtWidgets.QDialog):
    def __init__(self, rowid, user, parent=None):
        super(ModifyUserDialog, self).__init__(parent)
        self.setWindowTitle("Modify User")
        self.setGeometry(300, 300, 400, 400)
        self.rowid = rowid

        self.layout = QtWidgets.QVBoxLayout()

        # Validators
        name_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z]+"))
        password_validator = QtGui.QRegExpValidator(QtCore.QRegExp(".{8,12}"))

        # First Name
        self.firstName_label = QtWidgets.QLabel("First Name: *")
        self.firstName_input = QtWidgets.QLineEdit()
        self.firstName_input.setText(user[0])
        self.firstName_input.setValidator(name_validator)
        self.layout.addWidget(self.firstName_label)
        self.layout.addWidget(self.firstName_input)

        # Last Name
        self.lastName_label = QtWidgets.QLabel("Last Name: *")
        self.lastName_input = QtWidgets.QLineEdit()
        self.lastName_input.setText(user[1])
        self.lastName_input.setValidator(name_validator)
        self.layout.addWidget(self.lastName_label)
        self.layout.addWidget(self.lastName_input)

        # Username
        self.username_label = QtWidgets.QLabel("Username: *")
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setText(user[2])
        self.username_input.setValidator(name_validator)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        # Password
        self.password_label = QtWidgets.QLabel("Password: *")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setText(user[3] or "")
        self.password_input.setValidator(password_validator)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        # Modify Button
        self.modify_button = QtWidgets.QPushButton("Update")
        self.modify_button.clicked.connect(self.modify_user)
        self.layout.addWidget(self.modify_button)

        self.setLayout(self.layout)

    def modify_user(self):
        first_name = self.firstName_input.text()
        last_name = self.lastName_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if not first_name or not last_name or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Input Error", "All required fields must be filled")
            return

        if not (8 <= len(password) <= 12):
            QtWidgets.QMessageBox.warning(self, "Input Error", "Password must be between 8 and 12 characters")
            return

        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?, password = ? WHERE rowid = ?",
                    (first_name, last_name, username, password, self.rowid))
        conn.commit()
        conn.close()

        self.accept()
