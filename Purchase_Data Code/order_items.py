import json
import random

# Constants
NUM_ORDER_ITEMS = 1_000_000
NUM_ORDERS = 300_000  # Some orders will have multiple items
PRODUCT_IDS = [f'PROD{str(i).zfill(6)}' for i in range(1, 10001)]  # 10,000 products

order_items = []

for _ in range(NUM_ORDER_ITEMS):
    order_id = f'ORD{str(random.randint(1, NUM_ORDERS)).zfill(9)}'
    product_id = random.choice(PRODUCT_IDS)
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(5.0, 500.0), 2)
    total = round(quantity * unit_price, 2)

    order_items.append({
        'order_id': order_id,
        'product_id': product_id,
        'quantity': quantity,
        'unit_price': unit_price,
        'total': total
    })

# Save to JSON
with open('order_items', 'w') as json_file:
    json.dump(order_items, json_file, indent=4)

print("✅ Generated 'order_items_1M.json' with exactly 1 million records.")
