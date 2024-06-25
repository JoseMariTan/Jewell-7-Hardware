import random
import sqlite3
import string
import uuid
from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class CartTab(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id  # Store the user_id
        self.initUI()
        self.load_cart_items()  # Load cart items when CartTab is initialized

    def initUI(self):
        self.setWindowTitle('Cart')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Search Component
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setFixedHeight(40)
        self.search_input.setPlaceholderText("Search cart...")

        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setFixedHeight(40)
        self.search_button.clicked.connect(self.search_cart)
        self.horizontalLayout.addWidget(self.search_input)
        self.horizontalLayout.addWidget(self.search_button)
        self.layout.addLayout(self.horizontalLayout)

        # Create a table to display cart items
        self.cart_table = QtWidgets.QTableWidget()
        self.cart_table.setColumnCount(7)
        self.cart_table.setHorizontalHeaderLabels(['Product', 'Brand', 'Variation', 'Size', 'Quantity', 'Price', 'Total'])
        self.cart_table.horizontalHeader().setStretchLastSection(True)
        self.cart_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.cart_table.verticalHeader().setVisible(False)

        # set table colors
        self.cart_table.setStyleSheet(
            "QTableWidget::item:selected { background-color: #3b352d; }"
            "QHeaderView::section { background-color: #ff7d7d; }"
        )

        self.layout.addWidget(self.cart_table)

        # Create a horizontal layout for the total label
        total_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(total_layout)

        # Create the total label and set its properties
        self.total_label = QtWidgets.QLabel()
        font = self.total_label.font()
        font.setPointSize(14)
        font.setBold(True)
        self.total_label.setFont(font)
        total_layout.addStretch(1)
        total_layout.addWidget(self.total_label)
        total_layout.setAlignment(QtCore.Qt.AlignRight)

        # Create buttons for cart operations
        self.pay_button = QtWidgets.QPushButton("Check Out")
        self.remove_button = QtWidgets.QPushButton("Remove Item")
        self.mark_button = QtWidgets.QPushButton("Mark as Replacement")
        self.clear_button = QtWidgets.QPushButton("Clear Cart")
  
        self.layout.addWidget(self.pay_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.mark_button)
        self.layout.addWidget(self.clear_button)

        # Connect buttons to methods
        self.pay_button.clicked.connect(self.pay)
        self.remove_button.clicked.connect(self.remove_item)
        self.mark_button.clicked.connect(self.mark_return)
        self.clear_button.clicked.connect(self.clear_cart)

        # Connect itemSelectionChanged signal to handle row selection
        self.cart_table.itemSelectionChanged.connect(self.on_selection_changed)

    def update_total_label(self):
        total = sum(float(self.cart_table.item(row, 6).text()) for row in range(self.cart_table.rowCount()))
        self.total_label.setText(f"Total Price: PHP{total:.2f}")

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

        self.cart_table.setRowCount(len(products))
        self.cart_table.setColumnCount(7)
        self.cart_table.setHorizontalHeaderLabels(["RowID", "Product", "Brand", "Variation", "Size", "Quantity", "Total Price"])

        for i, product in enumerate(products):
            for j, value in enumerate(product):
                self.cart_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.resize_table()
        conn.close()
        self.cart_table.setColumnHidden(0, True)
        self.update_total_label()

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.cart_table.columnCount()):
                item = self.cart_table.item(row, column)
                if item:
                    item.setSelected(True)
        self.update_total_label()

    def search_cart(self):
        search_query = self.search_input.text()
        self.load_cart_items(search_query)
        self.update_total_label()

    def pay(self):
        from paymentForm import PaymentForm
        if not self.cart_table.rowCount():
            QMessageBox.warning(self, "No items", "Your cart is empty.")
            return
        
        total_price_str = self.total_label.text().replace("Total Price: PHP", "")
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
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_item = self.cart_table.item(row, 1)
            if product_item is not None:
                product_name = product_item.text()
                # Retrieve current quantity from the cart
                cursor.execute("SELECT qty FROM cart WHERE product_name = ?", (product_name,))
                current_qty_in_cart = cursor.fetchone()[0]
                # Update product quantity in the database
                cursor.execute("SELECT qty FROM products WHERE product_name = ?", (product_name,))
                current_qty_in_db = cursor.fetchone()[0]
                new_qty_in_db = current_qty_in_db + current_qty_in_cart
                cursor.execute("UPDATE products SET qty = ? WHERE product_name = ?", (new_qty_in_db, product_name))
                # Delete item from the cart
                cursor.execute("DELETE FROM cart WHERE product_name = ?", (product_name,))
        conn.commit()
        conn.close()
        self.load_cart_items()
        self.update_total_label()

    def mark_return(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_name_item = self.cart_table.item(row, 1)  
            if product_name_item is not None:
                product_name = product_name_item.text()
                # Update the status to "return" in the cart table
                cursor.execute("UPDATE cart SET status = 'return', total_price = 0 WHERE product_name =?", (product_name,))
                # Update the QTableWidget directly
                total_price_item = self.cart_table.item(row, 6)  # Column index for total price
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

        # Retrieve the next available log_id
        cursor.execute("SELECT IFNULL(MAX(log_id), 0) + 1 FROM user_logs")
        log_id_result = cursor.fetchone()
        if log_id_result:
            log_id = log_id_result[0]
        else:
            QMessageBox.warning(self, "Error", "Unable to determine next log ID!")
            conn.close()
            return
        
        for row in range(self.cart_table.rowCount()):
            product_name_item = self.cart_table.item(row, 1)
            brand_item = self.cart_table.item(row, 2)
            var_item = self.cart_table.item(row, 3)
            size_item = self.cart_table.item(row, 4)
            qty_item = self.cart_table.item(row, 5)
            total_price_item = self.cart_table.item(row, 6)

            if qty_item and qty_item.text():
                product_name = product_name_item.text()
                qty = int(qty_item.text())
                total_price = float(total_price_item.text())
                brand = brand_item.text() if brand_item.text() else None
                var = var_item.text() if var_item.text() else None
                size = size_item.text() if size_item.text() else None
                transaction_id = self.generate_transaction_id()

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
                    transaction_type = "returns"
                    # Insert return details into the returns table
                    return_id = self.generate_return_id()
                    cursor.execute('''
                        INSERT INTO returns (return_id, product_name, brand, var, size, qty, date, transaction_id)
                        VALUES (?,?,?,?,?,?,?,?)
                    ''', (return_id, product_name, brand, var, size, qty, current_date, transaction_id))
                else:
                    transaction_type = "purchase"

                cursor.execute('''
                    INSERT INTO transactions ( transaction_id, customer, product_name, qty, total_price, date, time, type, product_id, log_id, brand, var, size, user_id, payment_id, contact)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''', (transaction_id, customer_name, product_name, qty, total_price, current_date, current_time, transaction_type, product_id, log_id, brand, var, size, user_id, payment_id, contact))

                # Update the quantity in the products table
                cursor.execute("UPDATE products SET qty = qty - ? WHERE product_id = ?", (qty, product_id))

                # Insert into user_logs table
                action = "checkout"
                cursor.execute('''
                    INSERT INTO user_logs (user_id, action, time, date)
                    VALUES (?,?,?,?)
                ''', (user_id, action, current_time, current_date))

                transaction_successful = True
                log_id += 1  # Increment log_id for the next entry if there are multiple items

        conn.commit()
        conn.close()

        # Clear cart table
        self.clear_cart()

        # Display success message
        if transaction_successful:
            QMessageBox.information(self, "Checkout", "Checkout successful!")
        else:
            QMessageBox.warning(self, "Checkout", "Checkout failed. Some items were not processed.")



    def resize_table(self):
        header = self.cart_table.horizontalHeader()
        for i in range(1, self.cart_table.columnCount() - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.cart_table.columnCount() - 1, QtWidgets.QHeaderView.ResizeToContents)
