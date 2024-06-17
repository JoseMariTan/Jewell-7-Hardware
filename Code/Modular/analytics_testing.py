import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to parse the datetime string
def parse_datetime(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p")

# Function to fetch data from SQLite database
def fetch_data(type_value, date_start=None, date_end=None):
    conn = sqlite3.connect('j7h.db')
    query = """
    SELECT date, time
    FROM transactions
    WHERE type = ?
    """
    params = [type_value]
    
    if date_start and date_end:
        query += " AND date BETWEEN ? AND ?"
        params.extend([date_start, date_end])
        
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to count frequency within business hours
def count_frequency(datetimes, times_24h):
    frequency = [0] * len(times_24h)
    for dt in datetimes:
        for i, hour_range in enumerate(times_24h):
            if hour_range[0] <= dt < hour_range[1]:
                frequency[i] += 1
                break
    return frequency

# Function to count frequency within each day of the week
def count_daily_frequency(datetimes, start_date, end_date):
    frequency = [0] * 7  # Initialize frequency list for 7 days (Monday to Sunday)
    for dt in datetimes:
        transaction_date = dt.date()
        if start_date <= transaction_date <= end_date:
            day_index = (transaction_date - start_date).days
            frequency[day_index] += 1
    return frequency

# Function to count weekly frequency for a given date range
def count_weekly_frequency(datetimes, week_ranges):
    frequency = [0] * len(week_ranges)
    for dt in datetimes:
        for i, (start_date, end_date) in enumerate(week_ranges):
            if start_date <= dt.date() <= end_date:
                frequency[i] += 1
                break
    return frequency

# Connect to the SQLite database and fetch data for purchases and returns
purchases_data_today = fetch_data('purchases', datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
returns_data_today = fetch_data('returns', datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
purchases_data_week = fetch_data('purchases', (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
returns_data_week = fetch_data('returns', (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))

# Parse datetime strings into datetime objects
datetimes_purchases_today = [parse_datetime(row[0], row[1]) for row in purchases_data_today]
datetimes_returns_today = [parse_datetime(row[0], row[1]) for row in returns_data_today]
datetimes_purchases_week = [parse_datetime(row[0], row[1]) for row in purchases_data_week]
datetimes_returns_week = [parse_datetime(row[0], row[1]) for row in returns_data_week]

# Get the current date and time
end_time = datetime.now()

# Define business operating hours (8 AM to 5 PM)
start_hour = 8
end_hour = 17

# Create a list of hourly ranges covering business hours for today
times_24h_today = []
for hour in range(start_hour, end_hour):
    hour_start = end_time.replace(hour=hour, minute=0, second=0, microsecond=0)
    hour_end = hour_start + timedelta(hours=1)  # 1-hour intervals
    times_24h_today.append((hour_start, hour_end))

# Count the frequency of purchases and returns per hourly interval for today
frequency_purchases_today = count_frequency(datetimes_purchases_today, times_24h_today)
frequency_returns_today = count_frequency(datetimes_returns_today, times_24h_today)

# Plotting the data for Purchases today
plt.figure(figsize=(10, 5))
plt.plot([time[0].strftime("%I %p") for time in times_24h_today], frequency_purchases_today, marker='o')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Customer Purchases Today')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the data for Returns today
plt.figure(figsize=(10, 5))
plt.plot([time[0].strftime("%I %p") for time in times_24h_today], frequency_returns_today, marker='o', color='orange')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Customer Returns Today')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Define the start and end dates for the previous week
start_date_week = end_time - timedelta(days=6)
end_date_week = end_time

# Count the frequency of purchases and returns per daily interval for the current week
frequency_purchases_week = count_daily_frequency(datetimes_purchases_week, start_date_week.date(), end_date_week.date())
frequency_returns_week = count_daily_frequency(datetimes_returns_week, start_date_week.date(), end_date_week.date())

# Plotting the data for Purchases over the current week
plt.figure(figsize=(10, 5))
days_of_week = [(start_date_week + timedelta(days=i)).strftime('%a') for i in range(7)]
plt.plot(days_of_week, frequency_purchases_week, marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Frequency')
plt.title('Customer Purchases This Week')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the data for Returns over the current week
plt.figure(figsize=(10, 5))
plt.plot(days_of_week, frequency_returns_week, marker='o', color='orange')
plt.xlabel('Day of the Week')
plt.ylabel('Frequency')
plt.title('Customer Returns This Week')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate the start and end dates for each week of the previous month
weeks = []
for i in range(3, -1, -1):
    end_date = (end_time - timedelta(days=i * 7)).date()
    start_date = end_date - timedelta(days=6)
    weeks.append((start_date, end_date))

# Connect to the SQLite database and fetch data for purchases and returns for the previous month
start_date_month = weeks[0][0]
end_date_month = weeks[-1][1]

purchases_data_month = fetch_data('purchases', start_date_month.strftime('%Y-%m-%d'), end_date_month.strftime('%Y-%m-%d'))
returns_data_month = fetch_data('returns', start_date_month.strftime('%Y-%m-%d'), end_date_month.strftime('%Y-%m-%d'))

# Parse datetime strings into datetime objects
datetimes_purchases_month = [parse_datetime(row[0], row[1]) for row in purchases_data_month]
datetimes_returns_month = [parse_datetime(row[0], row[1]) for row in returns_data_month]

# Count the frequency of purchases and returns per weekly interval for the previous month
frequency_purchases_month = count_weekly_frequency(datetimes_purchases_month, weeks)
frequency_returns_month = count_weekly_frequency(datetimes_returns_month, weeks)

# Dynamic x values for the weeks
weeks_of_month = ['Week 1', 'Week 2', 'Week 3', 'Week 4']

# Plotting the data for Purchases over the previous month
plt.figure(figsize=(10, 5))
plt.plot(weeks_of_month, frequency_purchases_month, marker='o')
plt.xlabel('Weeks')
plt.ylabel('Frequency')
plt.title('Customer Purchases Last Month')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the data for Returns over the previous month
plt.figure(figsize=(10, 5))
plt.plot(weeks_of_month, frequency_returns_month, marker='o', color='orange')
plt.xlabel('Weeks')
plt.ylabel('Frequency')
plt.title('Customer Returns Last Month')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate start and end dates for the current year
start_date_year = datetime(datetime.now().year, 1, 1)
end_date_year = datetime(datetime.now().year, 12, 31)

# Fetch purchases and returns data for the current year
purchases_data_year = fetch_data('purchases', start_date_year.strftime('%Y-%m-%d'), end_date_year.strftime('%Y-%m-%d'))
returns_data_year = fetch_data('returns', start_date_year.strftime('%Y-%m-%d'), end_date_year.strftime('%Y-%m-%d'))

# Parse datetime strings into datetime objects
datetimes_purchases_year = [parse_datetime(row[0], row[1]) for row in purchases_data_year]
datetimes_returns_year = [parse_datetime(row[0], row[1]) for row in returns_data_year]

# Function to count monthly frequency for the current year
def count_monthly_frequency(datetimes, year):
    frequency = [0] * 12  # Initialize frequency list for 12 months
    for dt in datetimes:
        if dt.year == year:
            month_index = dt.month - 1  # January is 0, December is 11
            frequency[month_index] += 1
    return frequency

# Count the frequency of purchases and returns per month for the current year
frequency_purchases_year = count_monthly_frequency(datetimes_purchases_year, datetime.now().year)
frequency_returns_year = count_monthly_frequency(datetimes_returns_year, datetime.now().year)

# Months of the year
months_of_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plotting the data for Purchases over the current year
plt.figure(figsize=(10, 5))
plt.plot(months_of_year, frequency_purchases_year, marker='o')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Customer Purchases This Year')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the data for Returns over the current year
plt.figure(figsize=(10, 5))
plt.plot(months_of_year, frequency_returns_year, marker='o', color='orange')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Customer Returns This Year')
plt.grid(True)
plt.tight_layout()
plt.show()
