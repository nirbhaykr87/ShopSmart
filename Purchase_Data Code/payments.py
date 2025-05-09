import json
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()
random.seed(42)

# Constants
NUM_PAYMENTS = 1_000_000
PAYMENT_METHODS = ['Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'Wallet']
STATUSES = ['Success', 'Failed', 'Pending']

payments = []

# Generate payment data
for i in range(1, NUM_PAYMENTS + 1):
    order_id = f"ORD{str(i).zfill(9)}"
    payment_method = random.choice(PAYMENT_METHODS)
    transaction_id = f"TXN{str(i).zfill(10)}"
    status = random.choices(STATUSES, weights=[0.9, 0.05, 0.05], k=1)[0]
    timestamp = fake.date_time_between(start_date='-2y', end_date='now').isoformat()

    payments.append({
        "order_id": order_id,
        "payment_method": payment_method,
        "transaction_id": transaction_id,
        "status": status,
        "timestamp": timestamp
    })

# Save to JSON
with open("payments.json", "w") as f:
    json.dump(payments, f, indent=2)

print("✅ Generated 'payments_1M.json' with 1 million payment records.")
