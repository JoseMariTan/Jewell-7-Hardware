import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
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
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.accept)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

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
        cursor.execute("SELECT * FROM products WHERE qty > 0 ORDER BY product_id DESC")

        if search_query:
            query = """
                SELECT * FROM products 
                WHERE qty > 0 
                AND (product_name LIKE ? 
                OR brand LIKE ? 
                OR var LIKE ? 
                OR size LIKE ?
                OR category LIKE ?) 
                ORDER BY product_id DESC
                """
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        else:
            cursor.execute("SELECT * FROM products WHERE qty > 0 ORDER BY product_id DESC")

        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for row_number, row_data in enumerate(rows):
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))  # product
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))  # brand
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))  # var
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))  # size
            self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data[5])))  # price
            qty = row_data[6]  # qty
            self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(qty)))  # Convert qty to string before setting it as text
            self.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(row_data[7])))  # category
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
                QtWidgets.QMessageBox.warning(self, "Error", "One or more fields are missing!")
                continue

            product_name = product_item.text()
            brand = brand_item.text() if brand_item else None
            var = var_item.text() if var_item else None
            size = size_item.text() if size_item else None
            price_text = price_item.text()
            qty_text = qty_item.text()

            if not all([product_name, price_text, qty_text]):
                QtWidgets.QMessageBox.warning(self, "Error", "One or more fields have empty values!")
                continue

            try:
                current_qty = float(qty_text)
                price = float(price_text)
                new_qty = current_qty - quantity

                if new_qty >= 0:
                    qty_item.setText(str(int(new_qty)))
                    conn = sqlite3.connect('j7h.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE products SET qty = ? WHERE product_name = ?", (new_qty, product_name))

                    total_price = quantity * price
                    log_id = 1  # Replace with actual log ID retrieval logic
                    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    cursor.execute("""SELECT product_id FROM products 
                                    WHERE product_name = ? 
                                    AND (brand = ? OR brand IS NULL) 
                                    AND (var = ? OR var IS NULL) 
                                    AND (size = ? OR size IS NULL)""",
                                (product_name, brand, var, size))
                    product_id_result = cursor.fetchone()

                    if product_id_result:
                        product_id = product_id_result[0]

                        cursor.execute('''INSERT INTO cart (product_name, qty, total_price, date, product_id, log_id, brand, var, size)
                                        VALUES (?,?,?,?,?,?,?,?,?)''',
                                    (product_name, quantity, total_price, date, product_id, log_id, brand, var, size))

                        conn.commit()

                        if new_qty == 0:
                            self.tableWidget.removeRow(row.row())

                        self.item_added_to_cart.emit()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", f"Product ID not found for {product_name}, {brand}, {var}, {size}")

                    conn.close()
                else:
                    QtWidgets.QMessageBox.warning(self, "Quantity Error", "Not enough items in stock.")
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Value Error", "Invalid quantity or price.")
                continue


    def show_add_to_cart_dialog(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        if selected_rows:
            max_quantity = float("inf")
            for row in selected_rows:
                qty_item = self.tableWidget.item(row, 5)
                if qty_item is not None:
                    try:
                        qty = float(qty_item.text())
                        max_quantity = min(max_quantity, qty)
                    except ValueError:
                        pass
            if max_quantity == float("inf"):
                max_quantity = 0  # Handle the case where no valid quantity is found
            dialog = AddToCartDialog(max_quantity=int(max_quantity))
            if dialog.exec_() == QDialog.Accepted:
                quantity = dialog.get_quantity()
                if quantity > 0:  # Ensure that the quantity is valid before adding to cart
                    self.add_to_cart(quantity)
                else:
                    QtWidgets.QMessageBox.warning(self, "Quantity Error", "Quantity must be greater than zero.")
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a product to add to the cart.")