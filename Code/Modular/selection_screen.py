import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Login
from registerSelection import RegSelection

class Selection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Selection):
        Selection.setObjectName("SelectionScreen")
        Selection.resize(870, 600)
        self.centralwidget = QtWidgets.QWidget(Selection)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 150, 441, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Jewell7_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Jewell7_label.setFont(font)
        self.Jewell7_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Jewell7_label.setObjectName("Jewell7_label")
        self.verticalLayout.addWidget(self.Jewell7_label)
        self.Hardware_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        self.Hardware_label.setFont(font)
        self.Hardware_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Hardware_label.setObjectName("Hardware_label")
        self.verticalLayout.addWidget(self.Hardware_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.loginButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color:#53C851;")
        self.loginButton.setDefault(True)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.registerButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("background-color:#53C851;")
        self.registerButton.setDefault(True)
        self.registerButton.setFlat(False)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        Selection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Selection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 22))
        self.menubar.setObjectName("menubar")
        Selection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Selection)
        self.statusbar.setObjectName("statusbar")
        Selection.setStatusBar(self.statusbar)

        # functionalitites
        self.loginButton.clicked.connect(self.open_login)
        self.registerButton.clicked.connect(self.open_register)

        self.retranslateUi(Selection)
        QtCore.QMetaObject.connectSlotsByName(Selection)

    def retranslateUi(self, Selection):
        _translate = QtCore.QCoreApplication.translate
        Selection.setWindowTitle(_translate("SelectionScreen", "Selection Screen"))
        self.Jewell7_label.setText(_translate("SelectionScreen", "Jewell 7"))
        self.Hardware_label.setText(_translate("SelectionScreen", "Hardware"))
        self.loginButton.setText(_translate("SelectionScreen", "Login"))
        self.registerButton.setText(_translate("SelectionScreen", "Register"))

    def open_login(self):
        self.login_window = QtWidgets.QMainWindow()
        self.ui = Login()
        self.ui.setupUi(self.login_window)
        self.login_window.show()
        self.close()
    
    def open_register(self):
        self.register_window = RegSelection() 
        self.register_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    selection_window = Selection()
    selection_window.show()
    sys.exit(app.exec_())