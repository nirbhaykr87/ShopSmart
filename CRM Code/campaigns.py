import pandas as pd
from faker import Faker
import random
from datetime import timedelta

# Setup
fake = Faker()
Faker.seed(3456)
random.seed(3456)

# Config
num_campaigns = 5000
channels = ['Email', 'SMS', 'In-Store', 'Social Media', 'Mobile App', 'Website']
target_groups = ['All Customers', 'Leads Only', 'North Region', 'VIP Customers', 'Online Only']
statuses = ['Planned', 'Ongoing', 'Completed', 'Cancelled']
objectives = ['Awareness', 'Promotion', 'Retargeting', 'New Launch', 'Feedback']

# Generate campaigns
campaigns = []

for i in range(1, num_campaigns + 1):
    start_date = fake.date_between(start_date='-2y', end_date='today')
    end_date = start_date + timedelta(days=random.randint(7, 30))

    campaigns.append({
        "campaign_id": f"CAMP{str(i).zfill(5)}",
        "name": f"{fake.bs().title()} Campaign",
        "channel": random.choice(channels),
        "start_date": start_date,
        "end_date": end_date,
        "target_audience": random.choice(target_groups),
        "budget_usd": round(random.uniform(1000, 50000), 2),
        "status": random.choice(statuses),
        "objective": random.choice(objectives)
    })

# Create DataFrame and save
campaigns_df = pd.DataFrame(campaigns)
campaigns_df.to_csv("campaigns.csv", index=False)

print("✅ Generated 'campaigns.csv' with 5,000 marketing campaign records.")
