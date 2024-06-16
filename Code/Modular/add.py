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
    time = (datetime.now() + timedelta(minutes=random.randint(0, 1000))).strftime("%I:%M %p")
    date = datetime.now().strftime("%Y-%m-%d")
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
