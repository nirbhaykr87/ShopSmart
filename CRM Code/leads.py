import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
Faker.seed(2345)
random.seed(2345)

# Config
num_leads = 1_000_000
conversion_rate = 0.05  # 5% leads are converted
sources = ['Google Ad', 'Facebook Ad', 'Email Campaign', 'Referral', 'Organic Search']
statuses = ['New', 'Contacted', 'Unreachable', 'Dropped', 'Converted']
interest_areas = ['Electronics', 'Clothing', 'Fitness', 'Books', 'Beauty', 'Groceries']

leads = []

for i in range(1, num_leads + 1):
    lead_id = f"LEAD{str(i).zfill(6)}"
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    source = random.choice(sources)
    status = random.choice(statuses[:-1])  # Exclude 'Converted' by default
    converted_customer_id = ""

    # Assign ~5% of leads as converted
    if random.random() < conversion_rate:
        status = 'Converted'
        converted_customer_id = f"CUST{str(random.randint(1, 1_000_000)).zfill(7)}"

    leads.append({
        "lead_id": lead_id,
        "name": name,
        "email": email,
        "phone": phone,
        "source": source,
        "status": status,
        "converted_customer_id": converted_customer_id,
        "created_at": fake.date_between(start_date='-1y', end_date='today')
    })

# Create DataFrame and Save
leads_df = pd.DataFrame(leads)
leads_df.to_csv("leads.csv", index=False)

print("✅ Generated 'leads.csv' with 1 million records, including ~5% converted leads.")
