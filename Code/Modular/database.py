# -*- coding: utf-8 -*-

import sqlite3
import shutil
import os
import threading
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1040, 880)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1001, 600))
        self.frame.setStyleSheet("background-color: #fff;\n"
"border: 3px solid black;\n"
"border-color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: green;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: green;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: green;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database Manager"))
        self.label_2.setText(_translate("Form", "Active Database:"))
        self.label_3.setText(_translate("Form", "database here"))
        self.label_4.setText(_translate("Form", "Last Backup:"))
        self.label_5.setText(_translate("Form", "date and time here"))
        self.label_6.setText(_translate("Form", "Last Backup:"))
        self.label_7.setText(_translate("Form", "date and time of last backup here"))
        self.pushButton_3.setText(_translate("Form", "Backup Schedule"))
        self.pushButton.setText(_translate("Form", "Restore Database"))
        self.pushButton_2.setText(_translate("Form", "Manual Backup"))


class DatabaseTab(QtWidgets.QWidget):
    backupCompleted = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(DatabaseTab, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Load UI from Ui_Form class
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self)
        self.frame = self.ui_form.frame
        
        # Initialize scheduler stop event
        self.scheduler_stop_event = threading.Event()

        # Customize labels and set initial text (replace with dynamic data if needed)
        self.ui_form.label.setText("Database Options")
        self.ui_form.label_2.setText("Active Database:")
        self.ui_form.label_3.setText("j7h.db")  # Replace with actual database name
        self.ui_form.label_4.setText("Last Backup:")
        self.ui_form.label_5.setText("2024-06-25")  # Replace with actual last backup date/time
        self.ui_form.label_6.setText("Current Automatic Backup Time:")
        self.ui_form.label_7.setText("Not scheduled")  # Replace with actual automatic backup time

        # Connect buttons from Ui_Form to corresponding methods
        self.ui_form.pushButton_2.clicked.connect(self.manual_backup)
        self.ui_form.pushButton.clicked.connect(self.restore_backup)
        self.ui_form.pushButton_3.clicked.connect(self.schedule_backup)
        
        # Initialize scheduler thread variable
        self.scheduler_thread = None
        
        self.update_schedule_label()
        self.backupCompleted.connect(self.updateBackupLabel)
    
    def updateBackupLabel(self, backup_time):
        self.ui_form.label_5.setText(backup_time)

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
            self.ui_form.label_5.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))

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
                    self.ui_form.label_3.setText("j7h.db")
                    
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
                self.ui_form.label_7.setText(time_edit.text())

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
                self.ui_form.label_7.setText(scheduled_time_str)
            else:
                self.ui_form.label_7.setText("Not scheduled")

            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to retrieve schedule from database: {str(e)}")

    def backup_scheduler(self, scheduled_time):
        try:
            while not self.scheduler_stop_event.wait(60):  # Check every minute
                current_time = datetime.now().time()
                if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute:
                    self.perform_auto_backup()
                    self.scheduler_stop_event.set()  # Stop the scheduler after one backup
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error in backup scheduler: {str(e)}")

    def perform_auto_backup(self):
        try:
            # Ensure "backups" folder exists in the script directory
            script_dir = os.path.dirname(os.path.realpath(__file__))
            backups_dir = os.path.join(script_dir, "backups")
            if not os.path.exists(backups_dir):
                os.makedirs(backups_dir)

            # Generate backup file name with current date and time
            current_datetime = QtCore.QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
            backup_filename = f"j7h_backup_{current_datetime}.db"
            backup_path = os.path.join(backups_dir, backup_filename)

            # Copy database file to backup location
            shutil.copyfile("j7h.db", backup_path)

            # Update labels with new backup date and time
            self.ui_form.label_5.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))

            # Emit signal for UI update
            self.backupCompleted.emit(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))

            QtWidgets.QMessageBox.information(self, "Backup Successful", "Backup saved successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error during backup: {str(e)}")
