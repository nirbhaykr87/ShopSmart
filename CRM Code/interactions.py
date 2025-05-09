import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
Faker.seed(1234)
random.seed(1234)

# Config
total_interactions = 1_000_000
interaction_types = ['Support Chat', 'Email', 'Phone Call', 'In-Store Visit', 'App Notification']
channels = ['Website', 'Mobile App', 'Call Center', 'In-Store']

# Generate interactions
interactions = []

for i in range(1, total_interactions + 1):
    customer_id = f"CUST{str(random.randint(1, 1_000_000)).zfill(7)}"
    interactions.append({
        "interaction_id": f"INT{str(i).zfill(9)}",
        "customer_id": customer_id,
        "interaction_type": random.choice(interaction_types),
        "interaction_date": fake.date_time_between(start_date='-2y', end_date='now'),
        "channel": random.choice(channels),
        "notes": fake.sentence(nb_words=6)
    })

# Create DataFrame
interactions_df = pd.DataFrame(interactions)

# Save to CSV
interactions_df.to_csv("interactions.csv", index=False)
print("✅ Generated 'interactions.csv' with exactly 1,000,000 interaction records.")
