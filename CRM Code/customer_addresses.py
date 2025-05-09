import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
Faker.seed(456)
random.seed(456)

# Configuration
num_customers = 1_000_000
regions = ['North', 'South', 'East', 'West', 'Central']
address_types = ['Billing', 'Shipping']

# Generate data
address_data = []

for i in range(1, num_customers + 1):
    address_data.append({
        "address_id": f"ADDR{str(i).zfill(8)}",
        "customer_id": f"CUST{str(i).zfill(7)}",
        "address_type": random.choice(address_types),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "postal_code": fake.postcode(),
        "region": random.choice(regions),
        "country": fake.country()
    })

# Create DataFrame
addresses_df = pd.DataFrame(address_data)

# Save to CSV
addresses_df.to_csv("customer_addresses.csv", index=False)
print("✅ Generated 'customer_addresses.csv' with 1 address per customer (billing or shipping).")
