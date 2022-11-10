#wypisz co 2 sport
favorite_sports = ["bieganie", "pływanie", "jazda na rowerze" ,"jazda konno", "łyzwy", "wymyśl" ]
for index, sport in enumerate(favorite_sports):
    if index % 2 != 0:
        continue
    print(sport)