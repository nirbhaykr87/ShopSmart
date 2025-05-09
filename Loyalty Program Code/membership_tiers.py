import pandas as pd

# Define membership tiers
tiers = [
    {
        "tier": "Silver",
        "benefits": "5% discount on purchases, Early access to sales",
        "criteria": "0 - 999 points"
    },
    {
        "tier": "Gold",
        "benefits": "10% discount, Free shipping, Birthday reward",
        "criteria": "1000 - 4999 points"
    },
    {
        "tier": "Platinum",
        "benefits": "15% discount, Priority customer support, Exclusive deals",
        "criteria": "5000+ points"
    }
]

# Convert to DataFrame and save
df = pd.DataFrame(tiers)
df.to_csv("membership_tiers.csv", index=False)

print("✅ Generated 'membership_tiers.csv' with Silver, Gold, and Platinum tiers.")
