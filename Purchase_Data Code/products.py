import json
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Constants
NUM_PRODUCTS = 1_000_000
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports', 'Beauty & Health', 'Toys', 'Automotive']
BRANDS = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']
MIN_PRICE = 5.0
MAX_PRICE = 1000.0
MIN_STOCK = 1
MAX_STOCK = 500

products = []

# Generate products
for i in range(1, NUM_PRODUCTS + 1):
    product_id = f'PROD{str(i).zfill(6)}'
    name = fake.word().capitalize() + " " + fake.word().capitalize()
    category = random.choice(CATEGORIES)
    brand = random.choice(BRANDS)
    price = round(random.uniform(MIN_PRICE, MAX_PRICE), 2)
    stock = random.randint(MIN_STOCK, MAX_STOCK)

    products.append({
        'product_id': product_id,
        'name': name,
        'category': category,
        'brand': brand,
        'price': price,
        'stock': stock
    })

# Save to JSON
with open('products', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("✅ Generated 'products_1M.json' with 1 million product records.")
