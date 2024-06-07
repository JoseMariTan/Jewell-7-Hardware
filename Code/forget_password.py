# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword):
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(592, 481)
        self.centralwidget = QtWidgets.QWidget(ForgotPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 110, 531, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.birthdate_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_label.setFont(font)
        self.birthdate_label.setObjectName("birthdate_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birthdate_label)
        self.middleName_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.middleName_label.setFont(font)
        self.middleName_label.setObjectName("middleName_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.middleName_label)
        self.birthdate_edit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.birthdate_edit.setFont(font)
        self.birthdate_edit.setObjectName("birthdate_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birthdate_edit)
        self.middleName_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.middleName_input.setFont(font)
        self.middleName_input.setObjectName("middleName_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.middleName_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.forgot_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.forgot_button.setFont(font)
        self.forgot_button.setStyleSheet("background-color:#53C851;")
        self.forgot_button.setDefault(True)
        self.forgot_button.setFlat(False)
        self.forgot_button.setObjectName("forgot_button")
        self.horizontalLayout.addWidget(self.forgot_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        ForgotPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForgotPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 22))
        self.menubar.setObjectName("menubar")
        ForgotPassword.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForgotPassword)
        self.statusbar.setObjectName("statusbar")
        ForgotPassword.setStatusBar(self.statusbar)

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "MainWindow"))
        self.birthdate_label.setText(_translate("ForgotPassword", "Birthdate:"))
        self.middleName_label.setText(_translate("ForgotPassword", "Middle Name:"))
        self.forgot_button.setText(_translate("ForgotPassword", "Forget Password"))

    def forget_password(self):
        birthdate = self.birthdate_edit.date().toString(QtCore.Qt.ISODate)
        middle_name = self.middleName_input.text().strip()

        if not middle_name:
            # Displaying a message box for error
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please fill in all the fields.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPassword = QtWidgets.QMainWindow()
    ui = Ui_ForgotPassword()
    ui.setupUi(ForgotPassword)
    ForgotPassword.show()
    sys.exit(app.exec_())