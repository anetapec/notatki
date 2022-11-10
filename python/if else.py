apple_price = float(input("Po ile są jabłka ?"))
pear_price = float(input("Po ile są gruszki ?"))
banana_price = float(input("Po ile są banany ?"))
if apple_price > pear_price:
    print("Jabłka są droższe niż gruszki")
else:
    print(("Jabłka są tańsze niż gruszki"))

if pear_price > banana_price:
    print("Gruszki są droższe od bananów.")
else:
    print("Gruszki są tańsze od bananów")

if apple_price > banana_price:
    print("Jabłka są droższe od bananów.")
else:
    print("Jabłka są tańsze od bananów.")
