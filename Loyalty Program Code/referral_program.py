import pandas as pd
import random
from faker import Faker

# Setup
fake = Faker()
random.seed(42)

# Constants
NUM_REFERRALS = 1_000_000
NUM_MEMBERS = 500_000  # Assume 500k total members
STATUS_OPTIONS = ['Completed', 'Pending', 'Rejected']
BONUS_RANGE = (50, 500)  # Bonus in points or currency

referrals = []

for i in range(1, NUM_REFERRALS + 1):
    referrer = random.randint(1, NUM_MEMBERS)
    referred = random.randint(1, NUM_MEMBERS)
    while referred == referrer:
        referred = random.randint(1, NUM_MEMBERS)
    
    status = random.choice(STATUS_OPTIONS)
    bonus = random.randint(*BONUS_RANGE) if status == 'Completed' else 0

    referrals.append({
        "referral_id": f"REF{str(i).zfill(8)}",
        "referrer_id": f"MEM{str(referrer).zfill(6)}",
        "referred_id": f"MEM{str(referred).zfill(6)}",
        "status": status,
        "bonus": bonus
    })

# Save to CSV
df = pd.DataFrame(referrals)
df.to_csv("referral_program.csv", index=False)

print("✅ Generated 'referral_program.csv' with 1 million records.")
