from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

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
        self.time_period_combo.addItems(["Today", "Last Week", "Last Month", "This Year"])
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

        # Sales prediction layout (for Line Chart and Last Week)
        self.sales_prediction_layout = QtWidgets.QHBoxLayout()
        self.sales_prediction_label = QtWidgets.QLabel("Sales Prediction:", self)
        self.sales_prediction_yes = QtWidgets.QRadioButton("Yes", self)
        self.sales_prediction_no = QtWidgets.QRadioButton("No", self)
        self.sales_prediction_group = QtWidgets.QButtonGroup(self)
        self.sales_prediction_group.addButton(self.sales_prediction_yes)
        self.sales_prediction_group.addButton(self.sales_prediction_no)
        self.sales_prediction_no.setChecked(True)
        self.sales_prediction_layout.addWidget(self.sales_prediction_label)
        self.sales_prediction_layout.addWidget(self.sales_prediction_yes)
        self.sales_prediction_layout.addWidget(self.sales_prediction_no)
        self.controls_layout.addLayout(self.sales_prediction_layout)

        # generate button
        self.generate_button = QtWidgets.QPushButton("Generate", self)
        self.controls_layout.addWidget(self.generate_button, alignment=QtCore.Qt.AlignRight)

        # Spacer below the generate button
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

        # Connect generate button to a method
        self.generate_button.clicked.connect(self.generate_analytics_data)

        # Connect chart type combo box to visibility handler
        self.chart_type_combo.currentIndexChanged.connect(self.toggle_data_type_visibility)
        self.time_period_combo.currentIndexChanged.connect(self.toggle_sales_prediction_visibility)

        # Initially hide data type options for Line Chart
        self.toggle_data_type_visibility()
        self.toggle_sales_prediction_visibility()

    def toggle_data_type_visibility(self):
        chart_type = self.chart_type_combo.currentText()
        if chart_type == "Line Chart":
            self.data_type_label.hide()
            self.data_type_product_name.hide()
            self.data_type_category.hide()
        else:
            self.data_type_label.show()
            self.data_type_product_name.show()
            self.data_type_category.show()

    def toggle_sales_prediction_visibility(self):
        time_period = self.time_period_combo.currentText()
        chart_type = self.chart_type_combo.currentText()
        if chart_type == "Line Chart" and time_period == "Last Week":
            self.sales_prediction_label.show()
            self.sales_prediction_yes.show()
            self.sales_prediction_no.show()
        else:
            self.sales_prediction_label.hide()
            self.sales_prediction_yes.hide()
            self.sales_prediction_no.hide()

    def generate_analytics_data(self):
        chart_type = self.chart_type_combo.currentText()
        time_period = self.time_period_combo.currentText()
        transaction_type = "purchases" if self.transaction_type_sales.isChecked() else "returns"
        data_type = "product_name" if self.data_type_product_name.isChecked() else "category"
        sales_prediction = self.sales_prediction_yes.isChecked()

        #if self.sales_prediction_yes.isChecked() and self.transaction_type_returns.isChecked():
            #if self.sales_prediction_yes.isChecked() and self.transaction_type_returns.isChecked():
                #QMessageBox.critical(self, "Error", "Prediction cannot be applied to customer returns.")
                #self.sales_prediction_yes.setChecked(False)

        self.update_chart(chart_type, time_period, transaction_type, data_type, sales_prediction)

    def update_chart(self, chart_type, time_period, transaction_type, data_type, sales_prediction):
        df = self.fetch_data(transaction_type, data_type, time_period)

        if df is not None and not df.empty:
            self.clear_chart_placeholder()  # Clear the placeholder before generating new chart
            if chart_type == "Pie Chart":
                self.generate_pie_chart(df, f'Customer {transaction_type.capitalize()} Distribution from the {time_period} per {data_type.capitalize()}', data_type)
            elif chart_type == "Line Chart":
                self.generate_line_chart(df, f'Customer {transaction_type.capitalize()} over {time_period}', data_type, sales_prediction)
            elif chart_type == "Bar Chart":
                self.generate_bar_chart(df, f'Customer {transaction_type.capitalize()} Distribution from the {time_period} per {data_type.capitalize()}')

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
        start_date = now - timedelta(days=1) if time_period == 'Today' else \
                     now - timedelta(weeks=1) if time_period == 'Last Week' else \
                     now - timedelta(days=30) if time_period == 'Last Month' else \
                     now - timedelta(days=365)
        df = df[df['datetime'] >= start_date]

        return df

    def generate_pie_chart(self, df, title, data_type):
        counts = df[data_type].value_counts().head(8)

        fig, ax = plt.subplots(figsize=(8, 6))
        wedges, texts, autotexts = ax.pie(counts, labels=counts.index, autopct=self.autopct_format(counts), startangle=90)
        ax.set_title(title)
        ax.axis('equal')

        # Adding a legend
        ax.legend(wedges, counts.index, title=data_type, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        # Replace chart placeholder with the pie chart
        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)

    def generate_line_chart(self, df, title, data_type, sales_prediction):
        fig, ax = plt.subplots(figsize=(10, 5))

        if self.time_period_combo.currentText() == 'Today':
            times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                        datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                        for h in range(8, 18)]  # Business hours from 8 AM to 5 PM
            counts = [len(df[(df['datetime'] >= start) & (df['datetime'] < end)]) for start, end in times_24h]
            times_labels = [start.strftime('%I %p') for start, end in times_24h]
            ax.plot(times_labels, counts, marker='o', label='Actual Data')

            if sales_prediction and 'returns' not in df['type'].unique():  # Check if sales prediction is enabled and transaction type is not 'returns'
                # Perform prediction only when applicable
                # You can implement your prediction logic here
                pass

        elif self.time_period_combo.currentText() == 'Last Week':
            days = [(datetime.now() - timedelta(days=i)).date() for i in range(6, -1, -1)]
            counts = [len(df[df['datetime'].dt.date == day]) for day in days]
            days_labels = [day.strftime('%a') for day in days]
            ax.plot(days_labels, counts, marker='o', label='Actual Sales', color='blue')

            if sales_prediction and 'returns' not in df['type'].unique():  # Check if sales prediction is enabled and transaction type is not 'returns'
                # Implementing Linear Regression for prediction
                X = np.arange(len(days)).reshape(-1, 1)
                y = np.array(counts)

                model = LinearRegression()
                model.fit(X, y)

                # Predict for an additional day
                next_day_index = len(days)
                next_day_pred = model.predict([[next_day_index]])[0]

                # Extend labels for prediction day
                days_labels.append("Next Day")
                counts.append(next_day_pred)
                ax.plot(days_labels, counts, marker='o', linestyle='--', color='blue', label='Estimated Sales')

        elif self.time_period_combo.currentText() == 'Last Month':
            weeks = [(datetime.now() - timedelta(days=i * 7), datetime.now() - timedelta(days=(i - 1) * 7)) for i in range(4, 0, -1)]
            counts = [len(df[(df['datetime'] >= start) & (df['datetime'] < end)]) for start, end in weeks]
            weeks_labels = [start.strftime('%B %d') + ' - ' + (end - timedelta(days=1)).strftime('%d') for start, end in weeks]
            ax.plot(weeks_labels, counts, marker='o', label='Actual Sales')

            if sales_prediction and 'returns' not in df['type'].unique():  # Check if sales prediction is enabled and transaction type is not 'returns'
                # Perform prediction only when applicable
                # You can implement your prediction logic here
                pass

        elif self.time_period_combo.currentText() == 'This Year':
            months = [datetime(datetime.now().year, m, 1) for m in range(1, 13)]
            counts = [len(df[df['datetime'].dt.month == month.month]) for month in months]
            months_labels = [month.strftime('%b') for month in months]
            ax.plot(months_labels, counts, marker='o', label='Actual Sales')

            if sales_prediction and 'returns' not in df['type'].unique():  # Check if sales prediction is enabled and transaction type is not 'returns'
                # Perform prediction only when applicable
                # You can implement your prediction logic here
                pass

        ax.set_title(title)
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        ax.grid(True)
        plt.xticks(rotation=45)

        # Add legend
        ax.legend()

        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)

    def generate_bar_chart(self, df, title, data_type):
        counts = df[data_type].value_counts().head(8)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(counts.index, counts, color='skyblue')
        ax.set_title(title)
        ax.set_xlabel(data_type.capitalize())
        ax.set_ylabel('Frequency')
        plt.xticks(rotation=45)

        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)

    def clear_chart_placeholder(self):
        while self.chart_layout.count():
            child = self.chart_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def autopct_format(self, values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f'{val} ({pct:.2f}%)'
        return my_format

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    analytics_tab = AnalyticsTab()
    analytics_tab.setWindowTitle('Analytics Dashboard')
    analytics_tab.resize(1200, 800)
    analytics_tab.show()

    app.exec_()
