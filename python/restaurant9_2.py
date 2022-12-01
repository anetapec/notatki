class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """"Wyświetla info o restauracji"""
        print(f"Restauracja {self.restaurant_name.title()} serwuje kuchnię {self.cuisine_type}")

    def set_number_served(self):
        """"Wyświetla info o liczbie obsłużonych klientów"""
        print(f"Ilość obsłużonych klientów wynosi {self.number_served}")

    #def increment_number_set(self, clients):
        #self.number_served += clients



restaurant = Restaurant('2 okna', 'włoską')
restaurant.describe_restaurant()

restaurant_1 = Restaurant('Willa pod Bramą', 'polską')
restaurant_2 = Restaurant('Italiano', 'włoską')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

restaurant.number_served = 6
restaurant.set_number_served() #wyświetli info o liczbie obsłuzonych klientów
#restaurant.increment_number_set(100)
#restaurant.number_served(15)
#restaurant.increment_number_set()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['czekoladowy', 'waniliowy', 'śmietankowy']

    def flavors_ice(self):
        print(f"Mamy dostępne smaki {self.flavors}")

ice = IceCreamStand('Zielona Budka', 'polskie')
print(ice.flavors_ice())

