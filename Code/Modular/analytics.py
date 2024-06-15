from PyQt5 import QtWidgets, QtCore
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class AnalyticsTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AnalyticsTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.main_layout = QtWidgets.QHBoxLayout(self)

        # Left side layout (controls)
        self.controls_layout = QtWidgets.QVBoxLayout()

        # Chart type layout
        self.chart_type_layout = QtWidgets.QHBoxLayout()
        self.chart_type_label = QtWidgets.QLabel("Chart Type:", self)
        self.chart_type_combo = QtWidgets.QComboBox(self)
        self.chart_type_combo.addItems(["Line Chart", "Pie Chart", "Bar Chart"])
        self.chart_type_layout.addWidget(self.chart_type_label)
        self.chart_type_layout.addWidget(self.chart_type_combo)
        self.controls_layout.addLayout(self.chart_type_layout)

        # Time period layout
        self.time_period_layout = QtWidgets.QHBoxLayout()
        self.time_period_label = QtWidgets.QLabel("Time Period:", self)
        self.time_period_combo = QtWidgets.QComboBox(self)
        self.time_period_combo.addItems(["Daily", "Weekly", "Monthly", "Yearly"])
        self.time_period_layout.addWidget(self.time_period_label)
        self.time_period_layout.addWidget(self.time_period_combo)
        self.controls_layout.addLayout(self.time_period_layout)

        # Transaction type layout
        self.transaction_type_layout = QtWidgets.QHBoxLayout()
        self.transaction_type_label = QtWidgets.QLabel("Transaction Type:", self)
        self.transaction_type_sales = QtWidgets.QRadioButton("Sales", self)
        self.transaction_type_returns = QtWidgets.QRadioButton("Returns", self)
        self.transaction_type_group = QtWidgets.QButtonGroup(self)
        self.transaction_type_group.addButton(self.transaction_type_sales)
        self.transaction_type_group.addButton(self.transaction_type_returns)
        self.transaction_type_sales.setChecked(True)
        self.transaction_type_layout.addWidget(self.transaction_type_label)
        self.transaction_type_layout.addWidget(self.transaction_type_sales)
        self.transaction_type_layout.addWidget(self.transaction_type_returns)
        self.controls_layout.addLayout(self.transaction_type_layout)

        # Data type layout
        self.data_type_layout = QtWidgets.QHBoxLayout()
        self.data_type_label = QtWidgets.QLabel("Data Type:", self)
        self.data_type_product_name = QtWidgets.QRadioButton("Product Name", self)
        self.data_type_category = QtWidgets.QRadioButton("Category", self)
        self.data_type_group = QtWidgets.QButtonGroup(self)
        self.data_type_group.addButton(self.data_type_product_name)
        self.data_type_group.addButton(self.data_type_category)
        self.data_type_product_name.setChecked(True)
        self.data_type_layout.addWidget(self.data_type_label)
        self.data_type_layout.addWidget(self.data_type_product_name)
        self.data_type_layout.addWidget(self.data_type_category)
        self.controls_layout.addLayout(self.data_type_layout)

        # Save button
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.controls_layout.addWidget(self.save_button, alignment=QtCore.Qt.AlignRight)

        # Spacer below the save button
        self.controls_layout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.main_layout.addLayout(self.controls_layout, 1)  # Smaller weight for controls layout

        # Spacer between controls and chart placeholder
        self.main_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        # Right side layout (chart placeholder)
        self.chart_layout = QtWidgets.QVBoxLayout()
        self.chart_placeholder = QtWidgets.QLabel("Chart or Graph Placeholder", self)
        self.chart_placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.chart_placeholder.setStyleSheet("border: 1px solid black;")
        self.chart_layout.addWidget(self.chart_placeholder)

        self.main_layout.addLayout(self.chart_layout, 3)  # Larger weight for chart layout

        # Connect save button to a method
        self.save_button.clicked.connect(self.save_analytics_data)

    def save_analytics_data(self):
        chart_type = self.chart_type_combo.currentText()
        time_period = self.time_period_combo.currentText()
        transaction_type = "sales" if self.transaction_type_sales.isChecked() else "returns"
        data_type = "product_name" if self.data_type_product_name.isChecked() else "category"

        # Fetch data from the database
        data = self.fetch_data(transaction_type, data_type, time_period)
        
        # Generate chart based on fetched data and user selections
        self.generate_chart(chart_type, data, transaction_type, data_type, time_period)

    def fetch_data(self, transaction_type, data_type, time_period):
        # Connect to the database
        conn = sqlite3.connect('j7h.db')
        query = f"""
        SELECT {data_type}, date, COUNT(*) as count 
        FROM transactions 
        WHERE type = ? 
        GROUP BY {data_type}, date
        """
        df = pd.read_sql_query(query, conn, params=(transaction_type,))
        conn.close()

        # Resample data based on the selected time period
        df['date'] = pd.to_datetime(df['date'])
        if time_period == "Daily":
            df.set_index('date', inplace=True)
        elif time_period == "Weekly":
            df = df.set_index('date').groupby([pd.Grouper(freq='W'), data_type]).sum().reset_index()
        elif time_period == "Monthly":
            df = df.set_index('date').groupby([pd.Grouper(freq='M'), data_type]).sum().reset_index()
        elif time_period == "Yearly":
            df = df.set_index('date').groupby([pd.Grouper(freq='Y'), data_type]).sum().reset_index()

        return df

    def generate_chart(self, chart_type, data, transaction_type, data_type, time_period):
        fig, ax = plt.subplots()

        if chart_type == "Line Chart":
            for key, grp in data.groupby([data_type]):
                ax.plot(grp['date'], grp['count'], label=key)
            ax.legend(loc='best')
        elif chart_type == "Pie Chart":
            summary = data.groupby(data_type).sum()
            ax.pie(summary['count'], labels=summary.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
        elif chart_type == "Bar Chart":
            summary = data.groupby(data_type).sum().reset_index()
            ax.bar(summary[data_type], summary['count'])

        ax.set_title(f"{chart_type} for {transaction_type} by {data_type} ({time_period})")
        ax.set_xlabel("Date")
        ax.set_ylabel("Count")

        # Clear the previous chart and plot the new one
        for i in reversed(range(self.chart_layout.count())): 
            widgetToRemove = self.chart_layout.itemAt(i).widget()
            self.chart_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    analytics_tab = AnalyticsTab()
    window.setCentralWidget(analytics_tab)
    window.show()
    sys.exit(app.exec_())
