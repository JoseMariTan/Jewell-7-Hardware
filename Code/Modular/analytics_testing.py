import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to generate pie chart for top products of a specific type
def generate_pie_chart(df, title, transaction_type):
    # Filter by transaction type
    df = df[df['type'] == transaction_type]
    
    # Calculate product counts
    product_counts = df['product_name'].value_counts()
    
    # Select top 8 products by frequency
    top_products = product_counts.head(8)
    
    # Create the pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(top_products, labels=top_products.index, autopct=autopct_format(top_products), startangle=90)
    ax.set_title(title)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

# Function to format autopct labels
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}% ({val:d})'
    return my_format

# Function to retrieve data for a given time period
def get_data_for_period(df, start_date):
    return df[df['datetime'] >= start_date]

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('j7h.db')

# Step 2: Write the SQL query to get all transactions with type
sql_query = "SELECT product_name, date, time, type FROM transactions"

# Step 3: Read the SQL query results into a Pandas DataFrame
df = pd.read_sql_query(sql_query, conn)

# Step 4: Close the database connection
conn.close()

# Combine 'date' and 'time' columns into a single datetime column
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%Y-%m-%d %I:%M %p')

# Get the current time
now = datetime.now()

# Define the time ranges
last_day = now - timedelta(days=1)
last_week = now - timedelta(days=7)
last_month = now - timedelta(days=30)
last_year = now - timedelta(days=365)

# Generate pie charts for each time period and each type
types = df['type'].unique()  # Get all unique types from the dataframe

for type_ in types:
    generate_pie_chart(get_data_for_period(df, last_day), f'Product Sales ({type_}) in Last 24 Hours', type_)
    generate_pie_chart(get_data_for_period(df, last_week), f'Product Sales ({type_}) in Last 7 Days', type_)
    generate_pie_chart(get_data_for_period(df, last_month), f'Product Sales ({type_}) in Last 30 Days', type_)
    generate_pie_chart(get_data_for_period(df, last_year), f'Product Sales ({type_}) in Last Year', type_)
