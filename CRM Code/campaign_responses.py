import pandas as pd
from faker import Faker
import random
from datetime import timedelta

# Setup
fake = Faker()
Faker.seed(4567)
random.seed(4567)

# Config
num_responses = 1_000_000
num_campaigns = 5000
response_types = ['Email Open', 'Link Click', 'SMS Reply', 'In-Store Redemption', 'App Engagement']
channels = ['Email', 'SMS', 'In-Store', 'Mobile App']

responses = []

for i in range(1, num_responses + 1):
    is_lead = random.choice([True, False])
    responses.append({
        "response_id": f"RESP{str(i).zfill(8)}",
        "campaign_id": f"CAMP{str(random.randint(1, num_campaigns)).zfill(5)}",
        "lead_id": f"LEAD{str(random.randint(1, 1_000_000)).zfill(6)}" if is_lead else "",
        "customer_id": f"CUST{str(random.randint(1, 1_000_000)).zfill(7)}" if not is_lead else "",
        "response_type": random.choice(response_types),
        "response_time": fake.date_time_between(start_date='-2y', end_date='now'),
        "channel": random.choice(channels)
    })

# Create DataFrame
df = pd.DataFrame(responses)
df.to_csv("campaign_responses.csv", index=False)

print("✅ Generated 'campaign_responses.csv' with 1 million records linked to campaigns.")
