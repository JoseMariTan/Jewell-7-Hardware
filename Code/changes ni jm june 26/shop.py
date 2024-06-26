import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

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
        
        self.button_layout = QHBoxLayout()
        
        self.min_button = QPushButton("Min (1)")
        self.min_button.setFixedWidth(50)
        self.min_button.clicked.connect(lambda: self.set_quantity(1))
        self.button_layout.addWidget(self.min_button)

        self.plus_5_button = QPushButton("+5")
        self.plus_5_button.setFixedWidth(50)
        self.plus_5_button.clicked.connect(lambda: self.adjust_quantity(5))
        self.button_layout.addWidget(self.plus_5_button)

        self.zero_button = QPushButton("0")
        self.zero_button.setFixedWidth(50)
        self.zero_button.clicked.connect(lambda: self.adjust_quantity(0))
        self.button_layout.addWidget(self.zero_button)
        
        self.plus_10_button = QPushButton("+10")
        self.plus_10_button.setFixedWidth(50)
        self.plus_10_button.clicked.connect(lambda: self.adjust_quantity(10))
        self.button_layout.addWidget(self.plus_10_button)
        
        self.max_button = QPushButton(f"Max ({max_quantity})")
        self.max_button.setFixedWidth(50)
        self.max_button.clicked.connect(lambda: self.set_quantity(max_quantity))
        self.button_layout.addWidget(self.max_button)
        
        self.layout.addLayout(self.button_layout)
        
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.accept)
        self.layout.addWidget(self.add_button)
        
        self.setLayout(self.layout)

    def set_quantity(self, quantity):
        self.spin_box.setValue(quantity)

    def adjust_quantity(self, adjustment):
        new_value = self.spin_box.value() + adjustment
        max_value = self.spin_box.maximum()
        self.spin_box.setValue(min(max(new_value, 0), max_value))

    def get_quantity(self):
        return self.spin_box.value()

