import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import string, random
from datetime import datetime

class PaymentForm(QDialog):
    def __init__(self, total_price, parent=None):
        super().__init__(parent)
        self.total_price = total_price
        self.payment_id = None
        self.products_in_cart = []
        self.customer_details = None
        self.setupUi()
        self.fetch_products_from_cart()
    
    def setupUi(self):
        self.setObjectName("Payment Form")
        self.resize(426, 445)
        self.setMinimumSize(QtCore.QSize(426, 445))
        self.setMaximumSize(QtCore.QSize(426, 445))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: #FAF9F6;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.name_edit = QtWidgets.QLineEdit(self)
        self.verticalLayout.addWidget(self.name_edit)
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.contact_edit = QtWidgets.QLineEdit(self)
        self.verticalLayout.addWidget(self.contact_edit)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.address_edit = QtWidgets.QLineEdit(self)
        self.verticalLayout.addWidget(self.address_edit)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.amount_edit = QtWidgets.QLineEdit(self)
        self.amount_edit.setValidator(QtGui.QDoubleValidator(0.99, 9999.99, 2))
        self.verticalLayout.addWidget(self.amount_edit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.complete_button = QtWidgets.QPushButton(self)
        self.complete_button.setEnabled(False)
        self.complete_button.setObjectName("complete_button")
        self.gridLayout_2.addWidget(self.complete_button, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 2)
        self.clear_button = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout_2.addWidget(self.clear_button, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.retranslateUi()
        self.amount_edit.textChanged.connect(self.check_amount)
        self.clear_button.clicked.connect(self.clear_fields)
        self.complete_button.clicked.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Payment Form"))
        self.label.setText(_translate("Form", "PAYMENT FORM"))
        self.label_2.setText(_translate("Form", "Customer Name"))
        self.name_edit.setPlaceholderText(_translate("Form", "Enter name"))
        self.label_3.setText(_translate("Form", "Contact Number"))
        self.contact_edit.setPlaceholderText(_translate("Form", "Enter number"))
        self.label_4.setText(_translate("Form", "Address"))
        self.address_edit.setPlaceholderText(_translate("Form", "Enter address"))
        self.label_5.setText(_translate("Form", "Amount Paid (PHP)"))
        self.amount_edit.setPlaceholderText(_translate("Form", "Enter amount paid"))
        self.complete_button.setText(_translate("Form", "Complete"))
        self.clear_button.setText(_translate("Form", "Clear"))

    def fetch_products_from_cart(self):
        try:
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()
            cursor.execute("SELECT product_name, qty, total_price, brand, var, size FROM cart")
            rows = cursor.fetchall()
            for row in rows:
                product = {
                    'name': row[0],       
                    'quantity': row[1],   
                    'total_price': float(row[2]),  
                    'brand': row[3],      
                    'variant': row[4],    
                    'size': row[5]      
                }
                self.products_in_cart.append(product)
        except sqlite3.Error as e:
            print(f"Error fetching products from cart: {e}")
        finally:
            if conn:
                conn.close()
                
    def check_amount(self):
        amount_paid_str = self.amount_edit.text()
        if amount_paid_str:
                amount_paid = float(amount_paid_str)
        else:
                amount_paid = 0

        if amount_paid >= float(self.total_price):
                self.complete_button.setEnabled(True)
                self.amount_edit.setStyleSheet("")
        else:
                self.complete_button.setEnabled(False)
                self.amount_edit.setStyleSheet("border: 1px solid red;")

    def clear_fields(self):
        self.name_edit.clear()
        self.contact_edit.clear()
        self.address_edit.clear()
        self.amount_edit.clear()
        self.complete_button.setEnabled(False)

    def accept(self):
        if self.validate_fields():
                customer_details = {
                "name": self.name_edit.text(),
                "contact": self.contact_edit.text(),
                "address": self.address_edit.text(),
                "amount_paid": float(self.amount_edit.text())
                }
                self.customer_details = customer_details
                payment_id = self.generate_payment_id()
                self.payment_id = payment_id
                self.done(QtWidgets.QDialog.Accepted)
                self.show_receipt(customer_details, payment_id)
                
        else:
                QMessageBox.warning(self, "Validation Error", "Please fill in all fields and ensure amount is sufficient.")

    def validate_fields(self):
        fields = [
            self.name_edit.text(),
            self.contact_edit.text(),
            self.address_edit.text(),
            self.amount_edit.text()
        ]
        if all(fields) and float(self.amount_edit.text()) >= self.total_price:
            return True
        return False


    def show_receipt(self, customer_details, payment_id):
        cart_products = self.products_in_cart  # Use the already fetched cart products

        def censor_text(text, visible_chars=4):
            return text[:visible_chars] + '*' * (len(text) - visible_chars) if len(text) > visible_chars else text

        # Censoring contact number and address
        censored_contact = censor_text(customer_details['contact'])
        censored_address = censor_text(customer_details['address'])

        business_name = "Jewell 7 Hardware"
        business_address = "123 Hardware St., City, Country"  # Placeholder address
        business_contact1 = "09530330697"
        business_contact2 = "09852434838"

        # Function to center text within a given width using asterisks
        def center_text(text, width):
            return f"*{text:^{width - 2}}*"

        receipt_width = 46  # Define the width of the receipt

        receipt_header = f"""
    *{'=' * 44}*
    *{center_text(business_name, 44)}*
    *{'=' * 44}*
    Address: {business_address}
    Contact: {business_contact1}, {business_contact2}
    *{'=' * 44}*
    PAYMENT ID: {payment_id}
    *{'-' * 60}*
    Customer Details:
    *{'-' * 60}*
    Name\t: {customer_details['name']}
    Contact\t: {censored_contact}
    Address\t: {censored_address}
    *{'-' * 60}*
    Products Purchased:
    *{'-' * 60}*
    """

        total_price = 0
        product_lines = []

        # Define fixed-width columns
        name_width = 20
        quantity_width = 8
        price_width = 15

        for product in cart_products:
            name = product['name'][:name_width]  # Truncate if too long
            quantity = product['quantity']
            total_price_product = product['total_price']
            total_price += total_price_product
            product_line = f"{name:<{name_width}} {quantity:<{quantity_width}} PHP{total_price_product:>{price_width - 4}.2f}"
            product_lines.append(product_line)

        payment_details = f"""
    *{'-' * 44}*
    Total Price\t: PHP{total_price:.2f}
    Amount Paid\t: PHP{customer_details['amount_paid']:.2f}
    Change\t\t: PHP{customer_details['amount_paid'] - total_price:.2f}
    *{'=' * 44}*
    THANK YOU FOR YOUR PURCHASE!
    *{'=' * 44}*
    """

        receipt = receipt_header + "\n".join(product_lines) + payment_details

        # Create a QMessageBox and set the receipt as its text
        message_box = QMessageBox()
        message_box.setWindowTitle("Receipt")
        message_box.setText(receipt)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def generate_payment_id(self):
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
                    payment_id = f"PAY{current_date}{random_letters}"
                
                    # Check if the transaction ID already exists in the database
                    cursor.execute("SELECT 1 FROM transactions WHERE payment_id = ?", (payment_id,))
                    if not cursor.fetchone():
                        return payment_id
            finally:
                # Ensure the database connection is closed
                conn.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PaymentForm() 
    ui.show()
    sys.exit(app.exec_())
