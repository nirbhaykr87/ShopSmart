import json
import random
from faker import Faker
from datetime import timedelta, date

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_RECORDS = 1_000_000  # Total number of records (Returns records)
NUM_ORDERS = 300_000  # Number of unique orders (Each order will have some returns)
NUM_PRODUCTS = 10000  # Number of unique products
return_reasons = ['Damaged', 'Incorrect Item', 'Not Satisfied', 'Defective', 'Late Delivery']
refund_amount_range = (5.0, 500.0)  # Refund range

# Generate unique order_ids and product_ids
order_ids = [f"ORD{str(i).zfill(9)}" for i in range(1, NUM_ORDERS + 1)]  # Order IDs like ORD000000001, ORD000000002...
product_ids = [f"PROD{str(i).zfill(6)}" for i in range(1, NUM_PRODUCTS + 1)]  # Product IDs like PROD000001, PROD000002...

# Generate returns records
returns_records = []

for i in range(NUM_RECORDS):
    return_id = f"RET{str(i+1).zfill(9)}"  # Return ID like RET000000001, RET000000002...
    order_id = random.choice(order_ids)  # Randomly pick an order_id from the available ones
    product_id = random.choice(product_ids)  # Randomly pick a product_id from the available ones
    reason = random.choice(return_reasons)  # Random return reason
    refund_amount = round(random.uniform(*refund_amount_range), 2)  # Random refund amount within the specified range
    return_date = fake.date_between(start_date='-30d', end_date='+30d')  # Random return date within a range of 30 days before or after today

    returns_records.append({
        "return_id": return_id,
        "order_id": order_id,
        "product_id": product_id,
        "reason": reason,
        "refund_amount": refund_amount,
        "return_date": str(return_date)  # Convert to string for JSON compatibility
    })

# Save to JSON file
with open('returns.json', 'w') as f:
    json.dump(returns_records, f, indent=4)

print("✅ Generated 'returns_1M.json' with 1 million returns records.")
