#zapytaj użytkownika o wiek ...i na podstawie kryteriów
#ocen czy może kandydować

# drugi sposób łatwiejszy

citzen_answer = input("Czy jesteś obuwatelem USA od urodzenia T/N ?")
age = int(input("Ile masz lat ?"))
usa_residance_years = int(input("Od ilu lat mieszkasz w USA ?"))

if citzen_answer == "T":
    citzen = True
else:
    citzen = False

if citzen:
    if age >= 35:
        if usa_residance_years >= 14:
            print("Możesz kandydować ")
        else:
            print("Nie możesz kandydować")
    else:
        print("Nie możesz kandydować")
else:
    print("Nie możesz kandydować")

# łatwiej dużo !!!!!


citzen_answer = input("Czy jesteś obuwatelem USA od urodzenia T/N ?")
age = int(input("Ile masz lat ?"))
usa_residance_years = int(input("Od ilu lat mieszkasz w USA ?"))

if citzen_answer == "T":
    citzen = True
else:
    citzen = False

if citzen and age >= 35 and usa_residance_years >= 14:
    print("Możesz kandydować")
else:
    print("Nie możesz kandydować")




