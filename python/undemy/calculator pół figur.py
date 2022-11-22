# Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:
# 1) prostokąta
# 2) kwadratu
# 3) trójkąta
# 4) trapezu
# 5) koła

print("Program obliczający pola figur")
while True:
    menu = input(
        f"Pole jakiej figury chcesz obiczyć?\n1 prostokąta\n2 kwadratu\n3 trójkąta\n4 trapezu\n5 koła\n6 Koniec")

    if menu == "1":  # pamiętać by było w ""
        def rectangle_area(a, b):
            return a * b


        a = float(input("Podaj długość boku a"))
        b = float(input("Podaj długość boku b"))

        print(f"Pole prostokąta o bokach a = {a} i b = {b} wynosi {rectangle_area(a, b)}")

    elif menu == "2":
        def square_area(a):
            return a * a


        a = float(input("Podaj długość boku a"))
        print(f"Pole kwadratu o boku a = {a} wynosi {square_area(a)}")

    # elif menu == "3":
    # def triangle_area(a,b,c):
    elif menu == "6":
        print("Kończymy na dziś .")
        break
    else:
        print(("Podałeś zły wariant"))


