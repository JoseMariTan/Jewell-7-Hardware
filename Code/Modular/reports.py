import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from datetime import datetime
import random, string

class ReceiptDialog(QtWidgets.QDialog):
    def __init__(self, transaction_details):
        super().__init__()
        self.transaction_details = transaction_details
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Receipt')
        self.setGeometry(100, 100, 400, 600)
        layout = QtWidgets.QVBoxLayout()

        # Add header
        header_label = QtWidgets.QLabel("Receipt")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        layout.addWidget(header_label)

        # Add store details
        store_details_label = QtWidgets.QLabel("Store Name\nAddress Line 1\nAddress Line 2\nPhone Number")
        store_details_label.setAlignment(Qt.AlignCenter)
        store_details_label.setStyleSheet("font-size: 10pt;")
        layout.addWidget(store_details_label)

        # Add a line separator
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(separator)

        # Add transaction details in a structured format
        details_layout = QtWidgets.QFormLayout()

        details_layout.addRow("Transaction ID:", QtWidgets.QLabel(self.transaction_details['Transaction ID']))
        details_layout.addRow("Customer:", QtWidgets.QLabel(self.transaction_details['Customer']))
        details_layout.addRow("Date and Time:", QtWidgets.QLabel(self.transaction_details['Date and Time']))
        details_layout.addRow("Total Price:", QtWidgets.QLabel(self.transaction_details['Total Price']))

        # Add another separator
        layout.addWidget(separator)
        
        # Add product details in a table format
        products_table = QtWidgets.QTableWidget()
        products_table.setColumnCount(5)
        products_table.setHorizontalHeaderLabels(['Product ID', 'Product Name', 'Brand', 'Size', 'Variation'])
        products_table.setRowCount(1)
        products_table.setItem(0, 0, QTableWidgetItem(self.transaction_details['Product ID']))
        products_table.setItem(0, 1, QTableWidgetItem(self.transaction_details['Product Name']))
        products_table.setItem(0, 2, QTableWidgetItem(self.transaction_details['Brand']))
        products_table.setItem(0, 3, QTableWidgetItem(self.transaction_details['Size']))
        products_table.setItem(0, 4, QTableWidgetItem(self.transaction_details['Variation']))
        products_table.horizontalHeader().setStretchLastSection(True)
        products_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        layout.addWidget(products_table)

        # Add footer
        footer_label = QtWidgets.QLabel("Thank you for shopping with us!")
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("font-size: 10pt; font-style: italic;")
        layout.addWidget(footer_label)

        # Add a close button
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        self.returns_table.itemSelectionChanged.connect(self.on_selection_changed)

