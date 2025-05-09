import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_RECORDS = 1_000_000
MEMBER_IDS = [f"LM{str(i).zfill(6)}" for i in range(1, 100001)]  # 100k loyalty members
TYPES = ['earn', 'redeem']
REASONS = {
    'earn': ['Purchase', 'Referral Bonus', 'Signup Bonus', 'Promotion'],
    'redeem': ['Discount Coupon', 'Gift Redemption', 'Cashback', 'Special Event']
}

records = []

for _ in range(NUM_RECORDS):
    member_id = random.choice(MEMBER_IDS)
    txn_type = random.choice(TYPES)
    reason = random.choice(REASONS[txn_type])
    points = random.randint(10, 500) if txn_type == 'earn' else random.randint(5, 300)
    date = fake.date_between(start_date='-2y', end_date='today')

    records.append({
        "member_id": member_id,
        "transaction_type": txn_type,
        "reason": reason,
        "points": points,
        "date": date
    })

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("point_transactions.csv", index=False)

print("✅ Generated 'point_transactions.csv' with 1 million point event records.")
