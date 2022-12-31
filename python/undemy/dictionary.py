1#napisz program w którym uzytkownik :
#1) doda nowe definicje
#2)szuka istniejących definicji
#3)usuwa wybrane przez niego definicje

dictionary = {}
while (True):
    print("1 : Dodaj definicje")
    print("2 : Szukaj definicji")
    print("3 Usuń wybraną definicje")
    print("4 Zakończ")

    choice = input("Co chcesz zrobić?")

    if (choice == "1"):
        key = input("Podaj słowo ,które chcesz zdefiniować ")
        definition = input("Podaj jego znaczenie")
        dictionary[key] = definition
        print("Definicja dodana domyślnie")

    elif (choice == "2"):
        key = input("Jaką definicje chcesz znaleźć? ")
        if key in dictionary:
            print(dictionary[key])
        else:
            print("Nie znaleziono podanej definicji")

    elif (choice == "3"):
        key = input("Jaką definicje chcesz usunąć")
        if key in dictionary:
            print("Wybrana definicja została usunięta")
        else:
            print("Nie znaleziono podanej definicji")

    elif (choice == "4"):
        print("Kończymy na dziś . Papa")
        break
    else:
        print("Podałeś zły wariant ")
