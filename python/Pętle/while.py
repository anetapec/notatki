# dopóki licznik nie przekroczy 30 wypisujey kolejne liczby

counter = 0             # najpierw trzeba inicjalizować !!!
while counter <= 30:
    print(counter)
    counter += 1
#spytaj ile chcesz ziemniaków na obiad i obierz tyle:

expected_patotes = int(input("Ile ziemniaków cgcesz na obiad?"))
patotes = []                     # najpierw trzeba inicjalizować !!!
while len(patotes) < expected_patotes:
    print("Obieram ziemniaka..")
    print(("I wrzucam go do garnka"))
    patotes.append("Ziemniak")
print(patotes)

#poproś użytkownika o podanie liczby większej od 100

number = 0          # najpierw trzeba inicjalizować !!!
while number <= 100:
    number = int(input("Podaj liczbę większą od 100 !"))
    if number <= 100:
        print(f"Liczba {number} jest mniejsza od 100. Próbuj dalej...\n")
print("Brawo")

#drugi sposób na podanie liczby większej niż 100
number = int(input("Podaj liczbę większą od 100 !"))
while number <= 100:
    print(f"Liczba {number} jest mniejsza od 100. Próbuj dalej...\n")
    number = int(input("Podaj liczbę większą od 100 !"))      #trzeba ponownie dać bo inaczej program się nie zatrzyma
print("Brawo")

