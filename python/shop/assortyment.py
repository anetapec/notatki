products = {
    "chleb": {
        "quanity": 100,
        "price": 3.5
    },
    "jabłka": {
        "quanity": 50,
        "price": 3.2
    }
}

#fumkcja aktualizująca ilość produktów na stanie
def update_product_quanity(product_name,ordered_quanity):
    products[product_name]["quanity"] -= ordered_quanity