from PyQt5 import QtWidgets, QtCore
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

        # Time period layout
        self.transaction_type_layout = QtWidgets.QHBoxLayout()
        self.transaction_type_label = QtWidgets.QLabel("Transaction Type:", self)
        self.transaction_type_combo = QtWidgets.QComboBox(self)
        self.transaction_type_combo.addItems(["Returns", "Sales"])
        self.transaction_type_layout.addWidget(self.transaction_type_label)
        self.transaction_type_layout.addWidget(self.transaction_type_combo)
        self.controls_layout.addLayout(self.transaction_type_layout)

        # Data type layout
        self.data_type_layout = QtWidgets.QHBoxLayout()
        self.data_type_label = QtWidgets.QLabel("Data Type:", self)
        self.data_type_product_name = QtWidgets.QRadioButton("Product Name", self)
        self.data_type_category = QtWidgets.QRadioButton("Category", self)
        self.data_type_reason = QtWidgets.QRadioButton("Reason", self)
        self.data_type_product_name.setChecked(True)
        self.data_type_layout.addWidget(self.data_type_label)
        self.data_type_layout.addWidget(self.data_type_product_name)
        self.data_type_layout.addWidget(self.data_type_category)
        self.data_type_layout.addWidget(self.data_type_reason)
        self.controls_layout.addLayout(self.data_type_layout)

        # Handling Reason visibility based on transaction type
        self.transaction_type_combo.currentIndexChanged.connect(self.toggle_reason_visibility)
        self.toggle_reason_visibility()
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

        # Initially hide data type options for Line Chart
        self.toggle_data_type_visibility()

    def toggle_data_type_visibility(self):
        chart_type = self.chart_type_combo.currentText()   
        transaction_type = self.transaction_type_combo.currentText()
        if chart_type == "Line Chart":
            self.data_type_label.hide()
            self.data_type_product_name.hide()
            self.data_type_category.hide()
            self.data_type_reason.hide()
        else:
            self.data_type_label.show()
            self.data_type_product_name.show()
            self.data_type_category.show()
            if transaction_type == "Sales":
                self.data_type_reason.hide()
            else:
                self.data_type_reason.show()
    # Function to toggle Reason visibility
    def toggle_reason_visibility(self):
        chart_type = self.chart_type_combo.currentText()  
        transaction_type = self.transaction_type_combo.currentText()
        if transaction_type == "Sales" or chart_type == "Line Chart":
            self.data_type_reason.hide()
        else:
            self.data_type_reason.show()


    def generate_analytics_data(self):
        chart_type = self.chart_type_combo.currentText()
        time_period = self.time_period_combo.currentText()
        transaction_type = self.transaction_type_combo.currentText()
        if self.data_type_product_name.isChecked():
            data_type = "product" 
        elif self.data_type_category.isChecked():
            data_type = "category"
        else:
            data_type = "reason"

        self.update_chart(chart_type, time_period, transaction_type, data_type)

    def update_chart(self, chart_type, time_period, transaction_type, data_type):
        data_df = self.fetch_data(data_type, time_period)

        current_datetime = datetime.today()
        current_date = current_datetime.strftime('%b %d')

        six_days_ago = current_datetime - timedelta(days=6)
        six_days_ago_date = six_days_ago.strftime('%b %d')
        week_range = f"{six_days_ago_date} - {current_date}"

        thirty_days_ago = current_datetime - timedelta(days=28)
        thirty_days_ago_date = thirty_days_ago.strftime('%b %d')
        month_range = f"{thirty_days_ago_date} - {current_date}"

        current_year = current_datetime.year
        start_date = datetime(current_year, 1, 1).strftime('%b')
        end_date = datetime(current_year, 12, 31).strftime('%b %Y')
        year_range = f"{start_date} - {end_date}"

        # Check if data_df or data_df are not empty before proceeding
        if not data_df.empty:
            self.clear_chart_placeholder()  # Clear the placeholder before generating new chart
            if chart_type == "Pie Chart":
                if transaction_type == "Sales":
                    if data_type == "product":    
                        if time_period == "Today":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product ({current_date})", data_type)
                        elif time_period == "Last Week":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product ({week_range})", data_type)
                        elif time_period == "Last Month":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product ({month_range})", data_type)
                        else:
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product ({year_range})", data_type)
                    else:
                        if time_period == "Today":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product Category ({current_date})", data_type)
                        elif time_period == "Last Week":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product Category ({week_range})", data_type)
                        elif time_period == "Last Month":
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product Category ({month_range})", data_type)
                        else:
                            self.generate_pie_chart(data_df, f"{time_period}'s Sales Distribution Per Product Category ({year_range})", data_type)
                else:
                    if data_type == "product":    
                        if time_period == "Today":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product ({current_date})", data_type)
                        elif time_period == "Last Week":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product ({week_range})", data_type)
                        elif time_period == "Last Month":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product ({month_range})", data_type)
                        else:
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product ({year_range})", data_type)
                    elif data_type == "category":
                        if time_period == "Today":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product Category ({current_date})", data_type)
                        elif time_period == "Last Week":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product Category ({week_range})", data_type)
                        elif time_period == "Last Month":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product Category ({month_range})", data_type)
                        else:
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Product Category ({year_range})", data_type)
                    else:
                        if time_period == "Today":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Reason ({current_date})", data_type)
                        elif time_period == "Last Week":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Reason ({week_range})", data_type)
                        elif time_period == "Last Month":
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Reason ({month_range})", data_type)
                        else:
                            self.generate_pie_chart(data_df, f"{time_period}'s Customer Returns Distribution Per Reason ({year_range})", data_type)
            elif chart_type == "Line Chart":
                if transaction_type == "Sales":    
                    if time_period == "Today":
                        self.generate_line_chart(data_df, f'Sales {time_period} ({current_date})')
                    elif time_period == "Last Week":
                        self.generate_line_chart(data_df, f'Sales {time_period} ({week_range})')
                    elif time_period == "Last Month":
                        self.generate_line_chart(data_df, f'Sales {time_period}')
                    else:
                        self.generate_line_chart(data_df, f'Sales {time_period} ({year_range})')
                else:
                    if time_period == "Today":
                        self.generate_line_chart(data_df, f'Customer Returns {time_period} ({current_date})')
                    elif time_period == "Last Week":
                        self.generate_line_chart(data_df, f'Customer Returns {time_period} ({week_range})')
                    elif time_period == "Last Month":
                        self.generate_line_chart(data_df, f'Customer Returns {time_period}')
                    else:
                        self.generate_line_chart(data_df, f'Customer Returns {time_period} ({year_range})')
            elif chart_type == "Bar Chart":
                if transaction_type == "Sales":
                    if data_type == "product":
                        if time_period == "Today":
                            self.generate_bar_chart(data_df, f'Most Sold Product {time_period} ({current_date})', data_type)
                        elif time_period == "Last Week":
                            self.generate_bar_chart(data_df, f'Most Sold Product {time_period} ({week_range})', data_type)
                        elif time_period == "Last Month":
                            self.generate_bar_chart(data_df, f'Most Sold Product {time_period} ({month_range})', data_type)
                        else:
                            self.generate_bar_chart(data_df, f'Most Sold Product {time_period} ({year_range})', data_type)
                    else:
                        if time_period == "Today":
                            self.generate_bar_chart(data_df, f'Most Sold Product Category {time_period} ({current_date})', data_type)
                        elif time_period == "Last Week":
                            self.generate_bar_chart(data_df, f'Most Sold Product Category {time_period} ({week_range})', data_type)
                        elif time_period == "Last Month":
                            self.generate_bar_chart(data_df, f'Most Sold Product Category {time_period} ({month_range})', data_type)
                        else:
                            self.generate_bar_chart(data_df, f'Most Sold Product Category {time_period} ({year_range})', data_type)
                else:
                    if data_type == "product":
                        if time_period == "Today":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products {time_period} ({current_date})', data_type)
                        elif time_period == "Last Week":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products {time_period} ({week_range})', data_type)
                        elif time_period == "Last Month":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products {time_period} ({month_range})', data_type)
                        else:
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products {time_period} ({year_range})', data_type)
                    elif data_type == "category":
                        if time_period == "Today":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products Per Category {time_period} ({current_date})', data_type)
                        elif time_period == "Last Week":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products Per Category {time_period} ({week_range})', data_type)
                        elif time_period == "Last Month":
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products Per Category {time_period} ({month_range})', data_type)
                        else:
                            self.generate_bar_chart(data_df, f'Most Frequently Returned Products Per Category {time_period} ({year_range})', data_type)
                    else:
                        if time_period == "Today":
                            self.generate_bar_chart(data_df, f'Most Common Reason for Customer Returns {time_period} ({current_date})', data_type)
                        elif time_period == "Last Week":
                            self.generate_bar_chart(data_df, f'Most Common Reason for Customer Returns {time_period} ({week_range})', data_type)
                        elif time_period == "Last Month":
                            self.generate_bar_chart(data_df, f'Most Common Reason for Customer Returns {time_period} ({month_range})', data_type)
                        else:
                            self.generate_bar_chart(data_df, f'Most Common Reason for Customer Returns {time_period} ({year_range})', data_type)
        else:
            print("Transaction Data is empty.")

    def fetch_data(self, data_type, time_period):
        conn = sqlite3.connect("j7h.db")
        transaction_type = self.transaction_type_combo.currentText()
        
        if transaction_type == "Sales":
            if data_type == "product":
                query_transaction = f"""
                SELECT product_name, date, time
                FROM transactions
                """
            else:
                query_transaction = f"""
                SELECT category, date, time
                FROM transactions
                """
        else:
            if data_type == "product":
                query_transaction = f"""
                SELECT product_name, date, time
                FROM returns
                """
            elif data_type == "category":
                query_transaction = f"""
                SELECT category, date, time
                FROM returns
                """
            else:
                query_transaction = f"""
                SELECT reason, date, time
                FROM returns
                """
        data_df = pd.read_sql_query(query_transaction, conn)
        conn.close()

        # Combine 'date' and 'time' columns into a single datetime column
        data_df['datetime'] = pd.to_datetime(data_df['date'] + ' ' + data_df['time'], format='%Y-%m-%d %I:%M %p')

        # Filter data based on the selected time period
        now = datetime.now()
        start_date = now - timedelta(days=1) if time_period == 'Today' else \
                    now - timedelta(weeks=1) if time_period == 'Last Week' else \
                    now - timedelta(days=30) if time_period == 'Last Month' else \
                    now - timedelta(days=365)
        data_df = data_df[data_df['datetime'] >= start_date]

        return data_df

    def generate_line_chart(self, data_df, title):
        transaction_type = self.transaction_type_combo.currentText()
        fig, ax = plt.subplots(figsize=(10, 5))
        if transaction_type == "Sales":
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                counts = [len(data_df[(data_df['datetime'] >= start) & (data_df['datetime'] < end)]) for start, end in times_24h]
                times_labels = [start.strftime('%I %p') for start, end in times_24h]
                ax.plot(times_labels, counts, marker='o', label='Sales')

                ax.set_xlabel('Time')
                ax.set_ylabel('Number of Transactions')

            elif self.time_period_combo.currentText() == 'Last Week':
                days = [(datetime.now() - timedelta(days=i)).date() for i in range(6, -1, -1)]
                counts = [len(data_df[data_df['datetime'].dt.date == day]) for day in days]
                days_labels = [day.strftime('%b %d') for day in days]  # Formatting as 'Month Day'

                fig, ax = plt.subplots()
                ax.plot(days_labels, counts, marker='o', color='r', label='Actual Sales')

                # Implementing Linear Regression
                X = np.arange(len(days)).reshape(-1, 1)
                y = np.array(counts)

                model = LinearRegression()
                model.fit(X, y)

                # Predict for an additional day
                next_day_index = len(days)
                next_day_pred = model.predict([[next_day_index]])[0]

                # Extend labels for prediction day
                next_day_date = (datetime.now() + timedelta(days=1)).date()
                days_labels.append(next_day_date.strftime('%b %d'))  # Next day date in 'Month Day' format
                counts.append(next_day_pred)
                ax.plot(days_labels, counts, linestyle='--', color='r', label='Estimated Sales')

                ax.set_xlabel('Days')
                ax.set_ylabel('Number of Transactions')

            elif self.time_period_combo.currentText() == 'Last Month':
                weeks = [(datetime.now() - timedelta(days=i * 7), datetime.now() - timedelta(days=(i - 1) * 7)) for i in range(4, 0, -1)]
                counts = [len(data_df[(data_df['datetime'] >= start) & (data_df['datetime'] < end)]) for start, end in weeks]
                weeks_labels = [start.strftime('%B %d') + ' - ' + (end - timedelta(days=1)).strftime('%d') for start, end in weeks]
                ax.plot(weeks_labels, counts, marker='o', label='Sales')

                ax.set_xlabel('Weeks')
                ax.set_ylabel('Number of Transactions')

            elif self.time_period_combo.currentText() == 'This Year':
                months = [datetime(datetime.now().year, m, 1) for m in range(1, 13)]
                counts = [len(data_df[data_df['datetime'].dt.month == month.month]) for month in months]
                months_labels = [month.strftime('%b') for month in months]
                ax.plot(months_labels, counts, marker='o', label='Sales')

                ax.set_xlabel('Months')
                ax.set_ylabel('Number of Transactions')
        else:
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                counts = [len(data_df[(data_df['datetime'] >= start) & (data_df['datetime'] < end)]) for start, end in times_24h]
                times_labels = [start.strftime('%I %p') for start, end in times_24h]
                ax.plot(times_labels, counts, marker='o', label='Returns')

                ax.set_xlabel('Time')
                ax.set_ylabel('Number of Returns')

            elif self.time_period_combo.currentText() == 'Last Week':
                days = [(datetime.now() - timedelta(days=i)).date() for i in range(6, -1, -1)]
                counts = [len(data_df[data_df['datetime'].dt.date == day]) for day in days]
                days_labels = [day.strftime('%b %d') for day in days]  # Formatting as 'Month Day'

                fig, ax = plt.subplots()
                ax.plot(days_labels, counts, marker='o', label='Returns')

                ax.set_xlabel('Days')
                ax.set_ylabel('Number of Returns')

            elif self.time_period_combo.currentText() == 'Last Month':
                weeks = [(datetime.now() - timedelta(days=i * 7), datetime.now() - timedelta(days=(i - 1) * 7)) for i in range(4, 0, -1)]
                counts = [len(data_df[(data_df['datetime'] >= start) & (data_df['datetime'] < end)]) for start, end in weeks]
                weeks_labels = [start.strftime('%B %d') + ' - ' + (end - timedelta(days=1)).strftime('%d') for start, end in weeks]
                ax.plot(weeks_labels, counts, marker='o', label='Returns')

                ax.set_xlabel('Weeks')
                ax.set_ylabel('Number of Returns')

            elif self.time_period_combo.currentText() == 'This Year':
                months = [datetime(datetime.now().year, m, 1) for m in range(1, 13)]
                counts = [len(data_df[data_df['datetime'].dt.month == month.month]) for month in months]
                months_labels = [month.strftime('%b') for month in months]
                ax.plot(months_labels, counts, marker='o', label='Returns')

                ax.set_xlabel('Months')
                ax.set_ylabel('Number of Returns')

        ax.set_title(title)
        ax.grid(True)
        plt.xticks(rotation=45)

        # Add legend
        ax.legend()

        # Adding the chart canvas to the layout
        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)

    def generate_pie_chart(self, data_df, title, data_type):
        transaction_type = self.transaction_type_combo.currentText()
        if transaction_type == "Sales":
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                filtered_df = data_df[data_df['datetime'].apply(lambda x: any(start <= x < end for start, end in times_24h))]

            elif self.time_period_combo.currentText() == 'Last Week':
                start_date = (datetime.now() - timedelta(days=7)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'Last Month':
                start_date = (datetime.now() - timedelta(days=30)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'This Year':
                start_date = datetime(datetime.now().year, 1, 1)
                filtered_df = data_df[data_df['datetime'] >= start_date]

            if data_type == "product":
                counts = filtered_df["product_name"].value_counts().head(8)
            else:
                counts = filtered_df["category"].value_counts().head(8)
        else:
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                filtered_df = data_df[data_df['datetime'].apply(lambda x: any(start <= x < end for start, end in times_24h))]

            elif self.time_period_combo.currentText() == 'Last Week':
                start_date = (datetime.now() - timedelta(days=7)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'Last Month':
                start_date = (datetime.now() - timedelta(days=30)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'This Year':
                start_date = datetime(datetime.now().year, 1, 1)
                filtered_df = data_df[data_df['datetime'] >= start_date]

            if data_type == "product":
                counts = filtered_df["product_name"].value_counts().head(8)
            elif data_type == "category":
                counts = filtered_df["category"].value_counts().head(8)
            else:
                counts = filtered_df["reason"].value_counts().head(8)

        fig, ax = plt.subplots(figsize=(8, 6))
        wedges, texts, autotexts = ax.pie(counts, labels=counts.index, autopct=self.autopct_format(counts), startangle=90)
        
        ax.set_title(title)
        ax.axis('equal')
        
        # Adding a legend
        ax.legend(wedges, counts.index, title=data_type, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        # Replace chart placeholder with the pie chart
        canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(canvas)


    def generate_bar_chart(self, data_df, title, data_type):
        transaction_type = self.transaction_type_combo.currentText()
        if transaction_type == "Sales":
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                filtered_df = data_df[data_df['datetime'].apply(lambda x: any(start <= x < end for start, end in times_24h))]

            elif self.time_period_combo.currentText() == 'Last Week':
                start_date = (datetime.now() - timedelta(days=7)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'Last Month':
                start_date = (datetime.now() - timedelta(days=30)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'This Year':
                start_date = datetime(datetime.now().year, 1, 1)
                filtered_df = data_df[data_df['datetime'] >= start_date]

            if data_type == "product":
                counts = filtered_df["product_name"].value_counts().head(8)
            else:
                counts = filtered_df["category"].value_counts().head(8)
        else:
            if self.time_period_combo.currentText() == 'Today':
                times_24h = [(datetime.now().replace(hour=h, minute=0, second=0, microsecond=0),
                            datetime.now().replace(hour=h + 1, minute=0, second=0, microsecond=0))
                            for h in range(8, 19)]  # Business hours from 8 AM to 5 PM
                filtered_df = data_df[data_df['datetime'].apply(lambda x: any(start <= x < end for start, end in times_24h))]

            elif self.time_period_combo.currentText() == 'Last Week':
                start_date = (datetime.now() - timedelta(days=7)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'Last Month':
                start_date = (datetime.now() - timedelta(days=30)).date()
                filtered_df = data_df[data_df['datetime'].dt.date >= start_date]

            elif self.time_period_combo.currentText() == 'This Year':
                start_date = datetime(datetime.now().year, 1, 1)
                filtered_df = data_df[data_df['datetime'] >= start_date]

            if data_type == "product":
                counts = filtered_df["product_name"].value_counts().head(8)
            elif data_type == "category":
                counts = filtered_df["category"].value_counts().head(8)
            else:
                counts = filtered_df["reason"].value_counts().head(8)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(counts.index, counts, color='skyblue')  # Use barh for horizontal bar chart
        ax.set_title(title)
        ax.set_ylabel(data_type.capitalize())
        ax.set_xlabel('Items Sold')
        plt.yticks(rotation=0)  # Rotate y-axis labels if needed

        ax.grid(True)

        # Create a FigureCanvas to display the plot in Qt
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
