#Wypisz ulubione potrawy użytkownika wraz z informacją, które miejsce zajmuje na liście

dishes = input("Podaj swoje ulubione potrawy")
favorit_dishes = dishes.split(",")
dishes_indeks = 0
while dishes_indeks < len(favorit_dishes):
    print(f"Ulubione danie nr {dishes_indeks}: -> {favorit_dishes[dishes_indeks]}")
    dishes_indeks += 1

# poproś użytkownika o nr tel i sformatuj go XXX-XXX-XXX

phone_number = input("Podaj swój numer telefonu")
phone_number = phone_number.replace("-", "")
phone_number_formated = ""
letter_indeks = 0
while letter_indeks < len(phone_number):
    if letter_indeks % 3 == 0 and letter_indeks != 0:
        phone_number_formated += "-"
    phone_number_formated += phone_number[letter_indeks]
    letter_indeks += 1

print(f"Twój numer telefonu to: {phone_number_formated}")

# pytaj użytkownika tak długo aż poda liczbę parzystą lub przekroczy limit 10 prób

number = int(input("Podaj liczbę parzystą ! "))
try_number = 1
while try_number < 10 and number % 2 != 0:
    number = int(input("Spróbuj jeszcze raz. "))
    try_number += 1

