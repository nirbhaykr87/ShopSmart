import pandas as pd
from faker import Faker
import random

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
num_feedback = 1000000  # Number of feedback entries
rating_scale = [1, 2, 3, 4, 5]
feedback_types = ['Product Quality', 'Delivery Experience', 'Customer Support', 'Overall Satisfaction']
sentiments = ['Positive', 'Neutral', 'Negative']

# Generate sample customer_ids (assuming customers.csv has 1 million records)
customer_ids = [f"CUST{str(i).zfill(7)}" for i in range(1, 1000001)]

feedback_data = []

for i in range(1, num_feedback + 1):
    customer_id = random.choice(customer_ids)
    rating = random.choice(rating_scale)
    feedback_data.append({
        "feedback_id": f"FDBK{str(i).zfill(6)}",
        "customer_id": customer_id,
        "feedback_type": random.choice(feedback_types),
        "rating": rating,
        "review": fake.sentence(nb_words=12),
        "sentiment": random.choices(sentiments, weights=[0.6, 0.2, 0.2])[0],
        "feedback_date": fake.date_this_year()
    })

# Convert to DataFrame and save
df_feedback = pd.DataFrame(feedback_data)
df_feedback.to_csv("customer_feedback.csv", index=False)

print("✅ Generated 'customer_feedback.csv' with 50,000 feedback records.")
