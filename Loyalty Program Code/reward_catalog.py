import pandas as pd
import random
from faker import Faker

# Setup
fake = Faker()
random.seed(42)

# Constants
NUM_ITEMS = 500  # reasonable catalog size
MIN_COST = 50
MAX_COST = 5000
AVAILABILITY_STATUSES = ["In Stock", "Out of Stock", "Limited", "Discontinued"]

catalog = []

for i in range(1, NUM_ITEMS + 1):
    item = {
        "item_id": f"ITEM{str(i).zfill(5)}",
        "name": fake.catch_phrase(),
        "cost": random.randint(MIN_COST, MAX_COST),  # in points
        "availability": random.choice(AVAILABILITY_STATUSES)
    }
    catalog.append(item)

# Save to CSV
df = pd.DataFrame(catalog)
df.to_csv("reward_catalog.csv", index=False)

print("✅ Generated 'reward_catalog.csv' with 500 reward items.")
