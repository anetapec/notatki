# napisz program który zapyta jaka jest cena jabłek w biedronce ,lidlu , zabce a następnie podaj najniższą cene
biedronka_price  = float(input("Ile kosztują jabłka w Biedronce ?"))
lidl_price = float(input("Ile kosztują jabłka w Lidlu ?"))
zabka_price = float(input("Ile kosztują jabłka w Żabce "))

cheapest_price = min(biedronka_price, lidl_price, zabka_price)
print("Najtańsze jabłka są po: ", cheapest_price, "zł.")