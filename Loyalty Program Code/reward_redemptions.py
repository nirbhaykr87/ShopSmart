import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)

# Constants
NUM_REDEMPTIONS = 1_000_000  # 1 million redemptions
NUM_MEMBERS = 100_000        # Assume 100k loyalty members
NUM_ITEMS = 500              # Reward catalog items
DELIVERY_METHODS = ['Email', 'Courier', 'Store Pickup']

redemptions = []

for i in range(1, NUM_REDEMPTIONS + 1):
    redemption = {
        "redemption_id": f"REDEEM{str(i).zfill(8)}",
        "member_id": f"MEM{str(random.randint(1, NUM_MEMBERS)).zfill(6)}",
        "item_id": f"ITEM{str(random.randint(1, NUM_ITEMS)).zfill(5)}",
        "redemption_date": fake.date_between(start_date='-2y', end_date='today'),
        "delivery_method": random.choice(DELIVERY_METHODS)
    }
    redemptions.append(redemption)

# Save to CSV
df = pd.DataFrame(redemptions)
df.to_csv("reward_redemptions.csv", index=False)

print("✅ Generated 'reward_redemptions.csv' with 1 million redemptions.")
