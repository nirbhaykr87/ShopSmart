import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)

# Constants
NUM_RECORDS = 1_000_000
NUM_MEMBERS = 500_000
FEEDBACK_TYPES = ['Suggestion', 'Complaint', 'Praise', 'Question']
FEEDBACK_STATUS = ['New', 'Reviewed', 'Resolved']

# Generate data
feedback_data = []

for i in range(1, NUM_RECORDS + 1):
    feedback_data.append({
        "feedback_id": f"FDBK{str(i).zfill(8)}",
        "member_id": f"MEM{str(random.randint(1, NUM_MEMBERS)).zfill(6)}",
        "date": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
        "type": random.choice(FEEDBACK_TYPES),
        "message": fake.sentence(nb_words=12),
        "status": random.choice(FEEDBACK_STATUS)
    })

# Save to CSV
df = pd.DataFrame(feedback_data)
df.to_csv("member_feedback.csv", index=False)

print("✅ Generated 'member_feedback.csv' with 1 million records.")
