#Wczytaj od użytkownika listę ulubionych sportów,
# a następnie stosując slicing wypisz co drugi, pomijając pierwszy sport z listy.

def run_homework():
    print("Jakie są Twoje ulubione sporty")

    favorite_sports = []
    while True:
        sport = input("Podaj swoje ulubone sporty lub zakończ wpisując 'X'")
        if sport == "X":
            break
        favorite_sports.append(sport)
#wypisujemy zez pierwszego ale co drugi :
    print(favorite_sports[1::2])


if __name__ == '__main__':
    run_homework()

