import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_MEMBERS = 1_000_000  # Total number of loyalty members
TIERS = ['Bronze', 'Silver', 'Gold', 'Platinum']  # Loyalty tiers

# Generate loyalty members data
loyalty_members = []

for i in range(1, NUM_MEMBERS + 1):
    member_id = f'MEM{str(i).zfill(7)}'  # Member ID like MEM0000001, MEM0000002...
    name = fake.name()  # Random name
    email = fake.email()  # Random email
    phone = fake.phone_number()  # Random phone number
    join_date = fake.date_between(start_date='-5y', end_date='today')  # Random join date within last 5 years
    tier = random.choice(TIERS)  # Randomly assign a loyalty tier

    loyalty_members.append({
        'ID': member_id,
        'name': name,
        'email': email,
        'phone': phone,
        'join_date': str(join_date),  # Convert to string for CSV compatibility
        'tier': tier
    })

# Convert to DataFrame
df_loyalty_members = pd.DataFrame(loyalty_members)

# Save to CSV
df_loyalty_members.to_csv('loyalty_members.csv', index=False)

print("✅ Generated 'loyalty_members_1M.csv' with 1 million loyalty member records.")
