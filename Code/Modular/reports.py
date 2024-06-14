import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

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


        # Add sub-tabs to the tab widget
        self.tab_widget.addTab(self.reports_tab, "User Logs")  
        self.tab_widget.addTab(self.transactions_tab, "Transactions")


        # Set layouts for each sub-tab
        self.initReportsTab()
        self.initTransactionsTab()


        self.layout.addWidget(self.tab_widget)

        # Connect itemSelectionChanged signal to handle row selection
        self.transactions_table.itemSelectionChanged.connect(self.on_selection_changed)


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

        # Create buttons for clearing logs
        buttons_layout = QtWidgets.QHBoxLayout()
        clear_logs_button = QtWidgets.QPushButton("Clear User Logs")
        
        # Connect button signals to slots
        clear_logs_button.clicked.connect(self.clear_user_logs)

        # Add buttons to the layout
        buttons_layout.addWidget(clear_logs_button)

        # Add buttons layout to the main layout
        layout.addLayout(buttons_layout)

    def initTransactionsTab(self):
        layout = QtWidgets.QVBoxLayout(self.transactions_tab)
        
        # Create the table widget
        self.transactions_table = QtWidgets.QTableWidget()
        self.transactions_table.setColumnCount(13)  # Update column count to match the number of columns
        self.transactions_table.setHorizontalHeaderLabels([
            'Total Amount',  'Price', 'Quantity', 'Customer', 'Product','Brand', 'Variation', 'Size', 'Category', 'Time', 
            'Date', 'User ID', 'Cashier'
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
        clear_logs_button = QtWidgets.QPushButton("Clear Transaction Logs")
        flag_transaction_button = QtWidgets.QPushButton("Flag Transaction")
        delete_log_button = QtWidgets.QPushButton("Remove Transaction")
        receipt_button = QtWidgets.QPushButton("Generate Receipt")

        # Connect button signals to slots
        clear_logs_button.clicked.connect(self.clear_logs)
        flag_transaction_button.clicked.connect(self.flag_transaction)
        delete_log_button.clicked.connect(self.remove_log)
        receipt_button.clicked.connect(self.generate_receipt)

        # Add buttons to the layout
        buttons_layout.addWidget(clear_logs_button)
        buttons_layout.addWidget(flag_transaction_button)
        buttons_layout.addWidget(delete_log_button)
        buttons_layout.addWidget(receipt_button)

        # Add buttons layout to the main layout
        layout.addLayout(buttons_layout)

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

    def on_selection_changed(self):
        selected_rows = set()
        selected_transactions = set()  # Track selected transactions (customer name + time)

        # Iterate over selected items to collect rows and transactions
        for item in self.transactions_table.selectedItems():
            row = item.row()
            customer_name = self.transactions_table.item(row, 2).text()
            time = self.transactions_table.item(row, 5).text()  # Assuming time is in column 5
            transaction = f"{customer_name} - {time}"
            selected_rows.add(row)
            selected_transactions.add(transaction)

        # Find all rows with the same customer names and times as selected
        for row in range(self.transactions_table.rowCount()):
            customer_name = self.transactions_table.item(row, 2).text()
            time = self.transactions_table.item(row, 5).text()  # Assuming time is in column 5
            transaction = f"{customer_name} - {time}"
            if transaction in selected_transactions:
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
            query = """SELECT transactions.transaction_id, transactions.total_price, transactions.qty, transactions.customer, products.product_name, products.brand, 
                           products.var, products.size, products.category, transactions.time, transactions.date, transactions.user_id, users.first_name, transactions.product_id
                    FROM transactions
                    JOIN products ON transactions.product_id = products.product_id
                    JOIN users ON transactions.user_id = users.user_id
                    WHERE transactions.user_id LIKE ? OR transactions.customer LIKE ? OR transactions.date LIKE ? OR transactions.time LIKE ?"""
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
            cursor.execute("""SELECT transactions.transaction_id, transactions.total_price, transactions.qty, transactions.customer, products.product_name, products.brand, 
                           products.var, products.size, products.category, transactions.time, transactions.date, transactions.user_id, users.first_name, transactions.product_id
                    FROM transactions
                    JOIN products ON transactions.product_id = products.product_id
                    JOIN users ON transactions.user_id = users.user_id""")

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

                row_number += 1

            # Set the total_total_price if there's more than one product in the group
            if span_length > 1:
                formatted_total_price = "{:.2f}".format(total_total_price)
                item = QTableWidgetItem(str(formatted_total_price))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.transactions_table.setItem(row_number - span_length, 0, item)


    #button functionalities

    def flag_transaction(self):
        for row in set(item.row() for item in self.transactions_table.selectedItems()):
            if row in self.flagged_rows:
                # Unflag the row (remove red background)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setBackground(QtGui.QColor(Qt.white))  # Set background to white
                self.flagged_rows.remove(row)
            else:
                # Flag the row (set orange background)
                for column in range(self.transactions_table.columnCount()):
                    item = self.transactions_table.item(row, column)
                    if item:
                        item.setBackground(QtGui.QColor('orange'))  # Set background to orange
                self.flagged_rows.add(row)


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

    def clear_logs(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to clear all logs?', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Clear the table
            self.transactions_table.clearContents()
            self.transactions_table.setRowCount(0)
            # Delete all log entries from the database
            self.delete_all_logs_from_database()

    def delete_all_logs_from_database(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions")
        conn.commit()
        conn.close()

    def clear_user_logs(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to clear all user logs?', 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Clear the table
            self.user_logs_table.clearContents()
            self.user_logs_table.setRowCount(0)
            # Delete all log entries from the database
            self.delete_all_user_logs_from_database()

    def delete_all_user_logs_from_database(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_logs")
        conn.commit()
        conn.close()

    def generate_receipt(self):
        selected_items = self.transactions_table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'No Selection', 'Please select a transaction to generate a receipt.')
            return

        # Get the unique transaction IDs from the selected items
        transaction_ids = set()
        for item in selected_items:
            transaction_id = self.transactions_table.item(item.row(), 0).text()
            transaction_ids.add(transaction_id)

        if len(transaction_ids) != 1:
            QMessageBox.warning(self, 'Multiple Selections', 'Please select items from a single transaction.')
            return

        transaction_id = transaction_ids.pop()

        # Get the row index of the selected transaction
        row = selected_items[0].row()

        transaction_details = {
            'Transaction ID': self.transactions_table.item(row, 0).text(),
            'Customer': self.transactions_table.item(row, 1).text(),
            'Date and Time': self.transactions_table.item(row, 3).text(),
            'Total Price': self.transactions_table.item(row, 4).text(),
            'Product ID': self.transactions_table.item(row, 5).text(),
            'Product Name': self.transactions_table.item(row, 6).text(),
            'Brand': self.transactions_table.item(row, 7).text(),
            'Size': self.transactions_table.item(row, 8).text(),
            'Variation': self.transactions_table.item(row, 9).text(),
        }

        # Show the receipt dialog with transaction details
        receipt_dialog = ReceiptDialog(transaction_details)
        receipt_dialog.exec_()
