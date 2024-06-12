from PyQt5 import QtCore, QtGui, QtWidgets
from shop import ShopTab
from cart import CartTab
from productManagement import ProductsTab
from reports import ReportsTab
from users import UsersTab

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

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)

        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)

        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shop_button.setFont(font)
        self.shop_button.setObjectName("shop_button")
        self.shop_button.setMinimumSize(QtCore.QSize(400, 25))
        self.shop_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cart_button.setFont(font)
        self.cart_button.setObjectName("cart_button")
        self.cart_button.setMinimumSize(QtCore.QSize(400, 25))
        self.cart_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.cart_button)
        self.products_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.products_button.setFont(font)
        self.products_button.setObjectName("products_button")
        self.products_button.setMinimumSize(QtCore.QSize(400, 25))
        self.products_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.products_button)
        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.users_button.setFont(font)
        self.users_button.setObjectName("users_button")
        self.users_button.setMinimumSize(QtCore.QSize(400, 25))
        self.users_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.users_button)
        self.reports_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reports_button.setFont(font)
        self.reports_button.setObjectName("reports_button")
        self.reports_button.setMinimumSize(QtCore.QSize(400, 25))
        self.reports_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.reports_button)
        self.analytics_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.analytics_button.setFont(font)
        self.analytics_button.setObjectName("analytics_button")
        self.analytics_button.setMinimumSize(QtCore.QSize(400, 25))
        self.analytics_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.analytics_button)
        self.returns_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.returns_button.setFont(font)
        self.returns_button.setObjectName("returns_button")
        self.returns_button.setMinimumSize(QtCore.QSize(400, 25))
        self.returns_button.setSizePolicy(button_size_policy)
        self.verticalLayout_2.addWidget(self.returns_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)

        # Create a QStackedWidget for different views
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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
        self.help_button.setText(_translate("MainWindow", "Help"))
        self.aboutUs_button.setText(_translate("MainWindow", "About Us"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
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
        self.products_tab = ProductsTab(self.user_id)
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
        pass  # Implement this function

    def open_returns(self):
        pass  # Implement this function

    def update_cart_tab(self):
        if hasattr(self, 'cart_tab'):
            self.cart_tab.load_cart_items()

    def logout(self):
        from login import Ui_Login
        # Create and show the login window
        self.login_window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login_window)
        self.login_window.show()
        # Close the main window
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    import sys
    from login import Ui_Login

    app = QtWidgets.QApplication(sys.argv)

    # Create and show the login window
    login_window = Ui_Login()
    login_window.show()

    # Start the application event loop
    sys.exit(app.exec_())
