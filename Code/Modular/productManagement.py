import sqlite3
import random
import string
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from assets import shop_rc

#Class for Products Tab
class ProductsTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_data()
        self.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)

    def setup_ui(self):
        self.setObjectName("ProductsTab")
        self.resize(1722, 741)
        self.setStyleSheet("background-color:#fff;")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.search_button = QtWidgets.QPushButton(self)
        self.search_button.setMinimumSize(QtCore.QSize(50, 50))
        self.search_button.setMaximumSize(QtCore.QSize(50, 50))
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #f6f4f4;
                border-radius: 25px;
                color: black;
            }
            QPushButton::pressed {
                background-color: #fff;
            }
            QPushButton:hover {
                background-color: #81cdc6;
                transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
                color: #fff;
            }
            border: none;
        """)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/search/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(20, 20))
        self.search_button.clicked.connect(self.search_products)
        self.horizontalLayout_2.addWidget(self.search_button)

        self.search_input = QtWidgets.QLineEdit(self)
        self.search_input.setMinimumSize(QtCore.QSize(300, 50))
        self.search_input.setMaximumSize(QtCore.QSize(600, 75))
        self.search_input.setStyleSheet("border-radius: 25px; padding: 0 10px; background-color: #f6f4f4;")
        self.search_input.setPlaceholderText("Search products...")
        self.horizontalLayout_2.addWidget(self.search_input)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QtWidgets.QTableWidget(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels([
            "Product ID", "Product", "Brand", "Variation", "Size",
            "Price", "Stock", "Threshold", "Category", "Status", "Supplier"
        ])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #88ccc4; }")
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(290, -1, 290, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        font_button = QtGui.QFont()
        font_button.setFamily("Segoe UI")
        font_button.setPointSize(8)
        font_button.setBold(True)
        font_button.setWeight(75)

        self.add_button = QtWidgets.QPushButton("Add", self)
        self.add_button.setMinimumSize(QtCore.QSize(175, 50))
        self.add_button.setMaximumSize(QtCore.QSize(350, 60))
        self.add_button.setFont(font_button)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #10cc94;
                border-radius: 12px;
                color: #fff;
            }
            QPushButton::pressed {
                background-color: #fff;
            }
            QPushButton:hover {
                background-color: #0a9c73;
                transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            }
            border: none;
        """)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(22, 22))
        self.add_button.clicked.connect(self.open_add_product_dialog)
        self.horizontalLayout.addWidget(self.add_button)

        self.modify_button = QtWidgets.QPushButton("Modify", self)
        self.modify_button.setMinimumSize(QtCore.QSize(175, 50))
        self.modify_button.setMaximumSize(QtCore.QSize(350, 60))
        self.modify_button.setFont(font_button)
        self.modify_button.setStyleSheet("""
            QPushButton {
                background-color: #10cc94;
                border-radius: 12px;
                color: #fff;
            }
            QPushButton::pressed {
                background-color: #fff;
            }
            QPushButton:hover {
                background-color: #0a9c73;
                transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            }
            border: none;
        """)
        self.modify_button.setIcon(icon1)
        self.modify_button.setIconSize(QtCore.QSize(22, 22))
        self.modify_button.clicked.connect(self.open_modify_product_dialog)
        self.horizontalLayout.addWidget(self.modify_button)

        self.changeStatus_button = QtWidgets.QPushButton("Change Status", self)
        self.changeStatus_button.setMinimumSize(QtCore.QSize(175, 50))
        self.changeStatus_button.setMaximumSize(QtCore.QSize(350, 60))
        self.changeStatus_button.setFont(font_button)
        self.changeStatus_button.setStyleSheet("""
            QPushButton {
                background-color: #5698d2;
                border-radius: 12px;
                color: #fff;
            }
            QPushButton::pressed {
                background-color: #fff;
            }
            QPushButton:hover {
                background-color: #4379a5;
                transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            }
            border: none;
        """)
        self.changeStatus_button.setIcon(icon1)
        self.changeStatus_button.setIconSize(QtCore.QSize(22, 22))
        self.changeStatus_button.clicked.connect(self.product_status)
        self.horizontalLayout.addWidget(self.changeStatus_button)

        spacerItem3 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

    def product_status(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product to change status.")
            return

        row = selected_items[0].row()
        rowid = self.tableWidget.item(row, 0).text()

        dialog = CustomDialog(self)
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            new_status = dialog.get_selected_status()
            if new_status:
                conn = sqlite3.connect('j7h.db')
                cur = conn.cursor()
                cur.execute("UPDATE products SET status=? WHERE rowid=?", (new_status, rowid))
                conn.commit()
                conn.close()
                self.load_data()
                QtWidgets.QMessageBox.information(self, "Success", f"Product status successfully updated to {new_status}.")
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Please select a status before proceeding.")
        else:
            QtWidgets.QMessageBox.information(self, "Cancelled", "Operation cancelled.")

    def apply_stock_alert(self, row, column, color):
        item = self.tableWidget.item(row, column)
        if item is not None:
            item.setBackground(QtGui.QColor(color))

    def stock_alert(self):
        for row in range(self.tableWidget.rowCount()):
            qty_item = self.tableWidget.item(row, 7)
            threshold_item = self.tableWidget.item(row, 8)
            if qty_item is not None and threshold_item is not None:
                try:
                    qty = float(qty_item.text())
                    threshold = float(threshold_item.text())
                    if qty - threshold <= 5:
                        self.apply_stock_alert(row, 7, "#ffcccc")
                    elif 5 < qty - threshold < 15:
                        self.apply_stock_alert(row, 7, "#ffcc99")
                    else:
                        self.apply_stock_alert(row, 7, "#ccffcc")
                except ValueError:
                    self.apply_stock_alert(row, 7, "#ffffff")

    def load_data(self, search_query=None):
        conn = sqlite3.connect('j7h.db')
        cur = conn.cursor()

        try:
            if search_query:
                search_param = '%{}%'.format(search_query)
                exact_search_param = '{}'.format(search_query)
                cur.execute("""
                    SELECT rowid, product_id, product_name, brand, var, size, price, qty, threshold, category, status, date_added, time_added, supplier 
                    FROM products 
                    WHERE 
                        (product_id LIKE ? COLLATE NOCASE OR product_id = ?) OR
                        (product_name LIKE ? COLLATE NOCASE OR product_name = ?) OR
                        (brand LIKE ? COLLATE NOCASE OR brand = ?) OR
                        (var LIKE ? COLLATE NOCASE OR var = ?) OR
                        (size LIKE ? COLLATE NOCASE OR size = ?) OR
                        (category LIKE ? COLLATE NOCASE OR category = ?) OR
                        (status LIKE ? COLLATE NOCASE OR status = ?) OR
                        (date_added LIKE ? COLLATE NOCASE OR date_added = ?) OR
                        (supplier LIKE ? COLLATE NOCASE OR supplier = ?)
                    ORDER BY date_added DESC, time_added DESC
                """, (search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param))
            else:
                cur.execute("""
                    SELECT rowid, product_id, product_name, brand, var, size, price, qty, threshold, category, status, date_added, time_added, supplier 
                    FROM products 
                    ORDER BY date_added DESC, time_added DESC
                    LIMIT 50
                """)

            products = cur.fetchall()

            if not products:
                QtWidgets.QMessageBox.information(self, "No Data Found", "No data found.")
                return
        
            self.tableWidget.setRowCount(len(products))
            self.tableWidget.setColumnCount(14)
            self.tableWidget.setHorizontalHeaderLabels(['RowID', 'Product ID', 'Product', 'Brand', 'Variation', 'Size', 'Price', 'Stock', 'Threshold', 'Category', 'Status', 'Date Added', 'Time Added', 'Supplier'])

            for row_number, row_data in enumerate(products):
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignLeft)
                    self.tableWidget.setItem(row_number, column_number, item)

        except sqlite3.Error as e:
            print("SQLite error:", e)
            QtWidgets.QMessageBox.critical(self, "Database Error", "Failed to load data. Please try again.")

        finally:
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
class AddProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Product Management")
        self.setGeometry(100, 100, 300, 400)  # Adjust dimensions as needed for additional fields
        layout = QtWidgets.QVBoxLayout()

        # Product ID input field
        self.product_id_label = QtWidgets.QLabel("Product ID:")
        self.product_id_input = QtWidgets.QLineEdit()
        self.product_id_input.setReadOnly(True)  # Make the input field read-only
        self.product_id_input.setText(self.generate_product_id())  # Set the generated product ID
        layout.addWidget(self.product_id_label)
        layout.addWidget(self.product_id_input)

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
        self.price_input.setValidator(QtGui.QDoubleValidator(decimals=2))  # Set validator for 2 decimal places
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.qty_label = QtWidgets.QLabel("Qty: *")
        self.qty_input = QtWidgets.QLineEdit()
        self.qty_input.setValidator(QtGui.QIntValidator())  # Set validator for integers
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        # Using QComboBox for Category with unique values from database
        self.category_label = QtWidgets.QLabel("Category: *")
        self.category_combobox = QtWidgets.QComboBox()
        self.category_combobox.addItem("")  # Add empty value
        self.populate_category_combobox()  # Populate the combobox with unique values
        self.new_category_checkbox = QtWidgets.QCheckBox("New Category")
        self.new_category_input = QtWidgets.QLineEdit()
        self.new_category_input.setEnabled(False)  # Initially disabled

        self.new_category_checkbox.stateChanged.connect(self.toggle_new_category_input)

        category_layout = QtWidgets.QHBoxLayout()
        category_layout.addWidget(self.category_combobox)
        category_layout.addWidget(self.new_category_checkbox)
        layout.addWidget(self.category_label)
        layout.addLayout(category_layout)
        layout.addWidget(self.new_category_input)

        self.threshold_label = QtWidgets.QLabel("Threshold:")
        self.threshold_spinbox = QtWidgets.QSpinBox()
        self.threshold_spinbox.setValue(5)  # Set initial value
        self.threshold_spinbox.setMinimum(0)  # Set minimum value
        self.threshold_spinbox.setMaximum(1000)  # Set maximum value
        layout.addWidget(self.threshold_label)
        layout.addWidget(self.threshold_spinbox)

        # New field for Status using radio buttons
        self.status_label = QtWidgets.QLabel("Status: *")
        self.available_radio = QtWidgets.QRadioButton("Available")
        self.unavailable_radio = QtWidgets.QRadioButton("Unavailable")
        self.available_radio.setChecked(True)  # Default selection
        self.status_group = QtWidgets.QButtonGroup(self)
        self.status_group.addButton(self.available_radio)
        self.status_group.addButton(self.unavailable_radio)
        
        status_layout = QtWidgets.QHBoxLayout()
        status_layout.addWidget(self.available_radio)
        status_layout.addWidget(self.unavailable_radio)
        
        layout.addWidget(self.status_label)
        layout.addLayout(status_layout)

        # Supplier input field (moved to the bottom)
        self.supplier_label = QtWidgets.QLabel("Supplier:")
        self.supplier_input = QtWidgets.QLineEdit()
        layout.addWidget(self.supplier_label)
        layout.addWidget(self.supplier_input)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        self.setLayout(layout)


    def generate_product_id(self):
        # Establishing connection with SQLite database
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()
    
        try:
            while True:
                # Get the current date in the format YYYYMMDD
                current_date = datetime.now().strftime("%Y%m%d")
            
                # Generate three random letters from A to Z
                random_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            
                # Combine the parts to form the product ID
                product_id = f"PRODUC{current_date}{random_letters}"
            
                # Check if the product ID already exists in the database
                cursor.execute("SELECT 1 FROM products WHERE product_id = ?", (product_id,))
                if not cursor.fetchone():
                    return product_id
        finally:
            # Ensure the database connection is closed
            conn.close()

    def populate_category_combobox(self):
        # Assuming SQLite database connection and fetching unique values from 'transactions' table
        try:
            connection = sqlite3.connect('j7h.db')  # Replace with your database path
            cursor = connection.cursor()
            cursor.execute("SELECT DISTINCT category FROM transactions")
            categories = cursor.fetchall()
            for category in categories:
                self.category_combobox.addItem(category[0])  # Assuming category is the first column
        except sqlite3.Error as error:
            print("Error while connecting to SQLite", error)
        finally:
            if connection:
                connection.close()

    def toggle_new_category_input(self, state):
        if state == QtCore.Qt.Checked:
            self.new_category_input.setEnabled(True)
            self.category_combobox.setEnabled(False)
            self.category_combobox.setCurrentIndex(0)  # Reset combobox selection
        else:
            self.new_category_input.setEnabled(False)
            self.category_combobox.setEnabled(True)

    def add_product(self):
        # Implement the functionality to handle adding a product here
        product_id = self.product_id_input.text().strip()
        product_name = self.product_name_input.text().strip()
        brand = self.brand_input.text().strip() or "-"
        var = self.var_input.text().strip() or "-"
        size = self.size_input.text().strip() or "-"
        price_text = self.price_input.text().strip()
        qty_text = self.qty_input.text().strip()
        category = self.category_combobox.currentText().strip()
        supplier = self.supplier_input.text().strip() or "-"
        if self.new_category_checkbox.isChecked():
            new_category = self.new_category_input.text().strip()
            if new_category:
                category = new_category
        
        threshold = self.threshold_spinbox.value()
        # Determine the status based on radio button selection
        if self.available_radio.isChecked():
            status = "Available"
        elif self.unavailable_radio.isChecked():
            status = "Unavailable"
        else:
            status = ""  # Handle if neither is checked, though one should always be checked in this setup

        # Validate input
        if not product_name or not price_text or not qty_text or not category:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all required fields *.")
            return

        # Validate that price and qty are numeric
        try:
            price = float(price_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
            return

        try:
            qty = int(qty_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Qty must be a valid integer.")
            return

        # Check if a status is selected
        if not self.available_radio.isChecked() and not self.unavailable_radio.isChecked():
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please select a Status (Available/Unavailable).")
            return

        current_datetime = datetime.today()
        date_log = current_datetime.strftime('%Y-%m-%d')
        time_log = current_datetime.strftime("%I:%M %p")

        # Insert the new product into the database
        try:
            conn = sqlite3.connect('j7h.db')  # Replace with your database path
            cur = conn.cursor()
            cur.execute("""INSERT INTO products (product_id, product_name, brand, var, size, price, qty, category, threshold, status, time_added, date_added, supplier) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (product_id, product_name, brand, var, size, price, qty, category, threshold, status, time_log, date_log, supplier))
            conn.commit()

            # Success message
            QtWidgets.QMessageBox.information(self, "Success", "Product added successfully.")

        except sqlite3.Error as error:
            print("Error while connecting to SQLite", error)
            QtWidgets.QMessageBox.critical(self, "Database Error", "Failed to add product. Please try again.")

        finally:
            if conn:
                conn.close()
        self.accept()

class ModifyProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, rowid=None, product_id=None, product_name=None, brand=None, var=None, size=None, price=None, qty=None, category=None, threshold=None, status=None, supplier=None):
        super().__init__(parent)
        self.setWindowTitle("Modify Product")
        self.setGeometry(100, 100, 300, 400)  # Adjust dimensions for additional fields if needed
        self.rowid = rowid

        layout = QtWidgets.QVBoxLayout()

        # Product ID input field (read-only)
        self.product_id_label = QtWidgets.QLabel("Product ID:")
        self.product_id_input = QtWidgets.QLineEdit(product_id)
        self.product_id_input.setReadOnly(True)
        layout.addWidget(self.product_id_label)
        layout.addWidget(self.product_id_input)

        # Product Name input field
        self.product_name_label = QtWidgets.QLabel("Product Name: *")
        self.product_name_input = QtWidgets.QLineEdit(product_name)
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_input)

        # Brand input field
        self.brand_label = QtWidgets.QLabel("Brand:")
        self.brand_input = QtWidgets.QLineEdit(brand)
        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_input)

        # Var input field
        self.var_label = QtWidgets.QLabel("Var:")
        self.var_input = QtWidgets.QLineEdit(var)
        layout.addWidget(self.var_label)
        layout.addWidget(self.var_input)

        # Size input field
        self.size_label = QtWidgets.QLabel("Size:")
        self.size_input = QtWidgets.QLineEdit(size)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        # Price input field
        self.price_label = QtWidgets.QLabel("Price: *")
        self.price_input = QtWidgets.QLineEdit(price)
        self.price_input.setValidator(QtGui.QDoubleValidator(decimals=2))  # Set validator for 2 decimal places
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        # Qty input field
        self.qty_label = QtWidgets.QLabel("Qty: *")
        self.qty_input = QtWidgets.QLineEdit(qty)
        self.qty_input.setValidator(QtGui.QIntValidator())  # Set validator for integers
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)

        # Category input field (using QComboBox and checkbox for new category)
        self.category_label = QtWidgets.QLabel("Category: *")
        self.category_combobox = QtWidgets.QComboBox()
        self.category_combobox.addItem("")  # Add empty value
        self.populate_category_combobox()  # Populate the combobox with unique values
        self.new_category_checkbox = QtWidgets.QCheckBox("New Category")
        self.new_category_input = QtWidgets.QLineEdit()
        self.new_category_input.setEnabled(False)  # Initially disabled

        self.new_category_checkbox.stateChanged.connect(self.toggle_new_category_input)

        category_layout = QtWidgets.QHBoxLayout()
        category_layout.addWidget(self.category_combobox)
        category_layout.addWidget(self.new_category_checkbox)
        layout.addWidget(self.category_label)
        layout.addLayout(category_layout)
        layout.addWidget(self.new_category_input)

        # Threshold input field
        self.threshold_label = QtWidgets.QLabel("Threshold:")
        self.threshold_spinbox = QtWidgets.QSpinBox()
        self.threshold_spinbox.setMinimum(0)  # Set minimum value
        self.threshold_spinbox.setMaximum(1000)  # Set maximum value
        if threshold is not None:
            self.threshold_spinbox.setValue(threshold)
        layout.addWidget(self.threshold_label)
        layout.addWidget(self.threshold_spinbox)

        # Status input field (radio buttons)
        self.status_label = QtWidgets.QLabel("Status: *")
        self.available_radio = QtWidgets.QRadioButton("Available")
        self.unavailable_radio = QtWidgets.QRadioButton("Unavailable")
        if status == "Available":
            self.available_radio.setChecked(True)
        else:
            self.unavailable_radio.setChecked(True)
        status_layout = QtWidgets.QHBoxLayout()
        status_layout.addWidget(self.available_radio)
        status_layout.addWidget(self.unavailable_radio)
        layout.addWidget(self.status_label)
        layout.addLayout(status_layout)

        # Supplier input field
        self.supplier_label = QtWidgets.QLabel("Supplier:")
        self.supplier_input = QtWidgets.QLineEdit(supplier)
        layout.addWidget(self.supplier_label)
        layout.addWidget(self.supplier_input)

        # Modify button
        self.modify_button = QtWidgets.QPushButton("Modify")
        self.modify_button.clicked.connect(self.modify_product)
        layout.addWidget(self.modify_button)

        self.setLayout(layout)

        self.fetch_product_details()

    def populate_category_combobox(self):
        try:
            conn = sqlite3.connect('j7h.db')
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT category FROM products")
            categories = cur.fetchall()
            for category in categories:
                self.category_combobox.addItem(category[0])
        except sqlite3.Error as e:
            print("Error fetching categories:", e)
        finally:
            if conn:
                conn.close()

    def toggle_new_category_input(self, checked):
        self.new_category_input.setEnabled(checked)
        if not checked:
            self.new_category_input.clear()

    def fetch_product_details(self):
        try:
            conn = sqlite3.connect('j7h.db')
            cur = conn.cursor()
            cur.execute("SELECT product_id, product_name, brand, var, size, price, qty, category, threshold, status, supplier FROM products WHERE rowid=?", (self.rowid,))
            result = cur.fetchone()
            if result:
                product_id, product_name, brand, var, size, price, qty, category, threshold, status, supplier = result
                self.product_id_input.setText(product_id)
                self.product_name_input.setText(product_name)
                self.brand_input.setText(brand)
                self.var_input.setText(var)
                self.size_input.setText(size)
                self.price_input.setText(str(price))
                self.qty_input.setText(str(qty))
                self.threshold_spinbox.setValue(threshold if threshold is not None else 0)
                self.supplier_input.setText(supplier)

                # Set category in combobox or new category input
                if category:
                    if category in [self.category_combobox.itemText(i) for i in range(self.category_combobox.count())]:
                        self.category_combobox.setCurrentText(category)
                        self.new_category_checkbox.setChecked(False)
                        self.new_category_input.setEnabled(False)
                    else:
                        self.category_combobox.setEditText(category)
                        self.new_category_checkbox.setChecked(True)
                        self.new_category_input.setEnabled(True)
                        self.new_category_input.setText(category)
                else:
                    self.category_combobox.setCurrentIndex(-1)
                    self.new_category_checkbox.setChecked(False)
                    self.new_category_input.setEnabled(False)

                # Set status
                if status == "Available":
                    self.available_radio.setChecked(True)
                else:
                    self.unavailable_radio.setChecked(True)
        except sqlite3.Error as e:
            print("Error fetching product details:", e)
        finally:
            if conn:
                conn.close()

    def modify_product(self):
        product_name = self.product_name_input.text().strip()
        brand = self.brand_input.text().strip() or "-"
        var = self.var_input.text().strip() or "-"
        size = self.size_input.text().strip() or "-"
        price_text = self.price_input.text().strip()
        qty_text = self.qty_input.text().strip()
        category = self.category_combobox.currentText().strip()
        if self.new_category_checkbox.isChecked():
            new_category = self.new_category_input.text().strip()
            if new_category:
                category = new_category
        
        threshold = self.threshold_spinbox.value()
        supplier = self.supplier_input.text().strip() or "-"

        # Validate input
        if not product_name or not price_text or not qty_text or not category:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all required fields *.")
            return

        # Validate that price and qty are numeric
        try:
            price = float(price_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
            return

        try:
            qty = int(qty_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Qty must be a valid integer.")
            return
        
        if threshold == 0:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Invalid threshold value.")
            return

        # Check if a status is selected
        if not self.available_radio.isChecked() and not self.unavailable_radio.isChecked():
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please select a Status (Available/Unavailable).")
            return

        # Determine the status based on radio button selection
        if self.available_radio.isChecked():
            status = "Available"
        else:
            status = "Unavailable"

        # Update the product in the database
        try:
            conn = sqlite3.connect('j7h.db')  # Replace with your database path
            cur = conn.cursor()

            # Set status based on qty and threshold
            if qty <= threshold:
                status = "Unavailable"

            cur.execute("""
                UPDATE products 
                SET product_name=?, brand=?, var=?, size=?, price=?, qty=?, category=?, threshold=?, status=?, supplier=? 
                WHERE rowid=?""",
                (product_name, brand, var, size, price, qty, category, threshold, status, supplier, self.rowid)
            )
            conn.commit()

            # Success message
            QtWidgets.QMessageBox.information(self, "Success", "Product modified successfully.")

        except sqlite3.Error as error:
            print("Error while connecting to SQLite", error)
            QtWidgets.QMessageBox.critical(self, "Database Error", "Failed to modify product. Please try again.")

        finally:
            if conn:
                conn.close()

        self.accept()

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Product Status")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Select the product status:")
        self.layout.addWidget(self.label)

        self.available_checkbox = QtWidgets.QCheckBox("Available")
        self.unavailable_checkbox = QtWidgets.QCheckBox("Unavailable")
        self.layout.addWidget(self.available_checkbox)
        self.layout.addWidget(self.unavailable_checkbox)

        # Create a QButtonGroup and add checkboxes to it
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.addButton(self.available_checkbox)
        self.button_group.addButton(self.unavailable_checkbox)
        self.button_group.setExclusive(True)

        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_selected_status(self):
        if self.available_checkbox.isChecked():
            return 'Available'
        elif self.unavailable_checkbox.isChecked():
            return 'Unavailable'
        else:
            return None