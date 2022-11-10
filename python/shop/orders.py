from assortyment import products
orders = [
    {
        "product": "chleb",
        "quanity": 10,
        "total price": 35
    }
]
def create_new_order(product_name,quanity):
    price = product[product_name]["price"]
    available_quanity = products[product_name]["quanity"]

    if available_quanity < quanity:
        print("Nie mamy tyle towaru!")
        return None

        total_price = price * quanity
        new_order = {
            "product": product_name,
            "quanity": quanity,
            "total_price": total_price
        }

        update_product_quanity(product_name, quanity)
        orders.append(new_order)
        return new_order

