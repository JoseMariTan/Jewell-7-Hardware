# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analytics.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1281, 914)
        Form.setStyleSheet("background-color:#fff;")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Container = QtWidgets.QWidget(Form)
        self.Container.setMinimumSize(QtCore.QSize(500, 200))
        self.Container.setMaximumSize(QtCore.QSize(500, 200))
        self.Container.setStyleSheet("border-radius:20px;\n"
"background-color:#f7f7f7;")
        self.Container.setObjectName("Container")
        self.gridLayout = QtWidgets.QGridLayout(self.Container)
        self.gridLayout.setContentsMargins(15, 5, 15, 5)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ChartType_label = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.ChartType_label.setFont(font)
        self.ChartType_label.setObjectName("ChartType_label")
        self.verticalLayout_2.addWidget(self.ChartType_label)
        self.TimePeriod_label = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.TimePeriod_label.setFont(font)
        self.TimePeriod_label.setObjectName("TimePeriod_label")
        self.verticalLayout_2.addWidget(self.TimePeriod_label)
        self.TransactioType_label = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.TransactioType_label.setFont(font)
        self.TransactioType_label.setObjectName("TransactioType_label")
        self.verticalLayout_2.addWidget(self.TransactioType_label)
        self.dataType_label = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.dataType_label.setFont(font)
        self.dataType_label.setObjectName("dataType_label")
        self.verticalLayout_2.addWidget(self.dataType_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chartType_comboBox = QtWidgets.QComboBox(self.Container)
        self.chartType_comboBox.setStyleSheet("QComboBox {\n"
"\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/Icon/icons8-arrow-down-16.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #cccccc;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: #e6e6e6;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down-arrow-icon.png); /* Replace with your own down arrow icon */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #e6e6e6;\n"
"    selection-color: #333333;\n"
"}\n"
"")
        self.chartType_comboBox.setObjectName("chartType_comboBox")
        self.chartType_comboBox.addItem("")
        self.chartType_comboBox.addItem("")
        self.chartType_comboBox.addItem("")
        self.verticalLayout.addWidget(self.chartType_comboBox)
        self.timePeriod_comboBox = QtWidgets.QComboBox(self.Container)
        self.timePeriod_comboBox.setStyleSheet("QComboBox {\n"
"\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/Icon/icons8-arrow-down-16.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #cccccc;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: #e6e6e6;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down-arrow-icon.png); /* Replace with your own down arrow icon */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #e6e6e6;\n"
"    selection-color: #333333;\n"
"}\n"
"")
        self.timePeriod_comboBox.setObjectName("timePeriod_comboBox")
        self.timePeriod_comboBox.addItem("")
        self.timePeriod_comboBox.addItem("")
        self.timePeriod_comboBox.addItem("")
        self.timePeriod_comboBox.addItem("")
        self.verticalLayout.addWidget(self.timePeriod_comboBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sales_radioButton = QtWidgets.QRadioButton(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sales_radioButton.setFont(font)
        self.sales_radioButton.setStyleSheet("QRadioButton {\n"
"    spacing: 8px; /* Space between indicator and text */\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f9f9f9;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #b3b3b3;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    border: 2px solid #999999;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"")
        self.sales_radioButton.setObjectName("sales_radioButton")
        self.horizontalLayout_3.addWidget(self.sales_radioButton)
        self.returns_radioButton = QtWidgets.QRadioButton(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.returns_radioButton.setFont(font)
        self.returns_radioButton.setStyleSheet("QRadioButton {\n"
"    spacing: 8px; /* Space between indicator and text */\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f9f9f9;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #b3b3b3;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    border: 2px solid #999999;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"")
        self.returns_radioButton.setObjectName("returns_radioButton")
        self.horizontalLayout_3.addWidget(self.returns_radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.productName_radioButton = QtWidgets.QRadioButton(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.productName_radioButton.setFont(font)
        self.productName_radioButton.setStyleSheet("QRadioButton {\n"
"    spacing: 8px; /* Space between indicator and text */\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f9f9f9;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #b3b3b3;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    border: 2px solid #999999;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"")
        self.productName_radioButton.setObjectName("productName_radioButton")
        self.horizontalLayout_4.addWidget(self.productName_radioButton)
        self.Category_radioButton = QtWidgets.QRadioButton(self.Container)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Category_radioButton.setFont(font)
        self.Category_radioButton.setStyleSheet("QRadioButton {\n"
"    spacing: 8px; /* Space between indicator and text */\n"
"    font: 14px \'Segoe UI\', sans-serif;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #cccccc;\n"
"    background-color: #f9f9f9;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #b3b3b3;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    border: 2px solid #999999;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"")
        self.Category_radioButton.setObjectName("Category_radioButton")
        self.horizontalLayout_4.addWidget(self.Category_radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Container, 0, 0, 1, 1)
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.setMinimumSize(QtCore.QSize(250, 50))
        self.generateButton.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.generateButton.setFont(font)
        self.generateButton.setMouseTracking(True)
        self.generateButton.setTabletTracking(True)
        self.generateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generateButton.setStyleSheet("QPushButton {\n"
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
        self.generateButton.setObjectName("generateButton")
        self.gridLayout_2.addWidget(self.generateButton, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LagayanNgChart = QtWidgets.QWidget(Form)
        self.LagayanNgChart.setMinimumSize(QtCore.QSize(1600, 0))
        self.LagayanNgChart.setStyleSheet("background-color:#f7f7f7;")
        self.LagayanNgChart.setObjectName("LagayanNgChart")
        self.verticalLayout_3.addWidget(self.LagayanNgChart)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ChartType_label.setText(_translate("Form", "Chart Type:"))
        self.TimePeriod_label.setText(_translate("Form", "Time Period:"))
        self.TransactioType_label.setText(_translate("Form", "Transaction Type:"))
        self.dataType_label.setText(_translate("Form", "Data Type:"))
        self.chartType_comboBox.setItemText(0, _translate("Form", "Line Chart"))
        self.chartType_comboBox.setItemText(1, _translate("Form", "Pie Chart"))
        self.chartType_comboBox.setItemText(2, _translate("Form", "Bar Chart"))
        self.timePeriod_comboBox.setItemText(0, _translate("Form", "Today"))
        self.timePeriod_comboBox.setItemText(1, _translate("Form", "Last Week"))
        self.timePeriod_comboBox.setItemText(2, _translate("Form", "Last Month"))
        self.timePeriod_comboBox.setItemText(3, _translate("Form", "This Year"))
        self.sales_radioButton.setText(_translate("Form", "Sales"))
        self.returns_radioButton.setText(_translate("Form", "Returns"))
        self.productName_radioButton.setText(_translate("Form", "Product Name"))
        self.Category_radioButton.setText(_translate("Form", "Category"))
        self.generateButton.setText(_translate("Form", "Generate"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
