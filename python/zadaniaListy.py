#zad 1
favorite_sports = ["bieganie", "pływanie", "jazda na rowerze" ,"jazda konno"]
print("Pierwszym spotrem jest :", favorite_sports[0], "a ostatnim ", favorite_sports[-1])
favorite_sports[2] = "skakanie"
print(favorite_sports)
#zad 2 zapytaj o 3 ulubione potrway
favorite_dishes = input("Jakie są Twoje 3 ulubione potrawy ?")

#zapisz ulubione potrawy w postaci listy
print(favorite_dishes.split())

#zad3 zapytaj o numer tel
your_phonenumber = input("Podaj swój numer telefonu")
anonim_number = your_phonenumber[2:] + "***"
print(f"Twój numer telefonu to:", anonim_number)

