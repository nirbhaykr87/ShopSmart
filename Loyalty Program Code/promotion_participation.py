import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)

# Constants
NUM_RECORDS = 1_000_000
NUM_MEMBERS = 500_000
PROMOTION_IDS = [f"PROMO{str(i).zfill(4)}" for i in range(1, 201)]  # 200 promotions
OUTCOMES = ['joined', 'completed', 'abandoned', 'rewarded']

# Generate data
records = []
for i in range(NUM_RECORDS):
    record = {
        "participation_id": f"PART{str(i+1).zfill(8)}",
        "member_id": f"MEM{str(random.randint(1, NUM_MEMBERS)).zfill(6)}",
        "promotion_id": random.choice(PROMOTION_IDS),
        "joined_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
        "outcome": random.choices(OUTCOMES, weights=[0.4, 0.3, 0.2, 0.1])[0]
    }
    records.append(record)

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("promotion_participation.csv", index=False)

print("✅ Generated 'promotion_participation.csv' with 1 million records.")
