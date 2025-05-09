import json
import random
from faker import Faker
from datetime import timedelta, date

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_RECORDS = 1_000_000  # Total number of records (Shipping records)
NUM_ORDERS = 300_000  # Number of unique orders (Each order will have one shipping)
shipping_methods = ['Standard', 'Express', 'Overnight']
shipping_statuses = ['Pending', 'Shipped', 'Delivered']

# Generate unique order_ids
order_ids = [f"ORD{str(i).zfill(9)}" for i in range(1, NUM_ORDERS + 1)]  # Order IDs like ORD000000001, ORD000000002...

# Generate shipping records
shipping_records = []

for i in range(NUM_RECORDS):
    order_id = random.choice(order_ids)  # Randomly pick an order_id from the available ones
    address = fake.address().replace("\n", ", ")  # Random address, formatted to be a single line
    method = random.choice(shipping_methods)  # Random shipping method
    delivery_date = fake.date_between(start_date='-30d', end_date='+30d')  # Random delivery date within a range of 30 days before or after today
    status = random.choice(shipping_statuses)  # Random shipping status

    shipping_records.append({
        "order_id": order_id,
        "address": address,
        "method": method,
        "delivery_date": str(delivery_date),  # Convert to string for JSON compatibility
        "status": status
    })

# Save to JSON file
with open('shipping.json', 'w') as f:
    json.dump(shipping_records, f, indent=4)

print("✅ Generated 'shipping_1M.json' with 1 million shipping records.")
