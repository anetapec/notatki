from shop.aplle import Aplle
from shop.order import print_order, generate_order
from shop.patato import Patato

def run_homework():
    green_aplle = Aplle(species_name="Green", size="M", price=3.5)
    red_aplle = Aplle(species_name="Red", size="S", price=2.8)
    print(green_aplle.species_name, green_aplle)
    print(red_aplle.species_name, red_aplle)

    old_patato = Patato(species_name="Patato Old", size="S", price=1.55)
    print(old_patato.species_name, old_patato)

    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

if __name__ == '__main__':
    run_homework()