#Class for Reports Tab
class ReportsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flagged_rows = set()
        
    def initUI(self):
        self.setWindowTitle('Reports')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Search Component
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setFixedHeight(40) 
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setFixedHeight(40)
        self.search_button.clicked.connect(self.search_logs)
        self.search_button.clicked.connect(self.search_transactions)
        self.horizontalLayout.addWidget(self.search_input)
        self.horizontalLayout.addWidget(self.search_button)
        self.layout.addLayout(self.horizontalLayout)

        # Create tab widget and sub-tabs
        self.tab_widget = QtWidgets.QTabWidget()
        self.reports_tab = QtWidgets.QWidget()
        self.transactions_tab = QtWidgets.QWidget()
        self.returns_tab = QtWidgets.QWidget()


        # Add sub-tabs to the tab widget
        self.tab_widget.addTab(self.reports_tab, "User Logs")  
        self.tab_widget.addTab(self.transactions_tab, "Transactions")
        self.tab_widget.addTab(self.returns_tab, "Returns")
        self.tab_widget.setStyleSheet(""" QHeaderView::section { background-color: #ff7d7d;} """)

        # Set layouts for each sub-tab
        self.initReportsTab()
        self.initTransactionsTab()
        self.initReturnsTab()

        self.layout.addWidget(self.tab_widget)

        # Connect itemSelectionChanged signal to handle row selection
        self.transactions_table.itemSelectionChanged.connect(self.on_selection_changed)
        self.returns_table.itemSelectionChanged.connect(self.on_selection_row)

        # Connect tabChanged signal to clear the search query
        self.tab_widget.currentChanged.connect(self.clear_search_query)

    def initReportsTab(self):
        layout = QtWidgets.QVBoxLayout(self.reports_tab)
        
        # Create the table widget for user logs
        self.user_logs_table = QtWidgets.QTableWidget()
        self.user_logs_table.setColumnCount(5)  # Set column count to match the number of columns in user_logs
        self.user_logs_table.setHorizontalHeaderLabels(['Log ID', 'User ID', 'Action', 'Time', 'Date'])
        self.user_logs_table.horizontalHeader().setStretchLastSection(True)
        self.user_logs_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.user_logs_table.verticalHeader().setVisible(False)

        # Add the table widget to the layout
        layout.addWidget(self.user_logs_table)

        # Load user logs into the table
        self.load_user_logs()

        buttons_layout = QtWidgets.QHBoxLayout()

        # Add buttons layout to the main layout
        layout.addLayout(buttons_layout)

    def initTransactionsTab(self):
        layout = QtWidgets.QVBoxLayout(self.transactions_tab)
        
        # Create the table widget
        self.transactions_table = QtWidgets.QTableWidget()
        self.transactions_table.setColumnCount(16)  # Update column count to match the number of columns
        self.transactions_table.setHorizontalHeaderLabels([
            'Total Amount',  'Price', 'Quantity', 'Customer', 'Product','Brand', 'Variation', 'Size', 'Category', 'Time', 
            'Date', 'Type', 'User ID', 'Cashier', 'Payment ID', 'Contact'
        ])
        
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        self.transactions_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.transactions_table.verticalHeader().setVisible(False)

        # Add the table widget to the layout
        layout.addWidget(self.transactions_table)

        # Load transactions into the table
        self.load_transactions()

        # Create buttons for clearing logs, flagging transactions, and generating receipts
        buttons_layout = QtWidgets.QHBoxLayout()
        return_button = QtWidgets.QPushButton("Return Item")
        flag_transaction_button = QtWidgets.QPushButton("Flag Transaction")
        receipt_button = QtWidgets.QPushButton("Generate Receipt")

        # Connect button signals to slots
        flag_transaction_button.clicked.connect(self.flag_transaction)
        receipt_button.clicked.connect(self.generate_receipt)
        return_button.clicked.connect(self.return_selected_item)

        # Add buttons to the layout
        buttons_layout.addWidget(return_button)
        buttons_layout.addWidget(flag_transaction_button)
        buttons_layout.addWidget(receipt_button)

        # Add buttons layout to the main layout
        layout.addLayout(buttons_layout)
        
    def initReturnsTab(self):
        layout = QtWidgets.QVBoxLayout(self.returns_tab)

        # Create the table widget for returns
        self.returns_table = QtWidgets.QTableWidget()
        self.returns_table.setColumnCount(8)  # Set column count to match the number of columns in returns
        self.returns_table.setHorizontalHeaderLabels(['Return ID', 'Product Name', 'Brand', 'Variation', 'Size', 'Quantity', 'Date', 'Transaction ID'])
        self.returns_table.horizontalHeader().setStretchLastSection(True)
        self.returns_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.returns_table.verticalHeader().setVisible(False)

        # Add the table widget to the layout
        layout.addWidget(self.returns_table)

        # Load returns into the table
        self.load_returns()

    def search_logs(self):
        search_query = self.search_input.text()
        self.load_user_logs(search_query)

    def search_transactions(self):
        search_query = self.search_input.text()
        self.load_transactions(search_query)

    def clear_search_query(self):
        self.search_input.clear()
        self.search_logs()
        self.search_transactions()
        
    def on_selection_row(self):
        selected_rows = set()
        for item in self.returns_table.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.returns_table.columnCount()):
                item = self.returns_table.item(row, column)
                if item:
                    item.setSelected(True)
                    
    def on_selection_changed(self):
        selected_rows = set()
        selected_payment_ids = set()  # Track selected payment_ids

        # Iterate over selected items to collect rows and payment_ids
        for item in self.transactions_table.selectedItems():
            row = item.row()
            payment_id = self.transactions_table.item(row, 14).text()  # Get payment_id from the 14th column
            selected_rows.add(row)
            selected_payment_ids.add(payment_id)

        # Find all rows with the same payment_id as selected
        for row in range(self.transactions_table.rowCount()):
            payment_id = self.transactions_table.item(row, 14).text()  # Get payment_id from the 14th column
            if payment_id in selected_payment_ids:
                selected_rows.add(row)

        # Select all identified rows in the table
        for row in selected_rows:
            for column in range(self.transactions_table.columnCount()):
                item = self.transactions_table.item(row, column)
                if item:
                    item.setSelected(True)


    def load_user_logs(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        if search_query:
            query = "SELECT log_id, user_id, action, time, date FROM user_logs WHERE user_id LIKE ? OR action LIKE ? OR date LIKE ?"
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
            cursor.execute("SELECT log_id, user_id, action, time, date FROM user_logs")

        rows = cursor.fetchall()
        conn.close()

        # Set the number of rows in the table
        self.user_logs_table.setRowCount(len(rows))

        # Populate the table with user logs data
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.user_logs_table.setItem(row_number, column_number, item)


    def load_transactions(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        if search_query:
            query = """SELECT t.transaction_id, t.total_price, t.qty, t.customer, t.product_name, t.brand, 
                            t.var, t.size, t.category, t.time, t.date, t.type, t.user_id, u.first_name, 
                            t.payment_id, t.contact, t.product_id, t.is_flagged
                    FROM transactions t
                    LEFT JOIN users u ON t.user_id = u.user_id
                    WHERE t.user_id LIKE ? OR t.customer LIKE ? OR t.date LIKE ? OR t.time LIKE ?"""
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
            query = """SELECT t.transaction_id, t.total_price, t.qty, t.customer, t.product_name, t.brand, 
                            t.var, t.size, t.category, t.time, t.date, t.type, t.user_id, u.first_name, 
                            t.payment_id, t.contact, t.product_id, t.is_flagged
                    FROM transactions t
                    LEFT JOIN users u ON t.user_id = u.user_id"""
            cursor.execute(query)

        rows = cursor.fetchall()
        conn.close()

        # Group rows by customer name and time
        grouped_rows = {}
        for row in rows:
            customer_name = row[3]
            time = row[9] 
            key = (customer_name, time)
            if key not in grouped_rows:
                grouped_rows[key] = []
            grouped_rows[key].append(row)

        # Calculate total number of rows after grouping
        total_rows = sum(len(group) for group in grouped_rows.values())

        # Set the number of rows in the table
        self.transactions_table.setRowCount(total_rows)

        # Populate the table with transaction data
        row_number = 0
        for customer_name, group in grouped_rows.items():
            span_length = len(group)
            total_total_price = 0  # Initialize total_total_price to 0

            for i, row_data in enumerate(group):
                total_price = float(row_data[1])  # Get the total price for each row
                total_total_price += total_price  # Add to the total_total_price

                if i == 0:  # For the first row in the group
                    item = QTableWidgetItem(str(total_price))
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    self.transactions_table.setItem(row_number, 0, item)
                    # Set the span for the first column
                    if span_length > 1:
                        self.transactions_table.setSpan(row_number, 0, span_length, 1)
                else:  # For subsequent rows in the group
                    # For subsequent rows, leave the first column empty
                    self.transactions_table.setItem(row_number, 0, QTableWidgetItem(''))

                # Populate the rest of the data
                for column_number, data in enumerate(row_data[1:], start=1):
                    item = QTableWidgetItem(str(data))
                    self.transactions_table.setItem(row_number, column_number, item)
                    # Set the background color based on is_flagged value
                    if row_data[-1] == 1:  # Assuming is_flagged is the last column
                        item.setBackground(QtGui.QColor('orange'))
                    else:
                        item.setBackground(QtGui.QColor('white'))

                row_number += 1

            # Set the total_total_price if there's more than one product in the group
            if span_length > 1:
                formatted_total_price = "{:.2f}".format(total_total_price)
                item = QTableWidgetItem(str(formatted_total_price))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.transactions_table.setItem(row_number - span_length, 0, item)
                # Set the background color for the total price cell
                if group[0][-1] == 1:  # Check is_flagged of the first row in the group
                    item.setBackground(QtGui.QColor('orange'))
                else:
                    item.setBackground(QtGui.QColor('white'))

    def load_returns(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        if search_query:
            query = """SELECT return_id, product_name, brand, var, size, qty, date, transaction_id 
                    FROM returns 
                    WHERE return_id LIKE ? OR product_name LIKE ? OR brand LIKE ? OR date LIKE ?"""
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
            cursor.execute("SELECT return_id, product_name, brand, var, size, qty, date, transaction_id FROM returns")

        rows = cursor.fetchall()
        conn.close()

        # Set the number of rows in the table
        self.returns_table.setRowCount(len(rows))

        # Populate the table with returns data
        for row_number, row_data in enumerate(rows):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.returns_table.setItem(row_number, column_number, item)

    #button functionalities

    def flag_transaction(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        for row in set(item.row() for item in self.transactions_table.selectedItems()):
            payment_id = self.transactions_table.item(row, 14).text()  # Assuming payment_id is in the 15th column (index 14)

            if row in self.flagged_rows:
                # Unflag the row (remove orange background)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setBackground(QtGui.QColor(Qt.white))  # Set background to white
                self.flagged_rows.remove(row)
                cursor.execute("UPDATE transactions SET is_flagged = 0 WHERE payment_id = ?", (payment_id,))
            else:
                # Flag the row (set orange background)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setBackground(QtGui.QColor('orange'))  # Set background to orange
                self.flagged_rows.add(row)
                cursor.execute("UPDATE transactions SET is_flagged = 1 WHERE payment_id = ?", (payment_id,))

        conn.commit()
        conn.close()

    def remove_log(self):
        selected_items = self.transactions_table.selectedItems()
        if not selected_items:
            return

        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to remove selected logs?', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            rows_to_remove = set()
            transaction_ids = []  # Store transaction IDs to delete from the database
            for item in selected_items:
                row = item.row()
                column = item.column()
                transaction_id = self.transactions_table.item(row, 0).text()  # Assuming transaction ID is in column 0
                rows_to_remove.add(row)
                transaction_ids.append(transaction_id)

            # Remove the flagged rows from the table
            for row in sorted(rows_to_remove, reverse=True):
                self.transactions_table.removeRow(row)
                # Since the rows are removed, adjust the flagged rows set accordingly
                self.flagged_rows.discard(row)

            # Delete logs from the database
            for transaction_id in transaction_ids:
                self.delete_log_from_database(transaction_id)

    def delete_log_from_database(self, transaction_id):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
        conn.commit()
        conn.close()

    def return_selected_item(self):
        selected_items = self.transactions_table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'No Selection', 'Please select a transaction to return.')
            return

        # Assuming payment_id is in the 15th column (index 14)
        row = selected_items[0].row()
        payment_id_item = self.transactions_table.item(row, 14) 
        if payment_id_item:
            payment_id = payment_id_item.text()
            # Get the transaction details from the database based on payment_id
            transaction_details = self.get_transaction_details(payment_id)
            print(transaction_details)

            if not transaction_details:
                QMessageBox.warning(self, 'Error', 'Failed to retrieve transaction details.')
                return

            # Generate a return_id
            return_id = self.generate_return_id()

            # Insert into returns table
            if self.insert_into_returns(return_id, transaction_details):
                QMessageBox.information(self, 'Success', 'Item returned successfully.')
                self.load_returns()
            else:
                QMessageBox.warning(self, 'Error', 'Failed to return item.')
        else:
            print("No payment_id found in selected items.")  # Debug print
            QMessageBox.warning(self, 'Error', 'No payment ID found in selected items.')


    def get_transaction_details(self, payment_id):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT transaction_id, product_name, brand, var, size, qty, date 
                        FROM transactions 
                        WHERE payment_id = ?""", (payment_id,))
        transaction_details = cursor.fetchone()

        conn.close()
        return transaction_details

    def insert_into_returns(self, return_id, transaction_details):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            # Extract transaction details
            transaction_id, product_name, brand, var, size, qty, date = transaction_details
            
            # Insert into returns table
            cursor.execute("""INSERT INTO returns (return_id, product_name, brand, var, size, qty, date, transaction_id)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (return_id, product_name, brand, var, size, qty, date, transaction_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error inserting into returns table:", e)
            conn.rollback()
            return False
        finally:
            conn.close()
    
    def generate_return_id(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            while True:
                current_date = datetime.now().strftime("%Y%m%d")
                random_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
                return_id = f"RETURN{current_date}{random_letters}"

                cursor.execute("SELECT 1 FROM returns WHERE return_id = ?", (return_id,))
                if not cursor.fetchone():
                    return return_id
        finally:
            conn.close()
            
    def generate_receipt(self):
        pass
