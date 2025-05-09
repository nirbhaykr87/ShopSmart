import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
num_customers = 1000000  # 1 million customers
num_loyalty_enrollments = 1000000  # 1 million loyalty enrollments
loyalty_tiers = ['Bronze', 'Silver', 'Gold', 'Platinum']
enrollment_channels = ['Online', 'Store', 'Referral']
loyalty_statuses = ['Active', 'Inactive']

# Generate customer data (1 million customers)
customers = []
for i in range(1, num_customers + 1):
    customers.append({
        "customer_id": f"CUST{str(i).zfill(7)}",
        "name": fake.name(),
        "email": fake.email(),
        "location": fake.city(),
        "customer_type": random.choice(['Online', 'Store'])
    })

# Generate loyalty enrollment data (1 million enrollments)
loyalty_data = []
for i in range(1, num_loyalty_enrollments + 1):
    customer = random.choice(customers)  # Pick a random customer for each enrollment
    loyalty_data.append({
        "customer_id": customer['customer_id'],  # Link to customer by customer_id
        "loyalty_status": random.choice(loyalty_statuses),
        "loyalty_tier": random.choice(loyalty_tiers),
        "enrollment_channel": random.choice(enrollment_channels),
        "enrollment_date": fake.date_this_year()
    })

# Save to CSV
df_customers = pd.DataFrame(customers)
df_loyalty = pd.DataFrame(loyalty_data)

# Save both dataframes to CSV
df_customers.to_csv("customers.csv", index=False)
df_loyalty.to_csv("loyalty_enrollments.csv", index=False)

print("✅ Generated 'customers.csv' and 'loyalty_enrollments.csv' with 1 million records each.")
