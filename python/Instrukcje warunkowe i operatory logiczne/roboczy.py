

#Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
#Product: nazwa, nazwa kategorii, cena jednostkowa
#Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
#Apple: nazwa gatunku, rozmiar, cena za kg
#Potato: nazwa gatunku, rozmiar, cena za kg
#Utwórz kilka obiektów każdej klasy.
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

class Order:
    def __int__(self, client_first_name, client_last_name, products = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price

class Aplle:
    def __int__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

class Patato:
    def __int__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

def run_home_work():
    green_aplle = Aplle(species_name="Green", size="M", price=3.55)
    red_aplle = Aplle(species_name="Red", size="S", price=2.80)
    print(green_aplle.species_name,green_aplle)
    print(red_aplle.species_name,red_aplle)

    old_patoto = Patato(species_name="Patato Old", size="S", price=1.50)
    print(old_patoto.species_name,old_patoto)

    coocies = Product(name="coocies", category_name="Food", unit_price=4)

    empty_order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski")
    print(coocies)
    print(empty_order)
    print(orders)

if __name__ == '__main__':
    run_home_work()

#Napisz funkcję wypisującą produkt i zamówienie. Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.
def print_product(product):
    print(f"Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.unit_price} / szt.")

def print_order(order):
    print("=" * 20)
    print(f"Zamówienie złożone przez {order.client_first_name} {order.client_last_name}")
    print(f"O łącznej wartości : {order.total_price} PLN")
    print("Zamówione produkty :")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("=" * 20)
    print()




