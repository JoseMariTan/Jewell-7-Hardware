import sqlite3
import uuid
from datetime import datetime, timedelta
import random

# Connect to the database
conn = sqlite3.connect('j7h.db')
cursor = conn.cursor()

# Define sample data for random generation
customers = ["Elden", "Genshin", "Wuther", "Notnac", "test"]
products = [
    {"name": "Plywood", "brand": None, "model": "Oak", "size": "12x16"},
    {"name": "Cement", "brand": "max", "model": None, "size": "10kg"},
    {"name": "Tablet", "brand": "BrandC", "model": "ModelZ", "size": "10 inch"},
    {"name": "Plier", "brand": "Ace", "model": "Blue", "size": None},
    {"name": "Smartphone", "brand": "BrandB", "model": "ModelY", "size": "6 inch"},
    {"name": "Monitor", "brand": "BrandD", "model": "ModelW", "size": "24 inch"},
    {"name": "Nail Polish ni Yohan", "brand": "wana", "model": "black", "size": None},
    {"name": "Paint", "brand": "Boysen", "model": "Black", "size": "10kg"},
    {"name": "Hammer", "brand": "Acer", "model": "Wood", "size": "12mm"},
    {"name": "Wrench", "brand": "Acer", "model": "Gray", "size": None},
    {"name": "Wrench", "brand": None, "model": "Black", "size": None}
]
transaction_types = ["purchase"]

# Generate and insert 150 new rows
for _ in range(150):
    transaction_id = str(uuid.uuid4())
    total_price = round(random.uniform(10, 3000), 2)
    qty = random.randint(1, 5)
    customer = random.choice(customers)
    product = random.choice(products)
    
    # Generate a random date between January 2024 and December 2024
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    date = random_date.strftime("%Y-%m-%d")
    
    # Generate a random time between 8:00 AM and 6:00 PM
    start_time = datetime.strptime("08:00 AM", "%I:%M %p")
    end_time = datetime.strptime("06:00 PM", "%I:%M %p")
    random_time = start_time + timedelta(minutes=random.randint(0, int((end_time - start_time).total_seconds() // 60)))
    time = random_time.strftime("%I:%M %p")

    user_id = random.randint(1, 10)
    status = None
    reference_id = None
    type = random.choice(transaction_types)
    category_id = random.randint(1, 21)
    transaction_number = random.randint(300, 999)

    cursor.execute('''
        INSERT INTO transactions (transaction_id, total_price, qty, customer, product_name, brand, var, size, time, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (transaction_id, total_price, qty, customer, product["name"], product["brand"], product["model"], product["size"], time, date))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
