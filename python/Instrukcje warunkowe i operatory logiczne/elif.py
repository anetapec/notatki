### Mamy 4 rodzaje wsparcia od najgorszych są to :
#Główne wsparcie: przychód poniżej 5000
#Wsparcie z funduszu pracowników : od 5 do 10 pracowników
#Wsparcie dla nowych firm : krócej niż 3 lata na rynku
#Wsparcie na pocieszenie : dla każdego kto nie dostał żadnego wsparcia

income = 5000
emploes = 7
years_on_the_market = 7

if income < 5000:
    print("Przyznano wsparcie główne.")
else:                                                           #sprawdzamy po koleji kolejne warunki
    if 5 <= emploes <= 10:
        print("Przyznano wsparcie z funduszu pracowników.")
    else:
        if years_on_the_market < 3:
            print("Przyznano wsparcie dla nowych firm.")
        else:
            print("Przyznano wsparcie na pocieszenie.")

#można zapisać to w łatwiejszy CZYTELNIEJSZY SPOSÓB :

income = 5000
emploes = 7
years_on_the_market = 7

if income < 5000:

    print("Przyznano główne wsparcie.")
if income >= 5000 and 5 <= emploes <= 10:

    print("przyznano wsparcie z funduszy pracowników.")
if income > 5000 and not 5 <= emploes <= 10 and years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm.")
else:
    print("Przyznano wsparcie na pocieszenie.")

#konstrukcja elif pozwala powiedzieć "inaczej jeśli"

#GDY WIĘCEJ WARIANTÓW

if income  < 5000:
    print(" Przyznano wsparcie główne:")
elif 5 <= emploes <= 10:
    print("Przyznano wsparcie z funduszy pracowników.!")
elif years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm. :)")
else:
    print("Przyznano wsparcie na pocieszenie :)")
