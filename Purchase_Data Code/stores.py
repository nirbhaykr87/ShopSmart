import json
import random
from faker import Faker

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
NUM_RECORDS = 1_000_000  # Total number of records
NUM_STORES = 100  # Unique stores
store_types = ['website', 'In-Store']

# Generate unique stores
stores = []
for i in range(1, NUM_STORES + 1):
    store_id = f"STORE{str(i).zfill(3)}"  # 100 unique stores with store_id like STORE001, STORE002...
    location = fake.city()  # Random city name for location
    stores.append({
        "store_id": store_id,
        "location": location
    })

# Generate records (1 million records) for stores
records = []

for _ in range(NUM_RECORDS):
    store = random.choice(stores)  # Randomly pick a store from the 100 stores
    store_id = store['store_id']
    location = store['location']
    
    # Determine store type and rep_id
    store_type = random.choice(store_types)
    if store_type == 'website':
        rep_id = "NA"  # Website stores don't have a rep_id
    else:
        rep_id = f"REP{str(random.randint(1, NUM_STORES)).zfill(5)}"  # Generate random rep_id for In-Store stores
    
    records.append({
        "store_id": store_id if store_type != 'website' else "NA",
        "location": location,
        "type": store_type,
        "rep_id": rep_id
    })

# Save to JSON file
with open('stores.json', 'w') as f:
    json.dump(records, f, indent=4)

print("✅ Generated 'stores_1M.json' with 1 million records.")
