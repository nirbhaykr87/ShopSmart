import pandas as pd
import random

# Define channel types and regions
channel_types = ['Online', 'Mobile App', 'In-Store']
regions = ['North', 'South', 'East', 'West', 'Central']
statuses = ['Active', 'Inactive']

# Start with Online and Mobile App channels
channels = [
    {
        "channel_id": "CHN001",
        "channel_type": "Online",
        "store_id": "",
        "region": "Global",
        "status": "Active"
    },
    {
        "channel_id": "CHN002",
        "channel_type": "Mobile App",
        "store_id": "",
        "region": "Global",
        "status": "Active"
    }
]

# Generate 100 In-Store channels
for i in range(1, 101):
    channels.append({
        "channel_id": f"CHN{str(i + 2).zfill(3)}",  # CHN003 to CHN102
        "channel_type": "In-Store",
        "store_id": f"STORE{str(i).zfill(4)}",      # STORE0001 to STORE0100
        "region": random.choice(regions),
        "status": random.choice(statuses)
    })

# Save to CSV
df = pd.DataFrame(channels)
df.to_csv("sales_channels.csv", index=False)

print("✅ Generated 'sales_channels.csv' with 102 records (Online, Mobile App, and 100 In-Store channels).")
