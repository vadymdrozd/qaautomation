from product import Product
from psycopg2 import connect

from queries import (select_all_query,
                     add_new_products_query,
                     price_modification_query,
                     delete_query)

connection = connect(
    database='store',
    user='vadimdrozd',
    password='postgres'
    )

cursor = connection.cursor()
cursor.execute(select_all_query)
result_before_update = cursor.fetchall()
products = Product.from_cursor_data(result_before_update)

for product in products:
    print(product)

# Adding new products
cursor.execute(add_new_products_query)
cursor.execute(select_all_query)
result_after_new_products_add = cursor.fetchall()
products = Product.from_cursor_data(result_after_new_products_add)

print("-" * 50)

for product in products:
    print(product)

# Updating products where quantity less than 10
cursor.execute(price_modification_query)
cursor.execute(select_all_query)
result_after_price_updating = cursor.fetchall()
products = Product.from_cursor_data(result_after_price_updating)

print("-" * 50)

for product in products:
    print(product)

# Deleting products where quantity more than 10
cursor.execute(delete_query)
cursor.execute(select_all_query)
result_after_deleting = cursor.fetchall()
products = Product.from_cursor_data(result_after_deleting)

print("-" * 50)

for product in products:
    print(product)

# connection.commit()