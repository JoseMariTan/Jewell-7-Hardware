import sqlite3
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QPushButton,
                             QSpinBox, QVBoxLayout)


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
    
class Ui_ShopTab(object):
    def setupUi(self, ShopTab):
        ShopTab.setObjectName("ShopTab")
        ShopTab.resize(1300, 880)
        ShopTab.setStyleSheet("background-color:#fff;\n"
                              "")
        self.gridLayout = QtWidgets.QGridLayout(ShopTab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search_button = QtWidgets.QPushButton(ShopTab)
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
        self.search_input = QtWidgets.QLineEdit(ShopTab)
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
        self.tableWidget = QtWidgets.QTableWidget(ShopTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #88ccc4; }")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(45, -1, 45, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(ShopTab)
        self.line.setMinimumSize(QtCore.QSize(200, 0))
        self.line.setMaximumSize(QtCore.QSize(200, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.add_to_cart_button = QtWidgets.QPushButton(ShopTab)
        self.add_to_cart_button.setMinimumSize(QtCore.QSize(150, 50))
        self.add_to_cart_button.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.add_to_cart_button.setFont(font)
        self.add_to_cart_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_to_cart_button.setMouseTracking(True)
        self.add_to_cart_button.setTabletTracking(True)
        self.add_to_cart_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.add_to_cart_button.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.add_to_cart_button.setAcceptDrops(False)
        self.add_to_cart_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_to_cart_button.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(":/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_to_cart_button.setIcon(icon1)
        self.add_to_cart_button.setIconSize(QtCore.QSize(30, 30))
        self.add_to_cart_button.setObjectName("add_to_cart_button")
        self.horizontalLayout.addWidget(self.add_to_cart_button)
        self.line_2 = QtWidgets.QFrame(ShopTab)
        self.line_2.setMinimumSize(QtCore.QSize(200, 0))
        self.line_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.line.raise_()
        spacerItem3 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.search_input.setClearButtonEnabled(True)

        self.retranslateUi(ShopTab)
        QtCore.QMetaObject.connectSlotsByName(ShopTab)

    def retranslateUi(self, ShopTab):
        _translate = QtCore.QCoreApplication.translate
        ShopTab.setWindowTitle(_translate("ShopTab", "Form"))
        self.search_input.setPlaceholderText(_translate("ShopTab", "Search shop..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ShopTab", "Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ShopTab", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ShopTab", "Variation"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ShopTab", "Size"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ShopTab", "Price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ShopTab", "Items in Stock"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ShopTab", "Category"))
        self.add_to_cart_button.setText(_translate("ShopTab", "Add to cart"))
from assets import shop_rc

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
                    SELECT * FROM products
                    WHERE 
                        (product_name LIKE ? COLLATE NOCASE OR product_name = ?) OR
                        (brand LIKE ? COLLATE NOCASE OR brand = ?) OR
                        (var LIKE ? COLLATE NOCASE OR var = ?) OR
                        (size LIKE ? COLLATE NOCASE OR size = ?) OR
                        (category LIKE ? COLLATE NOCASE OR category = ?) AND
                        status = 'Available'
                    ORDER BY date_added DESC, time_added DESC
                """, (search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param, search_param, exact_search_param,
                      search_param, exact_search_param))
            else:
                cursor.execute("SELECT * FROM products WHERE status = 'Available' ORDER BY date_added DESC, time_added DESC")

            rows = cursor.fetchall()

            if not rows:
                QtWidgets.QMessageBox.information(self, "No Data Found", "No data found.")
                return
        
            self.tableWidget.setRowCount(len(rows))
            for row_number, row_data in enumerate(rows):
                self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))  # product
                self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))  # brand
                self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))  # var
                self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))  # size
                self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data[5])))  # price
                qty = row_data[6]  # qty
                threshold = row_data[7]  # threshold
                self.items_in_stock = qty - threshold  # subtract threshold
                self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(self.items_in_stock)))  # Items in Stock
                self.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(row_data[8])))  # category
        except sqlite3.Error as e:
            print("SQLite error:", e)
            QtWidgets.QMessageBox.critical(self, "Database Error", "Failed to load data. Please try again.")

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
        self.ui = Ui_ShopTab()
        self.ui.setupUi(self)
        self.ui.search_button.clicked.connect(self.search_products)
        self.ui.add_to_cart_button.clicked.connect(self.show_add_to_cart_dialog)
        self.ui.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)
        self.tableWidget = self.ui.tableWidget
        self.search_input = self.ui.search_input
        self.load_products()
        
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
                qty = int(qty_text)
                price = float(price_text)
                new_qty = qty - quantity

                conn = sqlite3.connect('j7h.db')
                cursor = conn.cursor()

                # Fetch threshold from the database
                cursor.execute("""
                    SELECT threshold 
                    FROM products 
                    WHERE product_name = ? 
                    AND (brand = ? OR brand IS NULL) 
                    AND (var = ? OR var IS NULL) 
                    AND (size = ? OR size IS NULL)
                """, (product_name, brand, var, size))
                threshold_result = cursor.fetchone()

                if threshold_result:
                    threshold = threshold_result[0]
                    new_qty += threshold

                if new_qty >= 0:
                    # Update quantity, time_added, and date_added in products table
                    cursor.execute("""
                        UPDATE products 
                        SET qty = ?, time_added = ?, date_added = ? 
                        WHERE product_name = ? 
                        AND (brand = ? OR brand IS NULL) 
                        AND (var = ? OR var IS NULL) 
                        AND (size = ? OR size IS NULL)
                    """, (new_qty, datetime.now().strftime('%H:%M:%S'), datetime.now().strftime('%Y-%m-%d'), product_name, brand, var, size))

                    items_in_stock = qty - quantity
                    if items_in_stock == 0:
                        status = "Unavailable"
                        cursor.execute("UPDATE products SET qty = ?, status = ? WHERE product_name = ?", (new_qty, status, product_name))
                        conn.commit() 
                        self.tableWidget.removeRow(row.row())
                        self.item_added_to_cart.emit()
                    else:
                        self.tableWidget.item(row.row(), 5).setText(str(items_in_stock))  # Update items in stock displayed in the shop

                    total_price = quantity * float(price_text)
                    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # Fetch product_id, time_added, and date_added from the database
                    cursor.execute("""
                        SELECT product_id, time_added, date_added 
                        FROM products 
                        WHERE product_name = ? 
                        AND (brand = ? OR brand IS NULL) 
                        AND (var = ? OR var IS NULL) 
                        AND (size = ? OR size IS NULL)
                    """, (product_name, brand, var, size))
                    product_data = cursor.fetchone()

                    if product_data:
                        product_id, time_added, date_added = product_data

                        cursor.execute('''INSERT INTO cart (product_name, qty, total_price, date, product_id, brand, var, size, time_added, date_added)
                                        VALUES (?,?,?,?,?,?,?,?,?,?)''',
                                    (product_name, quantity, total_price, date, product_id, brand, var, size, time_added, date_added))

                        conn.commit()
                        QtWidgets.QMessageBox.information(self, "Cart Updated", "Items added to cart!")
                        self.item_added_to_cart.emit()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", f"Product data not found for {product_name}, {brand}, {var}, {size}")

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

    def show_add_to_cart_dialog(self):
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())
        if selected_rows:
            max_quantity = 0
            for row in selected_rows:
                qty_item = self.tableWidget.item(row, 5)
                if qty_item is not None:
                    try:
                        qty = int(qty_item.text())
                        if qty > max_quantity:
                            max_quantity = qty
                    except ValueError:
                        pass
            dialog = AddToCartDialog(max_quantity=max_quantity)
            if dialog.exec_() == QDialog.Accepted:
                quantity = dialog.get_quantity()
                if quantity > 0:  # Ensure that the quantity is valid before adding to cart
                    self.add_to_cart(quantity)
                else:
                    QtWidgets.QMessageBox.warning(self, "Quantity Error", "Quantity must be greater than zero.")
        else:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a product to add to the cart.")
