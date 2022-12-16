class Cake:

    def __init__(self, name, kind, taste, additives, filling, *known_types):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    def show_info(self):
        print("Today in our ofer:")
        print(f"{self.name.upper()}")
        print(f"Kind: {self.kind}")
        print(f"Taste: {self.taste}")
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print(f"\t{a}")
        if len(self.filling) > 0:
            print(f"Filling: {self.filling}")






cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake01.show_info()
print('-' * 30)
cake02.show_info()
print('-' * 30)
cake03.show_info()

print('*' * 30)
bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

