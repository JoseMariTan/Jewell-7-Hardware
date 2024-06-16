import sys
import sqlite3
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from shop import ShopTab
from cart import CartTab
from productManagement import ProductsTab
from reports import ReportsTab
from users import UsersTab
from analytics import AnalyticsTab  # Import the AnalyticsTab class

class Ui_MainWindow(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setMinimumSize(QtCore.QSize(50, 50))
        self.help_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.help_button.setFont(font)
        self.help_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-style: outset;\n"
"    border: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutUs_button.setMinimumSize(QtCore.QSize(50, 50))
        self.aboutUs_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-style: outset;\n"
"    border: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setMinimumSize(QtCore.QSize(50, 50))
        self.logout_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-style: outset;\n"
"    border: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_button.sizePolicy().hasHeightForWidth())
        self.shop_button.setSizePolicy(sizePolicy)
        self.shop_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.shop_button.setFont(font)
        self.shop_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")

        self.shop_button.setObjectName("shop_button")
        self.verticalLayout_2.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cart_button.sizePolicy().hasHeightForWidth())
        self.cart_button.setSizePolicy(sizePolicy)
        self.cart_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cart_button.setFont(font)
        self.cart_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.cart_button.setObjectName("cart_button")
        self.verticalLayout_2.addWidget(self.cart_button)
        self.products_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.products_button.sizePolicy().hasHeightForWidth())
        self.products_button.setSizePolicy(sizePolicy)
        self.products_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.products_button.setFont(font)
        self.products_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.products_button.setObjectName("products_button")
        self.verticalLayout_2.addWidget(self.products_button)
        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.users_button.sizePolicy().hasHeightForWidth())
        self.users_button.setSizePolicy(sizePolicy)
        self.users_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.users_button.setFont(font)
        self.users_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.users_button.setObjectName("users_button")
        self.verticalLayout_2.addWidget(self.users_button)
        self.reports_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reports_button.sizePolicy().hasHeightForWidth())
        self.reports_button.setSizePolicy(sizePolicy)
        self.reports_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.reports_button.setFont(font)
        self.reports_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.reports_button.setObjectName("reports_button")
        self.verticalLayout_2.addWidget(self.reports_button)
        self.analytics_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analytics_button.sizePolicy().hasHeightForWidth())
        self.analytics_button.setSizePolicy(sizePolicy)
        self.analytics_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.analytics_button.setFont(font)
        self.analytics_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.analytics_button.setObjectName("analytics_button")
        self.verticalLayout_2.addWidget(self.analytics_button)
        self.returns_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returns_button.sizePolicy().hasHeightForWidth())
        self.returns_button.setSizePolicy(sizePolicy)
        self.returns_button.setMinimumSize(QtCore.QSize(400, 75))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.returns_button.setFont(font)
        self.returns_button.setStyleSheet("QPushButton{\n"
"    background-color: #c6c6c8;\n"
"    border-width: 2px;\n"
"    border-style: outset;;\n"
"    border-radius: 20px;\n"
"    border-color: black;\n"
"    padding: 4px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #575759; \n"
"    color: white;\n"
"}\n"
"")
        self.returns_button.setObjectName("returns_button")
        self.verticalLayout_2.addWidget(self.returns_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to methods
        self.shop_button.clicked.connect(self.open_shop)
        self.cart_button.clicked.connect(self.open_cart)
        self.products_button.clicked.connect(self.open_products)
        self.users_button.clicked.connect(self.open_users)
        self.reports_button.clicked.connect(self.open_reports)
        self.analytics_button.clicked.connect(self.open_analytics)
        self.returns_button.clicked.connect(self.open_returns)
        self.logout_button.clicked.connect(self.logout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jewell 7 Hardware"))
        self.label.setText(_translate("MainWindow", "Admin Dashboard"))
        self.help_button.setText(_translate("MainWindow", "?"))
        self.aboutUs_button.setText(_translate("MainWindow", "i"))
        self.logout_button.setText(_translate("MainWindow", "↩"))
        self.shop_button.setText(_translate("MainWindow", "Shop"))
        self.cart_button.setText(_translate("MainWindow", "Cart"))
        self.products_button.setText(_translate("MainWindow", "Products"))
        self.users_button.setText(_translate("MainWindow", "Users"))
        self.reports_button.setText(_translate("MainWindow", "Reports"))
        self.analytics_button.setText(_translate("MainWindow", "Analytics"))
        self.returns_button.setText(_translate("MainWindow", "Returns"))

    # Navigation Functions
    def open_shop(self):
        self.shop_tab = ShopTab()
        self.stackedWidget.addWidget(self.shop_tab)
        self.stackedWidget.setCurrentWidget(self.shop_tab)
        self.shop_tab.item_added_to_cart.connect(self.update_cart_tab)

    def open_cart(self):
        if not hasattr(self, 'cart_tab'):
            self.cart_tab = CartTab(self.user_id)
            self.stackedWidget.addWidget(self.cart_tab)
        self.stackedWidget.setCurrentWidget(self.cart_tab)

    def open_products(self):
        self.products_tab = ProductsTab()
        self.stackedWidget.addWidget(self.products_tab)
        self.stackedWidget.setCurrentWidget(self.products_tab)

    def open_users(self):
        self.users_tab = UsersTab()
        self.stackedWidget.addWidget(self.users_tab)
        self.stackedWidget.setCurrentWidget(self.users_tab)

    def open_reports(self):
        self.reports_tab = ReportsTab()
        self.stackedWidget.addWidget(self.reports_tab)
        self.stackedWidget.setCurrentWidget(self.reports_tab)

    def open_analytics(self):
        self.analytics_tab = AnalyticsTab()
        self.stackedWidget.addWidget(self.analytics_tab)
        self.stackedWidget.setCurrentWidget(self.analytics_tab)

    def open_returns(self):
        pass  # Implement this function

    def update_cart_tab(self):
        if hasattr(self, 'cart_tab'):
            self.cart_tab.load_cart_items()

    def logout(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        # Use the stored user_id
        user_id = self.user_id
        current_datetime = datetime.today()
        date_log = current_datetime.strftime('%Y-%m-%d')
        time_log = current_datetime.strftime("%I:%M %p")
        action = "logout"

        cursor.execute('''INSERT INTO user_logs (user_id, action, time, date) 
                            VALUES (?, ?, ?, ?)''', (user_id, action, time_log, date_log))
        conn.commit()

        # Create and show the login window
        from login import Login
        self.login_window = QtWidgets.QMainWindow()
        self.ui = Login()
        self.ui.setupUi(self.login_window)
        self.login_window.show()
        # Close the main window
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the selection window
    from selection_screen import Selection
    selection_window = Selection()
    selection_window.show()
    sys.exit(app.exec_())
