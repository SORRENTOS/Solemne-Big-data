# -*- coding: utf-8 -*-
import csv
import random
from datetime import datetime, timedelta

# 1. Generar Catálogo de Tiendas
stores = [
    (1, "Sucursal Centro", "Santiago"),
    (2, "Sucursal Norte", "Antofagasta"),
    (3, "Sucursal Sur", "Concepción"),
    (4, "Sucursal Costanera", "Viña del Mar"),
]

with open("stores.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(["store_id", "store_name", "city"])
  writer.writerows(stores)

# 2. Generar Catálogo de Productos (200 productos)
categories = ["Electrónica", "Alimentos", "Hogar", "Ropa", "Deportes"]
products = []
for i in range(1, 201):
  products.append((
      i,
      f"Producto_{i}",
      random.choice(categories),
      round(random.uniform(1000, 150000), 2),
  ))

with open("products.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(["product_id", "product_name", "category", "unit_price"])
  writer.writerows(products)

# 3. Generar Transacciones (55,000 registros)
start_date = datetime(2025, 1, 1)
with open("transactions.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(
      ["transaction_id", "store_id", "product_id", "quantity", "date", "total"]
  )
  for t_id in range(1, 55001):
    store_id = random.choice(stores)[0]
    prod = random.choice(products)
    prod_id = prod[0]
    price = prod[3]
    qty = random.randint(1, 5)
    days_offset = random.randint(0, 365)
    t_date = start_date + timedelta(days=days_offset)
    total = round(price * qty, 2)
    writer.writerow(
        [t_id, store_id, prod_id, qty, t_date.strftime("%Y-%m-%d"), total]
    )

print(
    "¡Archivos generados con éxito! transactions.csv contiene 55.000 registros."
)
