# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerSelection.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerSelection(object):
    def setupUi(self, registerSelection):
        registerSelection.setObjectName("registerSelection")
        registerSelection.resize(1150, 820)
        registerSelection.setStyleSheet("background-color: #FCFEFE;")
        registerSelection.setAnimated(True)
        registerSelection.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(registerSelection)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logoContainer = QtWidgets.QWidget(self.centralwidget)
        self.logoContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.logoContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.logoContainer.setStyleSheet("QWidget {\n"
"    background-color: #81cdc6;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"\n"
"}")
        self.logoContainer.setObjectName("logoContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.logoContainer)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.logoContainer)
        self.logo.setMinimumSize(QtCore.QSize(450, 50))
        self.logo.setMaximumSize(QtCore.QSize(450, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
"\n"
"border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.logoContainer, 0, 0, 1, 1)
        self.whiteContainer = QtWidgets.QWidget(self.centralwidget)
        self.whiteContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.whiteContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.whiteContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.whiteContainer.setAutoFillBackground(False)
        self.whiteContainer.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
" border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}")
        self.whiteContainer.setInputMethodHints(QtCore.Qt.ImhNone)
        self.whiteContainer.setObjectName("whiteContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.whiteContainer)
        self.verticalLayout.setContentsMargins(45, 9, 45, 60)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backButton = QtWidgets.QPushButton(self.whiteContainer)
        self.backButton.setMinimumSize(QtCore.QSize(0, 0))
        self.backButton.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.backButton.setFont(font)
        self.backButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color:#3d3d3d    ;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #265C42;\n"
"}\n"
"")
        self.backButton.setIconSize(QtCore.QSize(16, 16))
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.Title = QtWidgets.QLabel(self.whiteContainer)
        self.Title.setMinimumSize(QtCore.QSize(0, 10))
        self.Title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("border:none;")
        self.Title.setObjectName("Title")
        self.verticalLayout.addWidget(self.Title)
        self.staffButton = QtWidgets.QPushButton(self.whiteContainer)
        self.staffButton.setMinimumSize(QtCore.QSize(150, 50))
        self.staffButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.staffButton.setFont(font)
        self.staffButton.setMouseTracking(True)
        self.staffButton.setTabletTracking(True)
        self.staffButton.setStyleSheet("QPushButton {\n"
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
        self.staffButton.setObjectName("staffButton")
        self.verticalLayout.addWidget(self.staffButton)
        self.adminButton = QtWidgets.QPushButton(self.whiteContainer)
        self.adminButton.setMinimumSize(QtCore.QSize(150, 50))
        self.adminButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.adminButton.setFont(font)
        self.adminButton.setMouseTracking(True)
        self.adminButton.setTabletTracking(True)
        self.adminButton.setStyleSheet("QPushButton {\n"
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
        self.adminButton.setObjectName("adminButton")
        self.verticalLayout.addWidget(self.adminButton)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.whiteContainer, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        registerSelection.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(registerSelection)
        self.statusbar.setObjectName("statusbar")
        registerSelection.setStatusBar(self.statusbar)

        self.retranslateUi(registerSelection)
        QtCore.QMetaObject.connectSlotsByName(registerSelection)

    def retranslateUi(self, registerSelection):
        _translate = QtCore.QCoreApplication.translate
        registerSelection.setWindowTitle(_translate("registerSelection", "resgisterSelection"))
        self.backButton.setText(_translate("registerSelection", "←"))
        self.Title.setText(_translate("registerSelection", "Please choose between Staff or Admin"))
        self.staffButton.setText(_translate("registerSelection", "Staff"))
        self.adminButton.setText(_translate("registerSelection", "Admin"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerSelection = QtWidgets.QMainWindow()
    ui = Ui_registerSelection()
    ui.setupUi(registerSelection)
    registerSelection.show()
    sys.exit(app.exec_())
