import sys
import sqlite3
import random
import string
import atexit
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from shop import ShopTab
from cart import CartTab
from product_management import ProductsTab
from reports import ReportsTab
from user_management import UsersTab
from analytics import AnalyticsTab
from help import HelpTab
from about import AboutUsTab
from backup_restore import DatabaseTab

class Ui_MainWindow(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.update_cash_register()
        atexit.register(self.update_cash_register)

    def setupUi(self, AdminDashboard):
        AdminDashboard.setObjectName("AdminDashboard")
        AdminDashboard.resize(1254, 1020)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        AdminDashboard.setFont(font)
        AdminDashboard.setToolTipDuration(-1)
        AdminDashboard.setLayoutDirection(QtCore.Qt.LeftToRight)
        AdminDashboard.setStyleSheet("background-color:#fff;\n"
"")
        AdminDashboard.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(AdminDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 783, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, 15, 70, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutUs_button.setMinimumSize(QtCore.QSize(150, 50))
        self.aboutUs_button.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setMouseTracking(True)
        self.aboutUs_button.setTabletTracking(True)
        self.aboutUs_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.aboutUs_button.setStyleSheet("QPushButton {\n"
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
"    \n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Help/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutUs_button.setIcon(icon)
        self.aboutUs_button.setIconSize(QtCore.QSize(30, 30))
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 25))
        self.line.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setMinimumSize(QtCore.QSize(50, 50))
        self.help_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.help_button.setFont(font)
        self.help_button.setMouseTracking(True)
        self.help_button.setTabletTracking(True)
        self.help_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.help_button.setStyleSheet("QPushButton {\n"
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
"    \n"
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
        self.help_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Info/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QtCore.QSize(20, 20))
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        
        self.database_button = QtWidgets.QPushButton(self.centralwidget)
        self.database_button.setMinimumSize(QtCore.QSize(50, 50))
        self.database_button.setMaximumSize(QtCore.QSize(50, 50))
        icon_temp = QtGui.QIcon()
        icon_temp.addPixmap(QtGui.QPixmap(":/Icon/temp_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.database_button.setIcon(icon_temp)
        self.database_button.setIconSize(QtCore.QSize(30, 30))
        self.database_button.setObjectName("database_button")
        self.database_button.setStyleSheet("QPushButton {\n"
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
"    \n"
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
        self.database_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Settings/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.database_button.setIcon(icon1)
        self.database_button.setIconSize(QtCore.QSize(20, 20))
        self.database_button.setObjectName("help_button")
        # Add the button to the layout
        self.horizontalLayout.addWidget(self.database_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(325, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(325, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.widget_2.setToolTipDuration(-1)
        self.widget_2.setStyleSheet("background-color: #f6f4f4 ;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 40, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shop_button = QtWidgets.QPushButton(self.widget_2)
        self.shop_button.setMinimumSize(QtCore.QSize(150, 40))
        self.shop_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.shop_button.setFont(font)
        self.shop_button.setMouseTracking(True)
        self.shop_button.setTabletTracking(True)
        self.shop_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shop_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:98px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Shop/shopping-bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/Shop/white_bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.shop_button.setIcon(icon2)
        self.shop_button.setIconSize(QtCore.QSize(20, 20))
        self.shop_button.setObjectName("shop_button")
        self.verticalLayout.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.widget_2)
        self.cart_button.setMinimumSize(QtCore.QSize(150, 40))
        self.cart_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.cart_button.setFont(font)
        self.cart_button.setMouseTracking(True)
        self.cart_button.setTabletTracking(True)
        self.cart_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cart_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:106px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Cart/cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cart_button.setIcon(icon3)
        self.cart_button.setIconSize(QtCore.QSize(22, 22))
        self.cart_button.setObjectName("cart_button")
        self.verticalLayout.addWidget(self.cart_button)
        self.products_button = QtWidgets.QPushButton(self.widget_2)
        self.products_button.setMinimumSize(QtCore.QSize(150, 40))
        self.products_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.products_button.setFont(font)
        self.products_button.setMouseTracking(True)
        self.products_button.setTabletTracking(True)
        self.products_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.products_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:73px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Tools/products.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.products_button.setIcon(icon4)
        self.products_button.setIconSize(QtCore.QSize(20, 20))
        self.products_button.setObjectName("products_button")
        self.verticalLayout.addWidget(self.products_button)
        self.users_button = QtWidgets.QPushButton(self.widget_2)
        self.users_button.setMinimumSize(QtCore.QSize(150, 40))
        self.users_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.users_button.setFont(font)
        self.users_button.setMouseTracking(True)
        self.users_button.setTabletTracking(True)
        self.users_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.users_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:95px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/user/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users_button.setIcon(icon5)
        self.users_button.setIconSize(QtCore.QSize(24, 24))
        self.users_button.setObjectName("users_button")
        self.verticalLayout.addWidget(self.users_button)
        self.reports_button = QtWidgets.QPushButton(self.widget_2)
        self.reports_button.setMinimumSize(QtCore.QSize(150, 40))
        self.reports_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.reports_button.setFont(font)
        self.reports_button.setMouseTracking(True)
        self.reports_button.setTabletTracking(True)
        self.reports_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reports_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:80px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/reports/reports.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reports_button.setIcon(icon6)
        self.reports_button.setIconSize(QtCore.QSize(20, 20))
        self.reports_button.setObjectName("reports_button")
        self.verticalLayout.addWidget(self.reports_button)
        self.analytics_button = QtWidgets.QPushButton(self.widget_2)
        self.analytics_button.setMinimumSize(QtCore.QSize(150, 40))
        self.analytics_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.analytics_button.setFont(font)
        self.analytics_button.setMouseTracking(True)
        self.analytics_button.setTabletTracking(True)
        self.analytics_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.analytics_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:70px;\n"
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
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"QPushButton:focus {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/analytics/analytics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_button.setIcon(icon7)
        self.analytics_button.setIconSize(QtCore.QSize(20, 20))
        self.analytics_button.setObjectName("analytics_button")
        self.verticalLayout.addWidget(self.analytics_button)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(25, 190, 25, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setStyleSheet("background-color:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.logout_button = QtWidgets.QPushButton(self.widget_2)
        self.logout_button.setMinimumSize(QtCore.QSize(100, 40))
        self.logout_button.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.logout_button.setFont(font)
        self.logout_button.setMouseTracking(True)
        self.logout_button.setTabletTracking(True)
        self.logout_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logout_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:13px;\n"
"color: #636363;\n"
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
"    \n"
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/logout/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon8)
        self.logout_button.setIconSize(QtCore.QSize(25, 25))
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout_2.addWidget(self.logout_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(50, 10, -1, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(200, 150))
        self.logo.setMaximumSize(QtCore.QSize(200, 150))
        self.logo.setStyleSheet("image: url(:/Icon/logo.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_4.addWidget(self.logo)
        self.adminLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.adminLabel.setFont(font)
        self.adminLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.adminLabel.setStyleSheet("background:none;")
        self.adminLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.adminLabel.setObjectName("adminLabel")
        self.verticalLayout_4.addWidget(self.adminLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 3, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 1, 1)
        AdminDashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminDashboard)
        QtCore.QMetaObject.connectSlotsByName(AdminDashboard)
        
        # Connect buttons to methods
        self.shop_button.clicked.connect(self.open_shop)
        self.cart_button.clicked.connect(self.open_cart)
        self.products_button.clicked.connect(self.open_products)
        self.users_button.clicked.connect(self.open_users)
        self.reports_button.clicked.connect(self.open_reports)
        self.analytics_button.clicked.connect(self.open_analytics)
        self.logout_button.clicked.connect(self.logout)
        self.aboutUs_button.clicked.connect(self.open_about)
        self.database_button.clicked.connect(self.database_options)
        self.help_button.clicked.connect(self.open_help)

    def retranslateUi(self, AdminDashboard):
        _translate = QtCore.QCoreApplication.translate
        AdminDashboard.setWindowTitle(_translate("AdminDashboard", "AdminDashboard"))
        self.aboutUs_button.setText(_translate("AdminDashboard", "About us"))
        self.shop_button.setText(_translate("AdminDashboard", "  Shop"))
        self.cart_button.setText(_translate("AdminDashboard", "  Cart"))
        self.products_button.setText(_translate("AdminDashboard", "  Products"))
        self.users_button.setText(_translate("AdminDashboard", "  Users"))
        self.reports_button.setText(_translate("AdminDashboard", "  Reports"))
        self.analytics_button.setText(_translate("AdminDashboard", "  Analytics"))
        self.logout_button.setText(_translate("AdminDashboard", "Sign out"))
        self.adminLabel.setText(_translate("AdminDashboard", "    Admin Dashboard"))
    from assets import mainlogo_rc


    # Navigation Functions
    def open_shop(self):
        self.update_cash_register()
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
        self.users_tab = UsersTab(self.user_id)
        self.stackedWidget.addWidget(self.users_tab)
        self.stackedWidget.setCurrentWidget(self.users_tab)

    def open_reports(self):
        self.reports_tab = ReportsTab(self.user_id)
        self.stackedWidget.addWidget(self.reports_tab)
        self.stackedWidget.setCurrentWidget(self.reports_tab)

    def open_analytics(self):
        self.analytics_tab = AnalyticsTab()
        self.stackedWidget.addWidget(self.analytics_tab)
        self.stackedWidget.setCurrentWidget(self.analytics_tab)

    def update_cart_tab(self):
        if hasattr(self, 'cart_tab'):
            self.cart_tab.load_cart_items()

    def open_about(self):
        self.aboutUs_tab = AboutUsTab()
        self.stackedWidget.addWidget(self.aboutUs_tab)
        self.stackedWidget.setCurrentWidget (self.aboutUs_tab)

    def open_help(self):
        self.help_tab = HelpTab()
        self.stackedWidget.addWidget(self.help_tab)
        self.stackedWidget.setCurrentWidget (self.help_tab)
            
    def database_options(self):
        self.database_tab = DatabaseTab(self.user_id)
        self.stackedWidget.addWidget(self.database_tab)
        self.stackedWidget.setCurrentWidget(self.database_tab)

    def logout(self):
        conn = sqlite3.connect('j7h.db')
        cursor = conn.cursor()

        # Use the stored user_id
        user_id = self.user_id
        log_id = self.generate_log_id()
        current_datetime = datetime.today()
        date_log = current_datetime.strftime('%Y-%m-%d')
        time_log = current_datetime.strftime("%I:%M %p")
        action = "logout"

        cursor.execute('''INSERT INTO user_logs (log_id, user_id, action, time, date) 
                            VALUES (?, ?, ?, ?, ?)''', (log_id, user_id, action, time_log, date_log))
        conn.commit()
        
        # Update the cash register
        self.update_cash_register()
        
        QtWidgets.QApplication.instance().activeWindow().close()
        # Go back to selection_screen
        from main import Selection
        self.new_window = QtWidgets.QMainWindow()
        self.selection_ui = Selection()
        self.selection_ui.setupUi(self.new_window)
        self.new_window.showFullScreen()
        
    def update_cash_register(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('j7h.db')
            cursor = conn.cursor()
            
            # Get the current date in the specified format
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            # Get the latest entry in the cash_register table for the current date
            cursor.execute("""
                SELECT current_value, ending_value, date 
                FROM cash_register 
                WHERE date = ?
            """, (current_date,))
            result = cursor.fetchone()
            
            if result:
                current_value, ending_value, date = result
                
                # Check if the date is different from today
                if date != current_date:
                    # Get the ending value of the previous day
                    cursor.execute("""
                        SELECT ending_value 
                        FROM cash_register 
                        WHERE date < ? 
                        ORDER BY date DESC 
                        LIMIT 1
                    """, (current_date,))
                    previous_day_result = cursor.fetchone()
                    previous_ending_value = previous_day_result[0] if previous_day_result else 0

                    # Add a new row with the initial value set to the ending value of the previous day
                    cursor.execute("""
                        INSERT INTO cash_register (current_value, initial_value, ending_value, date) 
                        VALUES (?,?,?,?)
                    """, (previous_ending_value, previous_ending_value, previous_ending_value, current_date))
                else:
                    # Update the ending value to match the current value for today's entry
                    cursor.execute("""
                        UPDATE cash_register 
                        SET ending_value = ? 
                        WHERE date = ?
                    """, (current_value, current_date))
            else:
                # Get the ending value of the previous day
                cursor.execute("""
                    SELECT ending_value 
                    FROM cash_register 
                    WHERE date < ? 
                    ORDER BY date DESC 
                    LIMIT 1
                """, (current_date,))
                previous_day_result = cursor.fetchone()
                previous_ending_value = previous_day_result[0] if previous_day_result else 0

                # If no rows exist in the table, add a new row with initial and ending values set to 0
                cursor.execute("""
                    INSERT INTO cash_register (current_value, initial_value, ending_value, date) 
                    VALUES (?,?,?,?)
                """, (previous_ending_value, previous_ending_value, previous_ending_value, current_date))
            
            conn.commit()
        
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        
        finally:
            if conn:
                conn.close()
            
    def generate_log_id(self):
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
                log_id = f"LOG{current_date}{random_letters}"
            
                # Check if the transaction ID already exists in the database
                cursor.execute("SELECT 1 FROM user_logs WHERE log_id = ?", (log_id,))
                if not cursor.fetchone():
                    return log_id
        finally:
            # Ensure the database connection is closed
            conn.close()   
