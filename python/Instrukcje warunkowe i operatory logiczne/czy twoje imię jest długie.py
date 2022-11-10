#określenie czy Twoje imię est krótkie czy dlugie czy zwykłej długości

#TRUDNIEJSZY SPOSÓB NIŻ if and

name = input("Jak masz na imię?")
print(f"Miło Cię poznać {name.title()}.")
name_lenght = len(name)
if name_lenght < 5:
    print(f"{name.title()} to raczej krótkie imię.")
if name_lenght >= 5:
    if name_lenght <= 8:
        print(f"{name.title()} to imię zwyłej długości.")
    else:
        print(f"{name.title()} to długie imię.")

# można łatwiej !!!!!!!
name = input("Jak masz na imię?")
print(f"Miło Cię poznać {name.title()}.")
name_lenght = len(name)
if name_lenght < 5:
    print(f"{name.title()} to raczej krótkie imię.")
if 5 <= name_lenght <= 8:
    print(f"{name.title()} to imię zwyłej długości.")
else:
    print(f"{name.title()} to długie imię.")


### trzeci sposób :
name = input("Jak masz na imię?")
print(f"Miło Cię poznać {name.title()}.")
name_lenght = len(name)

if name_lenght < 5:
    print(f"{name.title()} to raczej krótkie imię.")
if name_lenght >= 5 and name_lenght <= 8:
    print(f"{name.title()} to imię zwyłej długości.")
else:
    print(f"{name.title()} to długie imię.")





