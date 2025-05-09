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
NUM_MEMBERS = 1_000_000  # Assuming 1M members exist
TODAY = datetime.today()

loyalty_points = []

for _ in range(NUM_RECORDS):
    member_id = f'MEM{str(random.randint(1, NUM_MEMBERS)).zfill(7)}'
    earned = random.randint(10, 1000)
    redeemed = random.randint(0, earned)  # Can't redeem more than earned
    expiry = TODAY + timedelta(days=random.randint(30, 730))  # 1 month to 2 years from now

    loyalty_points.append({
        'member_id': member_id,
        'earned': earned,
        'redeemed': redeemed,
        'expiry': expiry.strftime('%Y-%m-%d')
    })

# Convert to DataFrame and save
df = pd.DataFrame(loyalty_points)
df.to_csv('loyalty_points.csv', index=False)

print("✅ Generated 'loyalty_points_1M.csv' with 1 million records.")
