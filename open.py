import csv
import os
import locale

def load_data(filename):
    products = [] 

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])

            products.append(
                {
                    "id": id,
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)

    return "\n".join(product_list)

def get_product_by_id(products, product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

os.system('cls')
products = load_data('db_products.csv')

print(get_products(products))


product_id = int(input("Choose your product"))
product = get_product_by_id(products, product_id)
if product:
    print(f"Product found: {product}")
else:
    print("Product not found")
