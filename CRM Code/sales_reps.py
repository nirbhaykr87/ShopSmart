import pandas as pd
import random
from faker import Faker

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
num_store_staff = 100    # Example: 2 per 100 stores
num_marketing_reps = 50
regions = ['North', 'South', 'East', 'West', 'Central']
statuses = ['Active', 'Inactive']

sales_reps = []

# In-store staff (linked to store IDs)
for i in range(1, num_store_staff + 1):
    store_number = random.randint(1, 100)
    sales_reps.append({
        "rep_id": f"REP{str(i).zfill(5)}",
        "name": fake.name(),
        "role": "In-Store Staff",
        "store_id": f"STORE{str(store_number).zfill(4)}",
        "region": random.choice(regions),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "status": random.choice(statuses)
    })

# Regional marketing reps (no store, tied to region)
for j in range(1, num_marketing_reps + 1):
    i = num_store_staff + j
    region = random.choice(regions)
    sales_reps.append({
        "rep_id": f"REP{str(i).zfill(5)}",
        "name": fake.name(),
        "role": "Regional Marketer",
        "store_id": "",
        "region": region,
        "email": fake.email(),
        "phone": fake.phone_number(),
        "status": random.choice(statuses)
    })

# Save to CSV
df = pd.DataFrame(sales_reps)
df.to_csv("sales_reps.csv", index=False)

print("✅ Generated 'sales_reps.csv' with in-store staff and regional marketing reps.")
