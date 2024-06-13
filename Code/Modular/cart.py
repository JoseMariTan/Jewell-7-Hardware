import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtWidgets, QtCore
import uuid

class CustomerNameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Name")
        self.layout = QVBoxLayout()
        self.label = QLabel("Enter customer name:")
        self.layout.addWidget(self.label)
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

    def get_customer_name(self):
        return self.line_edit.text()
    
class AddToCartDialog(QDialog):
    def __init__(self, parent=None, max_quantity=10):
        super().__init__(parent)
        self.setWindowTitle("Add to Cart")
        self.layout = QVBoxLayout()
        self.label = QLabel("Enter quantity:")
        self.layout.addWidget(self.label)
        self.spin_box = QSpinBox()
        self.spin_box.setMaximum(max_quantity)
        self.layout.addWidget(self.spin_box)
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.accept)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

    def get_quantity(self):
        return self.spin_box.value()

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
        self.remove_button = QtWidgets.QPushButton("Remove Item")
        self.clear_button = QtWidgets.QPushButton("Clear Cart")
        self.checkout_button = QtWidgets.QPushButton("Checkout")

        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.checkout_button)

        # Connect buttons to methods
        self.remove_button.clicked.connect(self.remove_item)
        self.clear_button.clicked.connect(self.clear_cart)
        self.checkout_button.clicked.connect(self.checkout)

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

    def remove_item(self):
        selected_rows = set()
        for item in self.cart_table.selectedItems():
            selected_rows.add(item.row())
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
        for row in selected_rows:
            product_item = self.cart_table.item(row, 0)
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
        
    def checkout(self):
        # Prompt user for customer name
        customer_dialog = CustomerNameDialog()
        if customer_dialog.exec_() == QDialog.Accepted:
            customer_name = customer_dialog.get_customer_name()

            # Get current date and time
            current_date = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime("%I:%M %p")

            #connect to db
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()

            # Use the stored user_id
            user_id = self.user_id
            
            # Generate a unique transaction_id using UUID
            transaction_id = str(uuid.uuid4())

            # Retrieve the next available log_id
            cursor.execute("SELECT IFNULL(MAX(log_id), 0) + 1 FROM user_logs")
            log_id_result = cursor.fetchone()
            if log_id_result:
                log_id = log_id_result[0]
            else:
                QMessageBox.warning(self, "Error", "Unable to determine next log ID!")
                conn.close()
                return
            
            transaction_successful = True
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

                    # Replace with actual transaction type logic
                    transaction_type = "purchase"
                    transaction_id = str(uuid.uuid4())

                    # Insert into transactions table
                    cursor.execute('''INSERT INTO transactions (transaction_id, customer, product_name, qty, total_price, date, time, type, product_id, log_id, brand, var, size, user_id)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                    (transaction_id, customer_name, product_name, qty, total_price, current_date, current_time, transaction_type, product_id, log_id, brand, var, size, user_id))

                    # Update the quantity in the products table
                    cursor.execute("UPDATE products SET qty = qty - ? WHERE product_id = ?", (qty, product_id))

                    # Insert into user_logs table
                    action = "checkout"
                    cursor.execute('''INSERT INTO user_logs (user_id, action, time, date)
                        VALUES (?,?,?,?)''',
                    (user_id, action, current_time, current_date))

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
            
        self.update_total_label()

    def resize_table(self):
        header = self.cart_table.horizontalHeader()
        for i in range(1, self.cart_table.columnCount() - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(self.cart_table.columnCount() - 1, QtWidgets.QHeaderView.ResizeToContents)
