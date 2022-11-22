from shop.order import generate_order
from shop.apple import calculate_price

def run_homework():
    green_aplle = Aplle(species_name="Green", size="M", price=3.5)
    red_aplle = Aplle(species_name="Red", size="S", price=2.8)
    print(f"10 kg zielonego jabłka kosztuje {green_aplle.calculate_price(10)}")
    print(f"5 kg czerwonego jabłka kosztuje {red_aplle.calculate_price(5)}")
    old_patato = Patato(species_name="Patato Old", size="S", price=1.55)
    print(f"8 kg starych ziemniaków kosztuje {old_patato.calculate_price(8)}")



if __name__ == "__main__":
    run_homework()
