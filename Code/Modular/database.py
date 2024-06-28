# -*- coding: utf-8 -*-

import logging
import os
import shutil
import sqlite3
import threading
import time
from datetime import datetime
import datetime
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog, QVBoxLayout, QLabel, QDateEdit, QDialogButtonBox, QComboBox, QGroupBox
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import QDate
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
        Form.setWindowTitle(_translate("Form", "Jewell 7 Hardware"))
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
        
from assets import settings_rc
logging.basicConfig(level=logging.DEBUG)

class DatabaseTab(QtWidgets.QWidget):
    backupCompleted = QtCore.pyqtSignal(str)

    def __init__(self, user_id, parent=None):
        super(DatabaseTab, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)

        self.user_id = user_id 
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self)
        self.report_customized = False
        self.selected_table_name = None
        self.selected_time_period = None
        self.selected_start_date = None
        self.selected_end_date = None

        self.ui_form.manualBackup_button.clicked.connect(self.manual_backup)
        self.ui_form.restoreDatabase_button.clicked.connect(self.restore_backup)
        self.ui_form.backupSchedule_button.clicked.connect(self.schedule_backup)
        self.ui_form.GenerateReport_button.clicked.connect(self.generate_report)
        self.ui_form.CustomizeReport_button.clicked.connect(self.customize_report)
        
        self.scheduler_thread = None
        
        self.update_schedule_label()
        self.backupCompleted.connect(self.updateBackupLabel)
        self.scheduler_stop_event = threading.Event()
        
        # Create a vertical layout for widget 2 and Container 1
        widget2_container_layout = QtWidgets.QVBoxLayout()
        widget2_container_layout.addWidget(self.ui_form.widget_2)
        widget2_container_layout.addWidget(self.ui_form.Container1)

        # Create a vertical layout for widget 4 and widget 5
        widget4_widget5_layout = QtWidgets.QVBoxLayout()
        widget4_widget5_layout.addWidget(self.ui_form.widget_4)
        widget4_widget5_layout.addWidget(self.ui_form.widget_5)

        # Add the vertical layouts to the main horizontal layout
        self.layout.addLayout(widget2_container_layout)
        self.layout.addLayout(widget4_widget5_layout)

    def manual_backup(self):
        # Implement manual backup functionality
        try:
            # Ensure "backups" folder exists in the script directory
            script_dir = os.path.dirname(os.path.realpath(__file__))
            backups_dir = os.path.join(script_dir, "backups")
            if not os.path.exists(backups_dir):
                os.makedirs(backups_dir)

            # Connect to the database
            conn = sqlite3.connect("j7h.db")
            cursor = conn.cursor()

            # Generate backup file name with current date and time
            current_datetime = QtCore.QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
            backup_filename = f"j7h_backup_{current_datetime}.db"
            backup_path = os.path.join(backups_dir, backup_filename)

            # Copy database file to backup location
            shutil.copyfile("j7h.db", backup_path)

            # Close database connection
            conn.close()

            # Update labels with new backup date and time
            self.ui_form.LastBackup_Data.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))

            QtWidgets.QMessageBox.information(self, "Backup Successful", "Backup saved successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error during backup: {str(e)}")

    def restore_backup(self):
        try:
            # Ensure "backups" folder exists in the script directory
            script_dir = os.path.dirname(os.path.realpath(__file__))
            backups_dir = os.path.join(script_dir, "backups")

            # List all backup files in the backups folder
            backup_files = [f for f in os.listdir(backups_dir) if f.endswith(".db")]

            if not backup_files:
                QtWidgets.QMessageBox.information(self, "No Backups", "No backup files found.")
                return

            # Create a dialog to select a backup file
            dialog = QtWidgets.QDialog()
            dialog.setWindowTitle("Restore Backup")
            layout = QtWidgets.QVBoxLayout()
            
            list_widget = QtWidgets.QListWidget()
            list_widget.addItems(backup_files)
            layout.addWidget(list_widget)
            
            button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
            layout.addWidget(button_box)
            
            dialog.setLayout(layout)
            
            def restore_selected_backup():
                selected_item = list_widget.currentItem()
                if selected_item:
                    backup_filename = selected_item.text()
                    backup_path = os.path.join(backups_dir, backup_filename)
                    # Replace current database with selected backup
                    shutil.copyfile(backup_path, "j7h.db")
                    
                    # Update displayed database name
                    self.ui_form.ActiveDatabase_Data.setText("j7h.db")
                    
                    # Inform the user that the restore was successful and the app will restart
                    message_box = QtWidgets.QMessageBox()
                    message_box.setWindowTitle("Restore Successful")
                    message_box.setText("Database restored successfully. The application will restart.")
                    message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    message_box.exec_()
                    
                    # Set a delay before restarting the application
                    QtCore.QTimer.singleShot(1000, self.restart_application)
                    
                    dialog.accept()
                else:
                    QtWidgets.QMessageBox.warning(self, "No Selection", "Please select a backup file to restore.")
            
            button_box.accepted.connect(restore_selected_backup)
            button_box.rejected.connect(dialog.reject)
            
            dialog.exec_()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error during restore: {str(e)}")

    def restart_application(self):
        from selection_screen import Selection
        QtWidgets.QApplication.instance().activeWindow().close()
        self.new_window = QtWidgets.QMainWindow()
        self.selection_ui = Selection()
        self.selection_ui.setupUi(self.new_window)
        self.new_window.showFullScreen()
        self.close()


    def connect_to_database(self, db_path):
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            print(f"Connected to {db_path}")
            # Perform any additional setup or UI updates here if needed
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to connect to database: {str(e)}")
 
    def schedule_backup(self):
        try:
            # Create a time edit widget
            time_edit = QtWidgets.QTimeEdit()
            time_edit.setDisplayFormat("h:mm AP")

            # Create a dialog with the time edit widget and OK and Cancel buttons
            dialog = QtWidgets.QDialog()
            dialog.setWindowTitle("Schedule Backup")
            dialog_layout = QtWidgets.QVBoxLayout()
            dialog_layout.addWidget(QtWidgets.QLabel("Enter backup time:"))
            dialog_layout.addWidget(time_edit)
            button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
            dialog_layout.addWidget(button_box)
            dialog.setLayout(dialog_layout)
            button_box.accepted.connect(dialog.accept)
            button_box.rejected.connect(dialog.reject)

            # Show the dialog and get the result
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                scheduled_time = time_edit.time().toPyTime()
                self.ui_form.label_8.setText(time_edit.text())

                # Stop any previous scheduler thread
                if self.scheduler_thread and self.scheduler_thread.is_alive():
                    self.scheduler_stop_event.set()
                    self.scheduler_thread.join()

                # Start a new scheduler thread
                self.scheduler_stop_event.clear()
                self.scheduler_thread = threading.Thread(target=self.backup_scheduler, args=(scheduled_time,), daemon=True)
                self.scheduler_thread.start()

                # Insert the scheduled time into the database
                self.insert_schedule_into_db(scheduled_time)

                QtWidgets.QMessageBox.information(self, "Scheduled Backup", f"Backup scheduled for {time_edit.text()}.")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error scheduling backup: {str(e)}")

    def insert_schedule_into_db(self, scheduled_time):
        try:
            conn = sqlite3.connect("j7h.db")
            cursor = conn.cursor()

            # Insert scheduled time into backup_schedule table
            cursor.execute("INSERT INTO backup_schedule (scheduled_time, created_at) VALUES (?, ?)", (scheduled_time.strftime("%H:%M %p"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to insert schedule into database: {str(e)}")

    def update_schedule_label(self):
        try:
            conn = sqlite3.connect("j7h.db")
            cursor = conn.cursor()

            # Retrieve the latest scheduled time from backup_schedule table
            cursor.execute("SELECT scheduled_time FROM backup_schedule ORDER BY created_at DESC LIMIT 1")
            result = cursor.fetchone()

            if result:
                scheduled_time_str = result[0]
                self.ui_form.label_8.setText(scheduled_time_str)
            else:
                self.ui_form.label_8.setText("Not scheduled")

            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to retrieve schedule from database: {str(e)}")

    def backup_scheduler(self, scheduled_time):
        try:
            while not self.scheduler_stop_event.is_set():
                current_time = datetime.now().time()
                if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute:
                    QtCore.QMetaObject.invokeMethod(self, "perform_auto_backup", QtCore.Qt.QueuedConnection)
                    self.scheduler_stop_event.set()  # Stop the scheduler after one backup
                time.sleep(60)  # Check every minute
        except Exception as e:
            logging.error(f"Error in backup scheduler: {str(e)}")

    @QtCore.pyqtSlot()
    def perform_auto_backup(self):
        try:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            backups_dir = os.path.join(script_dir, "backups")
            if not os.path.exists(backups_dir):
                os.makedirs(backups_dir)

            current_datetime = QtCore.QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
            backup_filename = f"j7h_backup_{current_datetime}.db"
            backup_path = os.path.join(backups_dir, backup_filename)

            shutil.copyfile("j7h.db", backup_path)

            backup_time_str = QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
            logging.info(f"Backup completed at {backup_time_str}")

            self.backupCompleted.emit(backup_time_str)
            QtWidgets.QMessageBox.information(self, "Backup Successful", "Backup saved successfully.")
        except Exception as e:
            logging.error(f"Error during backup: {str(e)}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Error during backup: {str(e)}")

    @QtCore.pyqtSlot(str)
    def updateBackupLabel(self, backup_time):
        self.ui_form.LastBackup_Data.setText(backup_time)
       
           
        # Reports Functions
        
    def generate_report(self):
        try:
            # Check if the report has been customized
            if not self.report_customized:
                QtWidgets.QMessageBox.warning(self, "Format Missing", "Please customize your report first.")
                return

            # Assuming you have variables to hold the selected table name and time period
            table_name = self.selected_table_name
            time_period = self.selected_time_period
            start_date = self.selected_start_date
            end_date = self.selected_end_date

            if table_name == "sales":
                table_name = "transactions"
            elif table_name == "returns":
                table_name = "returns"  # Ensure the correct table name is used for returns
            
            # Connect to the database
            conn = sqlite3.connect("j7h.db")
            cursor = conn.cursor()

            # Get the current user's first and last name
            cursor.execute("SELECT first_name, last_name FROM users WHERE user_id = ?", (self.user_id,))
            user_name = cursor.fetchone()
            user_full_name = f"{user_name[0]} {user_name[1]}"

            # Query data from your database
            today = datetime.date.today()
            if time_period == "Today":
                if table_name == "transactions":
                    cursor.execute(f"""
                        SELECT t.transaction_id, t.date, t.time, t.customer, t.total_price, u.first_name 
                        FROM {table_name} t
                        JOIN users u ON t.user_id = u.user_id
                        WHERE t.date = ?
                    """, (today,))
                elif table_name == "returns":
                    cursor.execute(f"SELECT return_id, return_date, product_name, brand, var, size, qty FROM {table_name} WHERE return_date=?", (today,))
            elif time_period == "This Week":
                start_of_week = today - datetime.timedelta(days=today.weekday())
                if table_name == "transactions":
                    cursor.execute(f"""
                        SELECT t.transaction_id, t.date, t.time, t.customer, t.total_price, u.first_name 
                        FROM {table_name} t
                        JOIN users u ON t.user_id = u.user_id
                        WHERE t.date BETWEEN ? AND ?
                    """, (start_of_week, today))
                elif table_name == "returns":
                    cursor.execute(f"SELECT return_id, return_date, product_name, brand, var, size, qty FROM {table_name} WHERE return_date BETWEEN ? AND ?", (start_of_week, today))
            elif time_period == "This Month":
                start_of_month = today.replace(day=1)
                if table_name == "transactions":
                    cursor.execute(f"""
                        SELECT t.transaction_id, t.date, t.time, t.customer, t.total_price, u.first_name 
                        FROM {table_name} t
                        JOIN users u ON t.user_id = u.user_id
                        WHERE t.date BETWEEN ? AND ?
                    """, (start_of_month, today))
                elif table_name == "returns":
                    cursor.execute(f"SELECT return_id, return_date, product_name, brand, var, size, qty FROM {table_name} WHERE return_date BETWEEN ? AND ?", (start_of_month, today))
            elif time_period == "Custom":
                if table_name == "transactions":
                    cursor.execute(f"""
                        SELECT t.transaction_id, t.date, t.time, t.customer, t.total_price, u.first_name 
                        FROM {table_name} t
                        JOIN users u ON t.user_id = u.user_id
                        WHERE t.date BETWEEN ? AND ?
                    """, (start_date, end_date))
                elif table_name == "returns":
                    cursor.execute(f"SELECT return_id, return_date, product_name, brand, var, size, qty FROM {table_name} WHERE return_date BETWEEN ? AND ?", (start_date, end_date))
            
            rows = cursor.fetchall()

            # Close database connection
            conn.close()

            # Prepare report content as an HTML table
            report_content = "<html><body>"
            report_content += "<div style='text-align:center;'>"
            report_content += "<h1><b>Jewell 7 Hardware</b></h1>"
            report_content += f"<h3>{table_name.capitalize()} Report</h3>"
            report_content += f"<p>Generated by: {user_full_name}</p>"
            report_content += f"<p>Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
            report_content += "</div>"
            report_content += "<table border='1' cellspacing='0' cellpadding='5' style='margin: auto;'>"

            if table_name == "transactions":
                report_content += "<tr><th>Transaction ID</th><th>Date</th><th>Time</th><th>Customer</th><th>Total Price</th><th>Cashier</th></tr>"
                total_sales = 0
                total_revenue = 0
                for row in rows:
                    transaction_str = (
                        f"<tr>"
                        f"<td>{row[0]}</td>"
                        f"<td>{row[1]}</td>"
                        f"<td>{row[2]}</td>"
                        f"<td>{row[3]}</td>"
                        f"<td>₱{float(row[4]):.2f}</td>"  # Convert to float before formatting
                        f"<td>{row[5]}</td>"
                        f"</tr>"
                    )
                    report_content += transaction_str
                    total_sales += 1
                    total_revenue += float(row[4])
            elif table_name == "sales":
                report_content += "<tr><th>Sales ID</th><th>Date</th><th>Product</th><th>Quantity</th><th>Total Price</th></tr>"
                total_sales = 0
                total_revenue = 0
                for row in rows:
                    sales_str = (
                        f"<tr>"
                        f"<td>{row[0]}</td>"
                        f"<td>{row[1]}</td>"
                        f"<td>{row[2]}</td>"
                        f"<td>{row[3]}</td>"
                        f"<td>₱{float(row[4]):.2f}</td>"  # Convert to float before formatting
                        f"</tr>"
                    )
                    report_content += sales_str
                    total_sales += 1
                    total_revenue += float(row[4])
            elif table_name == "returns":
                report_content += "<tr><th>Return ID</th><th>Return Date</th><th>Product Name</th><th>Brand</th><th>Variety</th><th>Size</th><th>Quantity</th></tr>"
                for row in rows:
                    returns_str = (
                        f"<tr>"
                        f"<td>{row[0]}</td>"
                        f"<td>{row[1]}</td>"
                        f"<td>{row[2]}</td>"
                        f"<td>{row[3]}</td>"
                        f"<td>{row[4]}</td>"
                        f"<td>{row[5]}</td>"
                        f"<td>{row[6]}</td>"
                        f"</tr>"
                    )
                    report_content += returns_str

            report_content += "</table>"

            # Add summary details
            if table_name in ["transactions", "sales"]:
                report_content += "<p>Summary:</p>"
                report_content += f"<p>Total Sales: {total_sales}</p>"
                report_content += f"<p>Total Revenue: ₱{total_revenue:.2f}</p>"

            report_content += "</body></html>"


            # Display report in a preview window
            preview_dialog = QMessageBox()
            preview_dialog.setWindowTitle("Generated Report")
            preview_dialog.setText(report_content)
            preview_dialog.exec_()

            # Save report as PDF
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("PDF files (*.pdf)")
            file_dialog.setDefaultSuffix("pdf")
            if file_dialog.exec_() == QFileDialog.Accepted:
                file_path = file_dialog.selectedFiles()[0]
                if not file_path.lower().endswith('.pdf'):
                    file_path += '.pdf'

                # Create PDF document
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)

                document = QTextDocument()
                document.setHtml(report_content)
                document.print_(printer)

                QMessageBox.information(self, "Report Saved", f"Report saved as {file_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating report: {str(e)}")


    def customize_report(self):
        dialog = QDialog()
        dialog.setWindowTitle("Customize Report")
        layout = QVBoxLayout()

        # Create a combo box for selecting the time period
        time_period_label = QLabel("Select Time Period:")
        time_period_combo = QComboBox()
        time_period_combo.addItem("Today")
        time_period_combo.addItem("This Week")
        time_period_combo.addItem("This Month")
        time_period_combo.addItem("Custom")

        # Create a combo box for selecting the data type
        data_type_label = QLabel("Select Data Type:")
        data_type_combo = QComboBox()
        data_type_combo.addItem("Sales")
        data_type_combo.addItem("Returns")

        # Create a date edit widget for custom date range
        custom_date_label = QLabel("Select Custom Date Range:")
        custom_date_start = QDateEdit()
        custom_date_end = QDateEdit()

        # Create a button box with OK and Cancel buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # Add widgets to the layout
        layout.addWidget(time_period_label)
        layout.addWidget(time_period_combo)
        layout.addWidget(data_type_label)
        layout.addWidget(data_type_combo)

        # Add custom date range widgets
        custom_date_group = QGroupBox("Custom Date Range")
        custom_date_group.setCheckable(True)
        custom_date_group.setChecked(False)
        custom_date_layout = QVBoxLayout()
        custom_date_group.setLayout(custom_date_layout)
        custom_date_layout.addWidget(custom_date_label)
        custom_date_layout.addWidget(custom_date_start)
        custom_date_layout.addWidget(custom_date_end)
        layout.addWidget(custom_date_group)

        layout.addWidget(button_box)

        dialog.setLayout(layout)

        # Connect signals and slots
        button_box.accepted.connect(lambda: [self.set_report_customization(time_period_combo.currentText(), data_type_combo.currentText(), custom_date_start.date().toPyDate(), custom_date_end.date().toPyDate()), dialog.accept()])
        button_box.rejected.connect(dialog.reject)
        time_period_combo.currentIndexChanged.connect(lambda index: custom_date_group.setChecked(index == 3))
        custom_date_group.toggled.connect(lambda checked: custom_date_label.setEnabled(checked))
        custom_date_group.toggled.connect(lambda checked: custom_date_start.setEnabled(checked))
        custom_date_group.toggled.connect(lambda checked: custom_date_end.setEnabled(checked))

        # Show the dialog
        dialog.exec_()


    def set_report_customization(self, time_period, table_name, start_date, end_date):
        self.report_customized = True
        self.selected_table_name = table_name.lower()
        self.selected_time_period = time_period
        self.selected_start_date = start_date
        self.selected_end_date = end_date
