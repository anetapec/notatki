class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """"Wyświetla info o restauracji"""
        print(f"Restauracja {self.restaurant_name.title()} serwuje kuchnię {self.cuisine_type}")

    #def open_restaurant(self):
        #print(f"Restauracja jest czynna w godzinach {self.opening_hours}")


restaurant = Restaurant('2 okna', 'włoską')
#openieng_hours = Restaurant('12.00 do 23.00')

restaurant.describe_restaurant()
#openieng_hours.open_restaurant()