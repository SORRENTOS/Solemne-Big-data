import csv
import random
from datetime import datetime, timedelta

stores = [
    (1, "Sucursal Centro", "Santiago"),
    (2, "Sucursal Norte", "Antofagasta"),
    (3, "Sucursal Sur", "Concepcion"),
    (4, "Sucursal Costanera", "Vina del Mar"),
]

with open("stores.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["store_id", "store_name", "city"])
    writer.writerows(stores)

categories = ["Electronica", "Alimentos", "Hogar", "Ropa", "Deportes"]
products = []
for i in range(1, 201):
    products.append((
        i,
        "Producto_" + str(i),
        random.choice(categories),
        round(random.uniform(1000, 150000), 2)
    ))

with open("products.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["product_id", "product_name", "category", "unit_price"])
    writer.writerows(products)

start_date = datetime(2025, 1, 1)
with open("transactions.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "store_id", "product_id", "quantity", "date", "total"])
    for t_id in range(1, 55001):
        store_id = random.choice(stores)[0]
        prod = random.choice(products)
        prod_id = prod[0]
        price = prod[3]
        qty = random.randint(1, 5)
        days_offset = random.randint(0, 365)
        t_date = start_date + timedelta(days=days_offset)
        total = round(price * qty, 2)
        writer.writerow([t_id, store_id, prod_id, qty, t_date.strftime("%Y-%m-%d"), total])

print("¡Archivos generados con exito!")