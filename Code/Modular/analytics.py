from PyQt5 import QtWidgets, QtCore
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime, timedelta

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
        self.time_period_combo.addItems(["Last 24 Hours", "Last Week", "Last Month", "Last Year"])
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
        transaction_type = "purchases" if self.transaction_type_sales.isChecked() else "returns"
        data_type = "product_name" if self.data_type_product_name.isChecked() else "category"

        self.update_chart(chart_type, time_period, transaction_type, data_type)

    def update_chart(self, chart_type, time_period, transaction_type, data_type):
        df = self.fetch_data(transaction_type, data_type, time_period)
        
        if df is not None and not df.empty:
            if chart_type == "Pie Chart":
                self.generate_pie_chart(df, f' Customer {transaction_type.capitalize()} Distribution from the {time_period} per {data_type.capitalize()}', data_type)
            # Add other chart types here as needed

    def fetch_data(self, transaction_type, data_type, time_period):
        conn = sqlite3.connect("j7h.db")
        query = f"""
        SELECT {data_type}, date, time, type
        FROM transactions
        WHERE type = ?
        """

        df = pd.read_sql_query(query, conn, params=(transaction_type,))
        conn.close()

        # Combine 'date' and 'time' columns into a single datetime column
        df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%Y-%m-%d %I:%M %p')
        
        # Filter data based on the selected time period
        now = datetime.now()
        start_date = now - timedelta(days=1) if time_period == 'Last 24 Hours' else \
                     now - timedelta(weeks=1) if time_period == 'Last Week' else \
                     now - timedelta(days=30) if time_period == 'Last Month' else \
                     now - timedelta(days=365)
        df = df[df['datetime'] >= start_date]
        
        return df

    def generate_pie_chart(self, df, title, data_type):
        if data_type == "product_name":
            counts = df['product_name'].value_counts().head(8)
        else:
            counts = df['category'].value_counts().head(8)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.pie(counts, labels=counts.index, autopct=self.autopct_format(counts), startangle=90)
        ax.set_title(title)
        ax.axis('equal')

        # Replace chart placeholder with the pie chart
        canvas = FigureCanvas(fig)
        self.clear_chart_placeholder()
        self.chart_layout.addWidget(canvas)

    def autopct_format(self, values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f'{pct:.1f}% ({val:d})'
        return my_format

    def clear_chart_placeholder(self):
        # Clear all widgets in the chart layout
        for i in reversed(range(self.chart_layout.count())):
            widget = self.chart_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    analytics_tab = AnalyticsTab()
    window.setCentralWidget(analytics_tab)
    window.show()
    sys.exit(app.exec_())
