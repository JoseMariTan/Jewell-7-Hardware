import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from staffRegistration import StaffRegistration
from adminRegistration import AdminRegistration

class Register(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setupConnections()

    def setupUi(self, registerSelection):
        registerSelection.resize(1150, 820)
        registerSelection.setStyleSheet("background-color: #FCFEFE;")
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        # Logo Container
        self.logoContainer = QtWidgets.QWidget(self)
        self.logoContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.logoContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.logoContainer.setStyleSheet("QWidget {\n"
                                         "    background-color: #81cdc6;\n"
                                         "    border-style: solid;\n"
                                         "    border-color: black;\n"
                                         "    border-width: 1px;\n"
                                         "}\n")
        self.logoContainer.setObjectName("logoContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.logoContainer)
        self.gridLayout.setObjectName("gridLayout")
        
        # Logo Image
        self.logo = QtWidgets.QLabel(self.logoContainer)
        self.logo.setMinimumSize(QtCore.QSize(450, 50))
        self.logo.setMaximumSize(QtCore.QSize(450, 290))
        self.logo.setStyleSheet("image: url(:/images/received_836614531712349.png);\n"
                                "border:none;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.logoContainer, 0, 0, 1, 1)
        
        # White Container (Main Content Area)
        self.whiteContainer = QtWidgets.QWidget(self)
        self.whiteContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.whiteContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.whiteContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.whiteContainer.setAutoFillBackground(False)
        self.whiteContainer.setStyleSheet("QWidget {\n"
                                          "    background-color: #fff;\n"
                                          "    border-style: solid;\n"
                                          "    border-color: black;\n"
                                          "    border-width: 1px;\n"
                                          "}\n")
        self.whiteContainer.setInputMethodHints(QtCore.Qt.ImhNone)
        self.whiteContainer.setObjectName("whiteContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.whiteContainer)
        self.verticalLayout.setContentsMargins(45, 9, 45, 60)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Back Button
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
                                      "}\n")
        self.backButton.setIconSize(QtCore.QSize(16, 16))
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        
        # Title Label
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
        
        # Staff Button
        self.staffButton = QtWidgets.QPushButton(self.whiteContainer)
        self.staffButton.setMinimumSize(QtCore.QSize(150, 50))
        self.staffButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.staffButton.setFont(font)
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
        
        # Admin Button
        self.adminButton = QtWidgets.QPushButton(self.whiteContainer)
        self.adminButton.setMinimumSize(QtCore.QSize(150, 50))
        self.adminButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adminButton.setFont(font)
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

        self.retranslateUi(registerSelection)
        QtCore.QMetaObject.connectSlotsByName(registerSelection)
    
    from assets import logo_rc

    def retranslateUi(self, registerSelection):
        _translate = QtCore.QCoreApplication.translate
        registerSelection.setWindowTitle(_translate("registerSelection", "Register Selection"))
        self.backButton.setText(_translate("registerSelection", "←"))
        self.Title.setText(_translate("registerSelection", "Please choose between Staff or Admin"))
        self.staffButton.setText(_translate("registerSelection", "Staff"))
        self.adminButton.setText(_translate("registerSelection", "Admin"))

    def setupConnections(self):
        self.staffButton.clicked.connect(self.openStaffRegistration)
        self.adminButton.clicked.connect(self.openAdminRegistration)
        self.backButton.clicked.connect(self.go_back)

    def openStaffRegistration(self):
        QtWidgets.QApplication.instance().activeWindow().close()
        self.staff_registration = StaffRegistration()
        self.staff_registration.showFullScreen()
        self.close()

    def openAdminRegistration(self):
        QtWidgets.QApplication.instance().activeWindow().close()
        self.admin_registration = AdminRegistration()
        self.admin_registration.showFullScreen()
        self.close()

    def go_back(self):
        QtWidgets.QApplication.instance().activeWindow().close()
        self.new_window = QtWidgets.QMainWindow()
        from selection_screen import Selection
        self.new_window = QtWidgets.QMainWindow()
        self.selection_ui = Selection()
        self.selection_ui.setupUi(self.new_window)
        self.new_window.showFullScreen()
        self.close()
