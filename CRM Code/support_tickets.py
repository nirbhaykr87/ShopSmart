import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Setup
fake = Faker()
random.seed(42)
Faker.seed(42)

# Constants
num_tickets = 1000000 # Number of support tickets
num_customers = 1000000  # Number of customers
statuses = ['Open', 'In Progress', 'Closed']
issue_types = ['Complaint', 'Inquiry', 'Technical Issue', 'Billing Issue']
staff_members = [fake.name() for _ in range(10000)]  # 10 staff members

# Generate customer data
customers = []
for i in range(1, num_customers + 1):
    customers.append({
        "customer_id": f"CUST{str(i).zfill(7)}",
        "name": fake.name(),
        "email": fake.email(),
        "location": fake.city(),
        "customer_type": random.choice(['Online', 'Store'])
    })

# Generate support ticket data
ticket_data = []
for i in range(1, num_tickets + 1):
    customer = random.choice(customers)  # Pick a random customer for each ticket
    status = random.choice(statuses)
    if status == 'Closed':
        resolution = fake.sentence(nb_words=6)
        date_resolved = fake.date_this_year()
    else:
        resolution = ""
        date_resolved = ""
    
    ticket_data.append({
        "ticket_id": f"TICKET{str(i).zfill(5)}",
        "customer_id": customer['customer_id'],  # Use customer_id instead of name
        "issue_type": random.choice(issue_types),
        "description": fake.text(max_nb_chars=200),
        "status": status,
        "assigned_staff": random.choice(staff_members),
        "date_submitted": fake.date_this_year(),
        "resolution": resolution,
        "date_resolved": date_resolved
    })

# Save to CSV
df_tickets = pd.DataFrame(ticket_data)
df_customers = pd.DataFrame(customers)

# Save both dataframes to CSV
df_customers.to_csv("customers.csv", index=False)
df_tickets.to_csv("support_tickets.csv", index=False)

print("✅ Generated 'customers.csv' and 'support_tickets.csv' with customer_id linked to tickets.")
