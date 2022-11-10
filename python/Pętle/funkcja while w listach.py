#wypisywanie listy ulubionych spotrów

favorite_sports = ["bieganie", "pływanie", "jazda na rowerze" ,"jazda konno"]
sport_index = 0                         #pamiętać o tym
while sport_index < len(favorite_sports):
    print(favorite_sports[sport_index])
    sport_index += 1                    #pamiętać o tym

#wypisanie codrugiego sportu z listy

favorite_sports = ["bieganie", "pływanie", "jazda na rowerze" ,"jazda konno"]
sport_index = 0                          #pamiętać o tym
while sport_index < len(favorite_sports):
    if sport_index % 2 == 0:
        print(favorite_sports[sport_index])
        sport_index += 1                   #pamiętać o tym