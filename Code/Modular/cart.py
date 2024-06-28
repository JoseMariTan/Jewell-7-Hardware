import random
import sqlite3
import string
import uuid
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class AdminLoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Admin Login')
        self.setGeometry(200, 200, 300, 180)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.help_label = QtWidgets.QLabel("Ask an Admin for Help", self)
        self.layout.addWidget(self.help_label)

        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        self.layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton('Login', self)
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
class Ui_Cart_Tab(object):
    def setupUi(self, Cart_Tab):
        Cart_Tab.setObjectName("Cart_Tab")
        Cart_Tab.resize(1284, 850)
        Cart_Tab.setStyleSheet("background-color:#fff;")
        self.gridLayout = QtWidgets.QGridLayout(Cart_Tab)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search_button = QtWidgets.QPushButton(Cart_Tab)
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
        self.search_input = QtWidgets.QLineEdit(Cart_Tab)
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
        self.tableWidget = QtWidgets.QTableWidget(Cart_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #88ccc4; }")
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_button = QtWidgets.QPushButton(Cart_Tab)
        self.clear_button.setMinimumSize(QtCore.QSize(175, 50))
        self.clear_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clear_button.setFont(font)
        self.clear_button.setMouseTracking(True)
        self.clear_button.setTabletTracking(True)
        self.clear_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear_button.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon1)
        self.clear_button.setIconSize(QtCore.QSize(22, 22))
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.remove_button = QtWidgets.QPushButton(Cart_Tab)
        self.remove_button.setMinimumSize(QtCore.QSize(175, 50))
        self.remove_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.remove_button.setFont(font)
        self.remove_button.setMouseTracking(True)
        self.remove_button.setTabletTracking(True)
        self.remove_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove_button.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/remover/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon2)
        self.remove_button.setIconSize(QtCore.QSize(22, 22))
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.mark_button = QtWidgets.QPushButton(Cart_Tab)
        self.mark_button.setMinimumSize(QtCore.QSize(175, 50))
        self.mark_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.mark_button.setFont(font)
        self.mark_button.setMouseTracking(True)
        self.mark_button.setTabletTracking(True)
        self.mark_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mark_button.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/replace/replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mark_button.setIcon(icon3)
        self.mark_button.setIconSize(QtCore.QSize(22, 22))
        self.mark_button.setObjectName("mark_button")
        self.horizontalLayout.addWidget(self.mark_button)
        self.pay_button = QtWidgets.QPushButton(Cart_Tab)
        self.pay_button.setMinimumSize(QtCore.QSize(175, 50))
        self.pay_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pay_button.setFont(font)
        self.pay_button.setMouseTracking(True)
        self.pay_button.setTabletTracking(True)
        self.pay_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pay_button.setStyleSheet("QPushButton {\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pay/checkout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pay_button.setIcon(icon4)
        self.pay_button.setIconSize(QtCore.QSize(22, 22))
        self.pay_button.setObjectName("pay_button")
        self.horizontalLayout.addWidget(self.pay_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.total_label = QtWidgets.QLabel(Cart_Tab)
        self.total_label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.total_label.setFont(font)
        self.total_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout.addWidget(self.total_label)
        self.verticalLayout.addWidget(self.total_label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        

        self.retranslateUi(Cart_Tab)
        QtCore.QMetaObject.connectSlotsByName(Cart_Tab)

    def retranslateUi(self, Cart_Tab):
        _translate = QtCore.QCoreApplication.translate
        Cart_Tab.setWindowTitle(_translate("Cart_Tab", "Cart"))
        self.search_input.setPlaceholderText(_translate("Cart_Tab", "Search cart..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Cart_Tab", "Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Cart_Tab", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Cart_Tab", "Variation"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Cart_Tab", "Size"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Cart_Tab", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Cart_Tab", "Total"))
        self.clear_button.setText(_translate("Cart_Tab", "Clear Cart"))
        self.remove_button.setText(_translate("Cart_Tab", "Remove Item"))
        self.mark_button.setText(_translate("Cart_Tab", "Mark as Replacement"))
        self.pay_button.setText(_translate("Cart_Tab", "Check Out"))
        self.total_label.setText(_translate("Cart_Tab", "Total Price: ₱ 0.00"))
        
from assets import shop_rc

class CartTab(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id  # Store the user_id
        self.ui = Ui_Cart_Tab()
        self.ui.setupUi(self)
        self.load_cart_items()  # Load cart items when CartTab is initialized

        # Connect buttons to methods
        self.ui.search_button.clicked.connect(self.search_cart)
        self.ui.pay_button.clicked.connect(self.pay)
        self.ui.remove_button.clicked.connect(self.remove_item)
        self.ui.mark_button.clicked.connect(self.mark_return)
        self.ui.clear_button.clicked.connect(self.clear_cart)
        # Connect itemSelectionChanged signal to handle row selection
        self.ui.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)
        
    def update_total_label(self):
        total = sum(float(self.ui.tableWidget.item(row, 6).text()) for row in range(self.ui.tableWidget.rowCount()))
        self.ui.total_label.setText(f"Total Price: ₱{total:.2f}")

    def load_cart_items(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT rowid, product_name, brand, var, size, qty, total_price FROM cart ORDER BY cart_id DESC""")

        if search_query:
            query = """
                SELECT c.product_name, c.qty, c.brand, c.var, c.size, p.price, (c.qty * p.price) AS total_price
                FROM cart c
                INNER JOIN products p ON c.product_name = p.product_name
                WHERE c.qty > 0 AND (c.product_name LIKE ? OR c.brand LIKE ? OR c.var LIKE ? OR c.size LIKE ?)
                ORDER BY c.cart_id DESC
                """
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        products = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(products))
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["RowID", "Product", "Brand", "Variation", "Size", "Quantity", "Total Price"])

        for i, product in enumerate(products):
            for j, value in enumerate(product):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()
        self.ui.tableWidget.setColumnHidden(0, True)
        self.update_total_label()

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.ui.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column)
                if item:
                    item.setSelected(True)
        self.update_total_label()

    def search_cart(self):
        search_query = self.search_input.text()
        self.load_cart_items(search_query)
        self.update_total_label()

    def pay(self):
        from paymentForm import PaymentForm
        if not self.ui.tableWidget.rowCount():
            QMessageBox.warning(self, "No items", "Your cart is empty.")
            return
        total_price_str = self.ui.total_label.text().replace("Total Price: ₱", "")
        total_price = float(total_price_str)
        payment_form = PaymentForm(total_price=total_price, parent=self)
        
        if payment_form.exec_() == QtWidgets.QDialog.Accepted:
            customer_name = payment_form.customer_details['name']  
            contact = payment_form.customer_details['contact']
            payment_id = payment_form.payment_id
            self.checkout(customer_name, payment_id, contact) 
            QMessageBox.information(self, "Payment Successful", "Thank you for your purchase!")
            self.load_cart_items()
        else:
            QMessageBox.warning(self, "Payment Cancelled", "Payment was not completed.")

    def remove_item(self):
        selected_rows = set()
        for item in self.ui.tableWidget.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_item = self.ui.tableWidget.item(row, 1)
            if product_item is not None:
                product_name = product_item.text()
                # Retrieve current quantity from the cart
                cursor.execute("SELECT qty FROM cart WHERE product_name = ?", (product_name,))
                current_qty_in_cart = cursor.fetchone()[0]
                # Update product quantity in the database
                cursor.execute("SELECT qty, threshold FROM products WHERE product_name = ?", (product_name,))
                result = cursor.fetchone()
                current_qty_in_db = result[0]
                threshold = result[1]
                new_qty_in_db = current_qty_in_db + current_qty_in_cart
                cursor.execute("UPDATE products SET qty = ? WHERE product_name = ?", (new_qty_in_db, product_name))
                if new_qty_in_db > threshold:
                    cursor.execute("UPDATE products SET status = 'Available' WHERE product_name = ?", (product_name,))
                # Delete item from the cart
                cursor.execute("DELETE FROM cart WHERE product_name = ?", (product_name,))
        conn.commit()
        conn.close()
        self.load_cart_items()
        self.update_total_label()

    def mark_return(self):
        # Check if admin user is logged in
        if not self.is_admin():
            if not self.show_admin_login_dialog():
                return
    
        selected_rows = set()
        for item in self.ui.tableWidget.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_name_item = self.ui.tableWidget.item(row, 1)  
            if product_name_item is not None:
                product_name = product_name_item.text()
                # Update the status to "return" in the cart table
                cursor.execute("UPDATE cart SET status = 'return', total_price = 0 WHERE product_name =?", (product_name,))
                # Update the QTableWidget directly
                total_price_item = self.ui.tableWidget.item(row, 6)  # Column index for total price
                total_price_item.setText("0.00")
        conn.commit()
        conn.close()
        self.update_total_label()

    def clear_cart(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        # Retrieve quantities of all products in the cart before clearing
        cursor.execute("SELECT product_name, qty FROM cart")
        quantities_removed = {row[0]: row[1] for row in cursor.fetchall()}

        # Update quantities of items in the products table
        for product_name, qty in quantities_removed.items():
            cursor.execute("UPDATE products SET qty = qty + ? WHERE product_name = ?", (qty, product_name))

            # Check if the product should be marked as "Available"
            cursor.execute("SELECT threshold FROM products WHERE product_name = ?", (product_name,))
            threshold = cursor.fetchone()[0]
            if qty > threshold:
                cursor.execute("UPDATE products SET status = 'Available' WHERE product_name = ?", (product_name,))

        # Clear the cart
        cursor.execute("DELETE FROM cart")

        conn.commit()
        conn.close()

        # Reload cart items
        self.load_cart_items()
        self.update_total_label()

        # Return the quantities of all products removed
        return quantities_removed
    
    def generate_transaction_id(self):
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
                transaction_id = f"TRANSAC{current_date}{random_letters}"
            
                # Check if the transaction ID already exists in the database
                cursor.execute("SELECT 1 FROM transactions WHERE transaction_id = ?", (transaction_id,))
                if not cursor.fetchone():
                    return transaction_id
        finally:
            # Ensure the database connection is closed
            conn.close()
            
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
        
    def checkout(self, customer_name, payment_id, contact):
        if not payment_id:
            QMessageBox.warning(self, "Error", "Payment ID is missing.")
            return

        # Get current date and time
        transaction_successful = False
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime("%I:%M %p")
        
        # Connect to db
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        # Use the stored user_id
        user_id = self.user_id
        
        for row in range(self.ui.tableWidget.rowCount()):
            product_name_item = self.ui.tableWidget.item(row, 1)
            brand_item = self.ui.tableWidget.item(row, 2)
            var_item = self.ui.tableWidget.item(row, 3)
            size_item = self.ui.tableWidget.item(row, 4)
            qty_item = self.ui.tableWidget.item(row, 5)
            total_price_item = self.ui.tableWidget.item(row, 6)

            if qty_item and qty_item.text():
                product_name = product_name_item.text()
                qty = int(qty_item.text())
                total_price = float(total_price_item.text())
                brand = brand_item.text() if brand_item.text() else None
                var = var_item.text() if var_item.text() else None
                size = size_item.text() if size_item.text() else None
                transaction_id = self.generate_transaction_id()
                log_id = self.generate_log_id()
                is_flagged = 0

                query = """
                    SELECT product_id 
                    FROM products 
                    WHERE product_name = ? 
                        AND (brand = ? OR brand IS NULL) 
                        AND (var = ? OR var IS NULL) 
                        AND (size = ? OR size IS NULL)
                """
                cursor.execute(query, (product_name, brand, var, size))

                product_id_result = cursor.fetchone()

                if product_id_result:
                    product_id = product_id_result[0]
                else:
                    # Log the error and continue with the next item
                    QMessageBox.warning(self, "Error", f"Product ID not found for {brand}!")
                    transaction_successful = False
                    continue  # Skip this item

            # Check the status of the item in the cart
                cursor.execute("SELECT status FROM cart WHERE product_name = ? AND brand = ? AND var = ? AND size = ?", (product_name, brand, var, size))
                status_result = cursor.fetchone()
                if status_result and status_result[0] == 'return':
                    transaction_type = "replacement"
                else:
                    transaction_type = "purchase"

                cursor.execute('''
                    INSERT INTO transactions ( transaction_id, customer, product_name, qty, total_price, date, time, type, product_id, brand, var, size, user_id, payment_id, contact, is_flagged)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''', (transaction_id, customer_name, product_name, qty, total_price, current_date, current_time, transaction_type, product_id, brand, var, size, user_id, payment_id, contact, is_flagged))

                # Update the quantity in the products table
                cursor.execute("UPDATE products SET qty = qty - ? WHERE product_id = ?", (qty, product_id))

                # Insert into user_logs table
                action = "checkout"
                cursor.execute('''
                    INSERT INTO user_logs (log_id,user_id, action, time, date)
                    VALUES (?,?,?,?,?)
                ''', (log_id, user_id, action, current_time, current_date))

                transaction_successful = True

        conn.commit()
        conn.close()

        # Clear cart table
        self.clear_cart()

        # Display success message
        if transaction_successful:
            QMessageBox.information(self, "Checkout", "Checkout successful!")
        else:
            QMessageBox.warning(self, "Checkout", "Checkout failed. Some items were not processed.")
            
    def is_admin(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            query = "SELECT 1 FROM admin WHERE user_id = ?"
            cursor.execute(query, (self.user_id,))
            result = cursor.fetchone()

            if result:
                return True
            else:
                return False
        finally:
            conn.close()
            
    def show_admin_login_dialog(self):
        return AdminLoginDialog.get_credentials(self)
    
    def resize_table(self):
        header = self.ui.tableWidget.horizontalHeader()
        for i in range(1, self.ui.tableWidget.columnCount() - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.ui.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.ResizeToContents)
