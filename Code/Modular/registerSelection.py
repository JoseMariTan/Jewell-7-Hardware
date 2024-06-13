import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from staffRegistration import StaffRegistration
from adminRegistration import AdminRegistration

class RegSelection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Selection):
        Selection.setObjectName("Select Registration")
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
        
        self.infoLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setText("Please choose between Staff and Admin")
        self.verticalLayout.addWidget(self.infoLabel)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        
        # Button for Staff
        self.staffButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.staffButton.setFont(font)
        self.staffButton.setStyleSheet("background-color:#53C851;")
        self.staffButton.setDefault(True)
        self.staffButton.setFlat(False)
        self.staffButton.setObjectName("staffButton")
        self.verticalLayout_2.addWidget(self.staffButton)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        
        # Button for Admin
        self.adminButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.adminButton.setFont(font)
        self.adminButton.setStyleSheet("background-color:#53C851;")
        self.adminButton.setDefault(True)
        self.adminButton.setFlat(False)
        self.adminButton.setObjectName("adminButton")
        self.verticalLayout_2.addWidget(self.adminButton)
        
        self.verticalLayout.addLayout(self.verticalLayout_2)
        Selection.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Selection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 22))
        self.menubar.setObjectName("menubar")
        Selection.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(Selection)
        self.statusbar.setObjectName("statusbar")
        Selection.setStatusBar(self.statusbar)

        # functionalities
        self.staffButton.clicked.connect(self.open_staff_registration) 
        self.adminButton.clicked.connect(self.open_admin_registration) 

        self.retranslateUi(Selection)
        QtCore.QMetaObject.connectSlotsByName(Selection)

    def retranslateUi(self, Selection):
        _translate = QtCore.QCoreApplication.translate
        Selection.setWindowTitle(_translate("SelectionScreen", "Select LOA"))
        self.Jewell7_label.setText(_translate("SelectionScreen", "Jewell 7"))
        self.Hardware_label.setText(_translate("SelectionScreen", "Hardware"))
        self.infoLabel.setText(_translate("SelectionScreen", "Please choose between Staff and Admin"))
        self.staffButton.setText(_translate("SelectionScreen", "Staff"))  
        self.adminButton.setText(_translate("SelectionScreen", "Admin"))  
    
    def open_staff_registration(self):
        self.staff_registration_window = StaffRegistration()
        self.staff_registration_window.show()
        self.close()

    def open_admin_registration(self):
        self.admin_registration_window = AdminRegistration()
        self.admin_registration_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    selection_window = RegSelection()
    selection_window.show()
    sys.exit(app.exec_())
