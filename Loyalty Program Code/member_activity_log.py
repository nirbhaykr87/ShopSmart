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
ACTIVITIES = ['login', 'purchase', 'reward_view']
START_DATE = datetime.now() - timedelta(days=365)

activity_logs = []

for i in range(NUM_RECORDS):
    member_id = f"MEM{str(random.randint(1, NUM_MEMBERS)).zfill(6)}"
    activity = random.choice(ACTIVITIES)
    timestamp = START_DATE + timedelta(days=random.randint(0, 365),
                                       seconds=random.randint(0, 86400))

    activity_logs.append({
        "log_id": f"LOG{str(i+1).zfill(8)}",
        "member_id": member_id,
        "activity": activity,
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")
    })

# Save to CSV
df = pd.DataFrame(activity_logs)
df.to_csv("member_activity_log.csv", index=False)

print("✅ Generated 'member_activity_log.csv' with 1 million activity records.")
