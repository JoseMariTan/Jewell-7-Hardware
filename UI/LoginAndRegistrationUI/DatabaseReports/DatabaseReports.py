# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseReports.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1251, 776)
        Form.setStyleSheet("background-color:#fff;")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("background-color:#81cdc6;\n"
"border-top-left-radius: 10px;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_4.setStyleSheet("background-color:#81cdc6;\n"
"\n"
"border-top-right-radius: 10px;")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setStyleSheet("background-color:#fff ;\n"
" border-style: solid;\n"
"    border-color: #dcdcdc;\n"
"    border-width: 1px;\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_2 = QtWidgets.QFrame(self.widget_5)
        self.line_2.setMinimumSize(QtCore.QSize(175, 1))
        self.line_2.setMaximumSize(QtCore.QSize(350, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.GenerateReport_button = QtWidgets.QPushButton(self.widget_5)
        self.GenerateReport_button.setMinimumSize(QtCore.QSize(175, 50))
        self.GenerateReport_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.GenerateReport_button.setFont(font)
        self.GenerateReport_button.setMouseTracking(True)
        self.GenerateReport_button.setTabletTracking(True)
        self.GenerateReport_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GenerateReport_button.setStyleSheet("QPushButton {\n"
" background-color: #10cc94;\n"
"border-radius:12px;\n"
"border-color:none;\n"
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
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GenerateReport_button.setIcon(icon)
        self.GenerateReport_button.setIconSize(QtCore.QSize(22, 22))
        self.GenerateReport_button.setObjectName("GenerateReport_button")
        self.verticalLayout_6.addWidget(self.GenerateReport_button)
        self.CustomizeReport_button = QtWidgets.QPushButton(self.widget_5)
        self.CustomizeReport_button.setMinimumSize(QtCore.QSize(175, 50))
        self.CustomizeReport_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.CustomizeReport_button.setFont(font)
        self.CustomizeReport_button.setMouseTracking(True)
        self.CustomizeReport_button.setTabletTracking(True)
        self.CustomizeReport_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CustomizeReport_button.setStyleSheet("QPushButton {\n"
" background-color: #5698d2;\n"
"border-radius:12px;\n"
"border-color:#fff;\n"
"color:#fff;\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #4379a5;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"")
        self.CustomizeReport_button.setIcon(icon)
        self.CustomizeReport_button.setIconSize(QtCore.QSize(22, 22))
        self.CustomizeReport_button.setObjectName("CustomizeReport_button")
        self.verticalLayout_6.addWidget(self.CustomizeReport_button)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.Image = QtWidgets.QLabel(self.widget_5)
        self.Image.setStyleSheet("image: url(:/Icon/report_tao.png);\n"
"border:none;")
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.gridLayout_2.addWidget(self.Image, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 286, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 1, 2, 1)
        self.Container1 = QtWidgets.QWidget(Form)
        self.Container1.setStyleSheet("background-color:#fff ;\n"
" border-style: solid;\n"
"    border-color: #dcdcdc;\n"
"    border-width: 1px;\n"
"")
        self.Container1.setObjectName("Container1")
        self.gridLayout = QtWidgets.QGridLayout(self.Container1)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.Container1)
        self.widget_3.setStyleSheet("border:none;")
        self.widget_3.setObjectName("widget_3")
        self.layoutWidget = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 311, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backupSchedule_button = QtWidgets.QPushButton(self.layoutWidget)
        self.backupSchedule_button.setMinimumSize(QtCore.QSize(175, 50))
        self.backupSchedule_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.backupSchedule_button.setFont(font)
        self.backupSchedule_button.setMouseTracking(True)
        self.backupSchedule_button.setTabletTracking(True)
        self.backupSchedule_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backupSchedule_button.setStyleSheet("QPushButton {\n"
" background-color: #10cc94;\n"
"border-radius:12px;\n"
"border-color:none;\n"
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
"\n"
"")
        self.backupSchedule_button.setIcon(icon)
        self.backupSchedule_button.setIconSize(QtCore.QSize(22, 22))
        self.backupSchedule_button.setObjectName("backupSchedule_button")
        self.verticalLayout_2.addWidget(self.backupSchedule_button)
        self.manualBackup_button = QtWidgets.QPushButton(self.layoutWidget)
        self.manualBackup_button.setMinimumSize(QtCore.QSize(175, 50))
        self.manualBackup_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.manualBackup_button.setFont(font)
        self.manualBackup_button.setMouseTracking(True)
        self.manualBackup_button.setTabletTracking(True)
        self.manualBackup_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.manualBackup_button.setStyleSheet("QPushButton {\n"
" background-color: #5698d2;\n"
"border-radius:12px;\n"
"border-color:#fff;\n"
"color:#fff;\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #4379a5;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"")
        self.manualBackup_button.setIcon(icon)
        self.manualBackup_button.setIconSize(QtCore.QSize(22, 22))
        self.manualBackup_button.setObjectName("manualBackup_button")
        self.verticalLayout_2.addWidget(self.manualBackup_button)
        self.restoreDatabase_button = QtWidgets.QPushButton(self.layoutWidget)
        self.restoreDatabase_button.setMinimumSize(QtCore.QSize(175, 50))
        self.restoreDatabase_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.restoreDatabase_button.setFont(font)
        self.restoreDatabase_button.setMouseTracking(True)
        self.restoreDatabase_button.setTabletTracking(True)
        self.restoreDatabase_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.restoreDatabase_button.setStyleSheet("QPushButton {\n"
" background-color: #5698d2;\n"
"border-radius:12px;\n"
"border-color:#fff;\n"
"color:#fff;\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #4379a5;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"\n"
"")
        self.restoreDatabase_button.setIcon(icon)
        self.restoreDatabase_button.setIconSize(QtCore.QSize(22, 22))
        self.restoreDatabase_button.setObjectName("restoreDatabase_button")
        self.verticalLayout_2.addWidget(self.restoreDatabase_button)
        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ActiveDatabase_label = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ActiveDatabase_label.setFont(font)
        self.ActiveDatabase_label.setStyleSheet("border:none;")
        self.ActiveDatabase_label.setObjectName("ActiveDatabase_label")
        self.horizontalLayout.addWidget(self.ActiveDatabase_label)
        self.ActiveDatabase_Data = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ActiveDatabase_Data.setFont(font)
        self.ActiveDatabase_Data.setStyleSheet("border:none;")
        self.ActiveDatabase_Data.setObjectName("ActiveDatabase_Data")
        self.horizontalLayout.addWidget(self.ActiveDatabase_Data)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lastBackup_label = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lastBackup_label.setFont(font)
        self.lastBackup_label.setStyleSheet("border:none;")
        self.lastBackup_label.setObjectName("lastBackup_label")
        self.horizontalLayout_2.addWidget(self.lastBackup_label)
        self.LastBackup_Data = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.LastBackup_Data.setFont(font)
        self.LastBackup_Data.setStyleSheet("border:none;")
        self.LastBackup_Data.setObjectName("LastBackup_Data")
        self.horizontalLayout_2.addWidget(self.LastBackup_Data)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CurrentTime_label = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CurrentTime_label.setFont(font)
        self.CurrentTime_label.setStyleSheet("border:none;")
        self.CurrentTime_label.setObjectName("CurrentTime_label")
        self.horizontalLayout_3.addWidget(self.CurrentTime_label)
        self.label_8 = QtWidgets.QLabel(self.Container1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border:none;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.Container1)
        self.line.setMinimumSize(QtCore.QSize(410, 1))
        self.line.setMaximumSize(QtCore.QSize(410, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.line.raise_()
        self.widget_3.raise_()
        self.gridLayout_3.addWidget(self.Container1, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database"))
        self.label_2.setText(_translate("Form", "Reports"))
        self.GenerateReport_button.setText(_translate("Form", "Generate Report"))
        self.CustomizeReport_button.setText(_translate("Form", "Customize Report"))
        self.backupSchedule_button.setText(_translate("Form", "Backup Schedule"))
        self.manualBackup_button.setText(_translate("Form", "Manual Backup"))
        self.restoreDatabase_button.setText(_translate("Form", "Restore Database"))
        self.ActiveDatabase_label.setText(_translate("Form", "Active Database: "))
        self.ActiveDatabase_Data.setText(_translate("Form", "Data"))
        self.lastBackup_label.setText(_translate("Form", "Last Backup: "))
        self.LastBackup_Data.setText(_translate("Form", "Data"))
        self.CurrentTime_label.setText(_translate("Form", "Current Automatic Backup Time: "))
        self.label_8.setText(_translate("Form", "Data"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
