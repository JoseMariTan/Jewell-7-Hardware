import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

#Class for Products Tab
class ProductsTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_data()
        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)

    def setup_ui(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
    
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
    
        self.search_input = QtWidgets.QLineEdit(self)
        self.search_input.setFixedHeight(40) 
        self.search_input.setPlaceholderText("Search products...")
        self.horizontalLayout_2.addWidget(self.search_input)
        

        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setFixedHeight(40)  # Match the shop tab's search button height
        self.search_button.clicked.connect(self.search_products)
        self.horizontalLayout_2.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
    
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.tableWidget = QtWidgets.QTableWidget()
        
        self.tableWidget.setFixedHeight(self.tableWidget.verticalHeader().defaultSectionSize() * 30)  # Adjust multiplier as needed
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
    
        # Ensure consistent border and frame shape
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setStyleSheet("QTableWidget { border: none; }")  # Ensure no border
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
        self.scrollArea.setWidget(self.tableWidget)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
    
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.addProduct_button = QtWidgets.QPushButton()
        self.addProduct_button.setIcon(QtGui.QIcon("plus_icon.png"))
        self.addProduct_button.setFont(font)
        self.addProduct_button.setFixedHeight(40)  # Adjust height as needed
        self.addProduct_button.clicked.connect(self.open_add_product_dialog)
        self.horizontalLayout_5.addWidget(self.addProduct_button)
    
        self.modifyProduct_button = QtWidgets.QPushButton()
        self.modifyProduct_button.setIcon(QtGui.QIcon("edit_icon.png"))
        self.modifyProduct_button.setFont(font)
        self.modifyProduct_button.setFixedHeight(40)  # Adjust height as needed
        self.modifyProduct_button.clicked.connect(self.open_modify_product_dialog)
        self.horizontalLayout_5.addWidget(self.modifyProduct_button)
    
        self.voidProduct_button = QtWidgets.QPushButton()
        self.voidProduct_button.setIcon(QtGui.QIcon("bin_icon.png"))
        self.voidProduct_button.setFont(font)
        self.voidProduct_button.setFixedHeight(40)  # Adjust height as needed
        self.voidProduct_button.clicked.connect(self.void_product)
        self.horizontalLayout_5.addWidget(self.voidProduct_button)
    
        self.verticalLayout.addLayout(self.horizontalLayout_5)


    def apply_stock_alert(self, row, column, color):
        item = self.tableWidget.item(row, column)
        if item is not None:
            item.setBackground(QtGui.QColor(color))

    def stock_alert(self):
        for row in range(self.tableWidget.rowCount()):
            qty_item = self.tableWidget.item(row, 6)
            if qty_item is not None:
                try:
                    qty = float(qty_item.text())
                    if qty <= 5:
                        self.apply_stock_alert(row, 6, "#ffcccc")
                    elif 5 < qty < 15:
                        self.apply_stock_alert(row, 6, "#ffcc99")
                    else:
                        self.apply_stock_alert(row, 6, "#ccffcc")
                except ValueError:
                    self.apply_stock_alert(row, 6, "#ffffff")

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        if search_query:
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty, category FROM products WHERE "
                        "product_name LIKE ? OR brand LIKE ? OR var LIKE ? OR size LIKE ? OR category LIKE ? ORDER BY product_id DESC",
                        ('%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            cur.execute("SELECT rowid, product_name, brand, var, size, price, qty, category FROM products ORDER BY product_id DESC")

        products = cur.fetchall()
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['RowID', 'Product', 'Brand', 'Variation', 'Size', 'Price', 'Items in Stock', 'Category'])

        for i, product in enumerate(products):
            for j, value in enumerate(product):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))


        conn.close()
        self.tableWidget.setColumnHidden(0, True)
        self.stock_alert()

    def on_selection_changed(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        for row in selected_rows:
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item:
                    item.setSelected(True)

    def search_products(self):
        search_query = self.search_input.text()
        self.load_data(search_query)

    def open_add_product_dialog(self):
        dialog = AddProductDialog(self)
        dialog.exec_()
        self.load_data()

    def open_modify_product_dialog(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product to modify.")
            return

        row = selected_items[0].row()
        rowid = self.tableWidget.item(row, 0).text()
        product_name = self.tableWidget.item(row, 1).text()
        brand = self.tableWidget.item(row, 2).text()
        var = self.tableWidget.item(row, 3).text()
        size = self.tableWidget.item(row, 4).text()
        price = self.tableWidget.item(row, 5).text()
        qty = self.tableWidget.item(row, 6).text()
        category = self.tableWidget.item(row, 7).text()

        dialog = ModifyProductDialog(parent=self, rowid=rowid, product_name=product_name, brand=brand, var=var, size=size, price=price, qty=qty, category=category)
        dialog.exec_()
        self.load_data()

    def void_product(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product to void.")
            return

        row = selected_items[0].row()
        rowid = self.tableWidget.item(row, 0).text()
        
        confirmation = QtWidgets.QMessageBox.question(self, "Confirm Deletion",
                                                    "Are you sure you want to void this product?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if confirmation == QtWidgets.QMessageBox.Yes:
            conn = sqlite3.connect('j7h.db')
            cur = conn.cursor()

            # Delete the product
            cur.execute("DELETE FROM products WHERE rowid=?", (rowid,))
            conn.commit()
            conn.close()
            self.load_data()
            QtWidgets.QMessageBox.information(self, "Success", "Product successfully voided.")

class AddProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Product Management")
        self.setGeometry(100, 100, 300, 200)
        layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name: *")
        self.product_name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand:")
        self.brand_input = QtWidgets.QLineEdit()
        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var:")
        self.var_input = QtWidgets.QLineEdit()
        layout.addWidget(self.var_label)
        layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size:")
        self.size_input = QtWidgets.QLineEdit()
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price: *")
        self.price_input = QtWidgets.QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty: *")
        self.qty_input = QtWidgets.QLineEdit()
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        self.category_label = QtWidgets.QLabel("Category: *")
        self.category_input = QtWidgets.QLineEdit()
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_input)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        
    def add_product(self):
        product_name = self.product_name_input.text().strip()
        brand = self.brand_input.text().strip() or "None"
        var = self.var_input.text().strip() or "None"
        size = self.size_input.text().strip() or "None"
        price = self.price_input.text().strip()
        qty = self.qty_input.text().strip()
        category = self.category_input.text().strip()

        # Check for required fields
        if not product_name or not price or not qty or not category:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all required fields *.")
            return

        # Validate that price and qty are numeric
        try:
            float(price)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
            return

        try:
            int(qty)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Qty must be a valid integer.")
            return

        # Insert the new product into the database
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO products (product_name, brand, var, size, price, qty, category) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (product_name, brand, var, size, price, qty, category))
        
        conn.commit()
        conn.close()

        self.accept()

class ModifyProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, rowid=None, product_name=None, brand=None, var=None, size=None, price=None, qty=None, category=None):
        super().__init__(parent)
        self.setWindowTitle("Modify Product")
        self.setGeometry(100, 100, 300, 200)
        self.rowid = rowid

        layout = QtWidgets.QVBoxLayout()

        self.product_name_label = QtWidgets.QLabel("Product Name: *")
        self.product_name_input = QtWidgets.QLineEdit(product_name)
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        self.brand_label = QtWidgets.QLabel("Brand:")
        self.brand_input = QtWidgets.QLineEdit(brand)
        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_input)

        self.var_label = QtWidgets.QLabel("Var:")
        self.var_input = QtWidgets.QLineEdit(var)
        layout.addWidget(self.var_label)
        layout.addWidget(self.var_input)

        self.size_label = QtWidgets.QLabel("Size:")
        self.size_input = QtWidgets.QLineEdit(size)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        self.price_label = QtWidgets.QLabel("Price: *")
        self.price_input = QtWidgets.QLineEdit(price)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty: *")
        self.qty_input = QtWidgets.QLineEdit(qty)
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        self.category_label = QtWidgets.QLabel("Category: *")
        self.category_input = QtWidgets.QLineEdit(category)
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_input)

        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_product)
        layout.addWidget(self.modify_button)

        self.setLayout(layout)
        self.fetch_product_id()

    def fetch_product_id(self):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM products WHERE rowid=?", (self.rowid,))
        result = cur.fetchone()
        if result:
            self.product_id = result[0]
        conn.close()

    def modify_product(self):
        if self.product_id is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Product ID not found!")
            return
        
        product_name = self.product_name_input.text().strip()
        brand = self.brand_input.text().strip() or "None"
        var = self.var_input.text().strip() or "None"
        size = self.size_input.text().strip() or "None"
        price = self.price_input.text().strip()
        qty = self.qty_input.text().strip()
        category = self.category_input.text().strip()

        # Check for required fields
        if not product_name or not price or not qty or not category:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all required fields *")
            return

        # Validate that price and qty are numeric
        try:
            float(price)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
            return

        try:
            int(qty)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Qty must be a valid integer.")
            return

        # Update the product in the database
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        cur.execute("UPDATE products SET product_name=?, brand=?, var=?, size=?, price=?, qty=?, category=? WHERE rowid=?",
                (product_name, brand, var, size, price, qty, category, self.rowid))
        
        conn.commit()
        conn.close()

        self.accept()

    