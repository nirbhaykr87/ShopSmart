import json
import random
from faker import Faker

# Initialize Faker
fake = Faker()
random.seed(42)

# Constants
NUM_CUSTOMERS = 1_000_000
REGIONS = ['North', 'South', 'East', 'West', 'Central']
LOYALTY_STATUSES = ['None', 'Bronze', 'Silver', 'Gold', 'Platinum']

customers = []

# Generate customer records
for i in range(1, NUM_CUSTOMERS + 1):
    customer = {
        "customer_id": f"CUST{str(i).zfill(7)}",
        "name": fake.name(),
        "email": fake.email(),
        "region": random.choice(REGIONS),
        "loyalty_status": random.choices(
            LOYALTY_STATUSES, weights=[0.3, 0.3, 0.2, 0.15, 0.05], k=1
        )[0]
    }
    customers.append(customer)

# Save to JSON
with open("customers.json", "w") as f:
    json.dump(customers, f, indent=2)

print("✅ Generated 'customers_1M.json' with 1 million customer records.")
