# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cart_Tab(object):
    def setupUi(self, Cart_Tab):
        Cart_Tab.setObjectName("Cart_Tab")
        Cart_Tab.resize(1284, 850)
        Cart_Tab.setStyleSheet("background-color:#fff;")
        self.gridLayout = QtWidgets.QGridLayout(Cart_Tab)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search_button = QtWidgets.QPushButton(Cart_Tab)
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
        self.search_input = QtWidgets.QLineEdit(Cart_Tab)
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
        self.tableWidget = QtWidgets.QTableWidget(Cart_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_button = QtWidgets.QPushButton(Cart_Tab)
        self.clear_button.setMinimumSize(QtCore.QSize(175, 50))
        self.clear_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clear_button.setFont(font)
        self.clear_button.setMouseTracking(True)
        self.clear_button.setTabletTracking(True)
        self.clear_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear_button.setStyleSheet("QPushButton {\n"
" background-color: #F88379;\n"
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
"   background-color: #E5676B;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon1)
        self.clear_button.setIconSize(QtCore.QSize(22, 22))
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.remove_button = QtWidgets.QPushButton(Cart_Tab)
        self.remove_button.setMinimumSize(QtCore.QSize(175, 50))
        self.remove_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.remove_button.setFont(font)
        self.remove_button.setMouseTracking(True)
        self.remove_button.setTabletTracking(True)
        self.remove_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove_button.setStyleSheet("QPushButton {\n"
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
        self.remove_button.setIcon(icon1)
        self.remove_button.setIconSize(QtCore.QSize(22, 22))
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.pay_button = QtWidgets.QPushButton(Cart_Tab)
        self.pay_button.setMinimumSize(QtCore.QSize(175, 50))
        self.pay_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pay_button.setFont(font)
        self.pay_button.setMouseTracking(True)
        self.pay_button.setTabletTracking(True)
        self.pay_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pay_button.setStyleSheet("QPushButton {\n"
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
        self.pay_button.setIcon(icon1)
        self.pay_button.setIconSize(QtCore.QSize(22, 22))
        self.pay_button.setObjectName("pay_button")
        self.horizontalLayout.addWidget(self.pay_button)
        self.add_to_cart_button = QtWidgets.QPushButton(Cart_Tab)
        self.add_to_cart_button.setMinimumSize(QtCore.QSize(175, 50))
        self.add_to_cart_button.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.add_to_cart_button.setFont(font)
        self.add_to_cart_button.setMouseTracking(True)
        self.add_to_cart_button.setTabletTracking(True)
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
        self.add_to_cart_button.setIcon(icon1)
        self.add_to_cart_button.setIconSize(QtCore.QSize(22, 22))
        self.add_to_cart_button.setObjectName("add_to_cart_button")
        self.horizontalLayout.addWidget(self.add_to_cart_button)
        self.total_label = QtWidgets.QLabel(Cart_Tab)
        self.total_label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.total_label.setFont(font)
        self.total_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout.addWidget(self.total_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Cart_Tab)
        QtCore.QMetaObject.connectSlotsByName(Cart_Tab)

    def retranslateUi(self, Cart_Tab):
        _translate = QtCore.QCoreApplication.translate
        Cart_Tab.setWindowTitle(_translate("Cart_Tab", "Cart"))
        self.search_input.setPlaceholderText(_translate("Cart_Tab", "  Search..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Cart_Tab", "Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Cart_Tab", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Cart_Tab", "Variation"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Cart_Tab", "Size"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Cart_Tab", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Cart_Tab", "Total Price"))
        self.clear_button.setText(_translate("Cart_Tab", "Clear Cart"))
        self.remove_button.setText(_translate("Cart_Tab", "Remove Item"))
        self.pay_button.setText(_translate("Cart_Tab", "Mark as Replacement"))
        self.add_to_cart_button.setText(_translate("Cart_Tab", "Check Out"))
        self.total_label.setText(_translate("Cart_Tab", "Total Price: ₱ 0.00"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cart_Tab = QtWidgets.QWidget()
    ui = Ui_Cart_Tab()
    ui.setupUi(Cart_Tab)
    Cart_Tab.show()
    sys.exit(app.exec_())