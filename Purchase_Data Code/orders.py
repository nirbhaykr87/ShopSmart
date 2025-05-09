import json
import random
from faker import Faker

# Initialize Faker and set seed for reproducibility
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_ORDERS = 1_000_000
CHANNELS = ['Website', 'Mobile App', 'In-Store']
CUSTOMER_IDS = [f'CUST{str(i).zfill(7)}' for i in range(1, 100001)]  # 100k customers

orders = []

# Generate data
for i in range(1, NUM_ORDERS + 1):
    order_id = f'ORD{str(i).zfill(9)}'
    customer_id = random.choice(CUSTOMER_IDS)
    order_date = fake.date_between(start_date='-2y', end_date='today')
    channel = random.choice(CHANNELS)
    total_amount = round(random.uniform(20.0, 2000.0), 2)

    orders.append({
        'order_id': order_id,
        'customer_id': customer_id,
        'order_date': str(order_date),  # Convert date to string
        'channel': channel,
        'total_amount': total_amount
    })

# Save to JSON
with open('orders', 'w') as json_file:
    json.dump(orders, json_file, indent=4)

print("✅ Generated 'orders_1M.json' with 1 million records.")
