import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
Faker.seed(123)
random.seed(123)

# Constants
num_customers = 1_000_000
customer_types = ['Website', 'In-Store']

# ['Website', 'Mobile App', 'Call Center', 'In-Store']

# Generate data
data = [{
    "customer_id": f"CUST{str(i).zfill(7)}",
    "name": fake.name(),
    "email": fake.email(),
    "location": fake.city(),
    "customer_type": random.choice(customer_types)
} for i in range(1, num_customers + 1)]

# Create DataFrame
customers_df = pd.DataFrame(data)

# Save to CSV
customers_df.to_csv("customers.csv", index=False)
print("✅ Generated 'customers.csv' with 1 million customer profiles.")