class ShopTab(QtWidgets.QWidget):
    item_added_to_cart = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def load_products(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        try:
            if search_query:
                search_param = '%{}%'.format(search_query)
                exact_search_param = '{}'.format(search_query)
                cursor.execute("""
                    SELECT *
                    FROM products 
                    WHERE 
                        (product_name LIKE ? COLLATE NOCASE OR product_name = ?) OR
                        (brand LIKE ? COLLATE NOCASE OR brand = ?) OR
                        (var LIKE ? COLLATE NOCASE OR var = ?) OR
                        (size LIKE ? COLLATE NOCASE OR size = ?) OR
                        (price LIKE ? COLLATE NOCASE OR price = ?) OR
                        (qty LIKE ? COLLATE NOCASE OR qty = ?) OR
                        (category LIKE ? COLLATE NOCASE OR category = ?)
                        AND status = 'Available'
                    ORDER BY date_added DESC, time_added DESC
                """, (search_param, exact_search_param,
                    search_param, exact_search_param, search_param, exact_search_param,
                    search_param, exact_search_param, search_param, exact_search_param,
                    search_param, exact_search_param, search_param, exact_search_param,))
            else:
                cursor.execute("""
                    SELECT *
                    FROM products 
                    WHERE status = 'Available'
                    ORDER BY date_added DESC, time_added DESC
                    LIMIT 50
                """)

            rows = cursor.fetchall()
            self.tableWidget.setRowCount(len(rows))
            for row_number, row_data in enumerate(rows):
                self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))  # product
                self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))  # brand
                self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))  # var
                self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))  # size
                self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data[5])))  # price
                qty = row_data[6]  # qty
                threshold = row_data[7]  # threshold
                items_in_stock = qty - threshold if qty >= threshold else 0  # Ensure items_in_stock is non-negative
                self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(items_in_stock)))  # Items in Stock
                self.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(row_data[8])))  # category
        
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        
        finally:
            conn.close()

    def search_products(self):
        search_query = self.search_input.text()
        self.load_products(search_query)

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item:
                    item.setSelected(True)

    def initUI(self):
        self.setWindowTitle('Shop')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Search Component
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setFixedHeight(40) 
        self.search_input.setPlaceholderText("Search shop...")

        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setFixedHeight(40)
        self.search_button.clicked.connect(self.search_products)
        self.horizontalLayout.addWidget(self.search_input)
        self.horizontalLayout.addWidget(self.search_button)
        self.layout.addLayout(self.horizontalLayout)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(7) 
        self.tableWidget.setHorizontalHeaderLabels(['Product', 'Brand', 'Variation', 'Size', 'Price', 'Items in Stock', 'Category'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)

        # set table colors
        self.tableWidget.setStyleSheet(
            "QTableWidget::item:selected { background-color: #3b352d; }"
            "QHeaderView::section { background-color: #ff7d7d; }"
        )

        self.layout.addWidget(self.tableWidget)

        self.load_products()

        self.add_to_cart_button = QPushButton("Add to Cart")
        self.add_to_cart_button.clicked.connect(self.show_add_to_cart_dialog)
        self.layout.addWidget(self.add_to_cart_button)

        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)
        
    def add_to_cart(self, quantity):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        for row in selected_rows:
            product_item = self.tableWidget.item(row.row(), 0)  # Product name
            brand_item = self.tableWidget.item(row.row(), 1)  # Brand
            var_item = self.tableWidget.item(row.row(), 2)  # Variation
            size_item = self.tableWidget.item(row.row(), 3)  # Size
            price_item = self.tableWidget.item(row.row(), 4)  # Price
            qty_item = self.tableWidget.item(row.row(), 5)  # Items in stock

            if not all([product_item, qty_item, price_item]):
                QMessageBox.warning(self, "Error", "One or more fields are missing!")
                continue

            product_name = product_item.text()
            brand = brand_item.text() if brand_item else None
            var = var_item.text() if var_item else None
            size = size_item.text() if size_item else None
            price_text = price_item.text()
            qty_text = qty_item.text()

            if not all([product_name, price_text, qty_text]):
                QMessageBox.warning(self, "Error", "One or more fields have empty values!")
                continue

            try:
                current_qty = float(qty_text)
                price = float(price_text)
                new_qty = current_qty - quantity

                if new_qty >= 0:
                    # Update quantity in the database
                    conn = sqlite3.connect('j7h.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE products SET qty = ? WHERE product_name = ?", (new_qty, product_name))

                    # Calculate total price and prepare for cart insertion
                    total_price = quantity * price
                    log_id = 1  # Replace with actual log ID retrieval logic
                    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # Retrieve product ID
                    cursor.execute("""SELECT product_id FROM products 
                                    WHERE product_name = ? 
                                    AND (brand = ? OR brand IS NULL) 
                                    AND (var = ? OR var IS NULL) 
                                    AND (size = ? OR size IS NULL)""",
                                   (product_name, brand, var, size))
                    product_id_result = cursor.fetchone()

                    if product_id_result:
                        product_id = product_id_result[0]

                        # Insert into cart
                        cursor.execute('''INSERT INTO cart (product_name, qty, total_price, date, product_id, log_id, brand, var, size)
                                        VALUES (?,?,?,?,?,?,?,?,?)''',
                                       (product_name, quantity, total_price, date, product_id, log_id, brand, var, size))

                        conn.commit()

                        # Update UI and remove row if stock is depleted
                        if new_qty == 0:
                            # Update product status in the database
                            cursor.execute("UPDATE products SET status = 'Unavailable' WHERE product_name = ?", (product_name,))
                            self.tableWidget.removeRow(row.row())

                        self.item_added_to_cart.emit()
                    else:
                        QMessageBox.warning(self, "Error", f"Product ID not found for {product_name}, {brand}, {var}, {size}")

                    conn.close()
                else:
                    QMessageBox.warning(self, "Quantity Error", "Not enough items in stock.")
            except ValueError:
                QMessageBox.warning(self, "Value Error", "Invalid quantity or price.")
                continue

    def show_add_to_cart_dialog(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Selection Error", "Please select a product to add to the cart.")
            return

        max_quantity = float("inf")
        for row in selected_rows:
            qty_item = self.tableWidget.item(row.row(), 5)
            if qty_item is not None:
                try:
                    qty = float(qty_item.text())
                    max_quantity = min(max_quantity, qty)
                except ValueError:
                    pass

        if max_quantity == float("inf") or max_quantity == 0:
            QMessageBox.warning(self, "Quantity Error", "No valid quantity available.")
            return

        dialog = AddToCartDialog(max_quantity=int(max_quantity))
        if dialog.exec_() == QDialog.Accepted:
            quantity = dialog.get_quantity()
            if quantity > 0 and quantity <= max_quantity:
                self.add_to_cart(quantity)
            else:
                QMessageBox.warning(self, "Quantity Error", f"Quantity must be greater than zero and less than or equal to {max_quantity}.")
