
#sprawdź jakie dotacje otrzymasz ?
#można wielokrotnie sprawdzać podmieniając dane


option = "T"
while option == "T":          #podajemy by użytkownik mógł sprawdzicz dla innych parametrów

    income = int(input("Jaki masz dochód ?"))
    emploes = int(input("Ile osób zatrudniasz ?"))
    years_on_the_market = int(input("Ile lat masz firmę"))

    if income < 2000:
        print(" Przyznano wsparcie główne:")
    elif 5 <= emploes <= 10:
        print("Przyznano wsparcie z funduszy pracowników.!")
    elif years_on_the_market < 3:
        print("Przyznano wsparcie dla nowych firm. :)")
    else:
        print("Przyznano wsparcie na pocieszenie :)")

    option = input("Jeżeli chcesz sptawdzić dla innych danych wpisz 'T':")

