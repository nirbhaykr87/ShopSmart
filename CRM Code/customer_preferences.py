import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
Faker.seed(789)
random.seed(789)

# Config
num_customers = 1_000_000
comm_modes = ['Email', 'SMS', 'Mobile App', 'Phone Call']
languages = ['English', 'Hindi', 'Spanish', 'French', 'German']
product_interests = ['Electronics', 'Apparel', 'Home Decor', 'Books', 'Groceries', 'Fitness', 'Beauty']

# Generate preferences
preferences = []

for i in range(1, num_customers + 1):
    preferences.append({
        "preference_id": f"PREF{str(i).zfill(8)}",
        "customer_id": f"CUST{str(i).zfill(7)}",
        "communication_mode": random.choice(comm_modes),
        "language": random.choice(languages),
        "product_interest": random.choice(product_interests)
    })

# Create DataFrame
prefs_df = pd.DataFrame(preferences)

# Save to CSV
prefs_df.to_csv("customer_preferences.csv", index=False)
print("✅ Generated 'customer_preferences.csv' with 1M customer preferences.")
