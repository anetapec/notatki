#czy dostaniesz dotacje
# firma nie może przekraczać dochodu LUB zatrudniać max pracowników
# dochód < 1550 zł
# liczba pracowników > 3

income = float(input("Jaki masz dochód ?"))
emploee = int(input("Ile osób zatrudniasz ?"))

if income < 15500 or emploee > 3:
    print("Możesz dostać dotacje")
else:
    print(("Nie dostaniesz dotacji"))

# operatory or i and można łączyć

income = float(input("Jaki masz dochód ?"))
emploee = int(input("Ile osób zatrudniasz ?"))
if income < 15500 or (emploee >= 3 and income < 30000):
    print("Możesz dostać dotacje")
else:
    print(("Nie dostaniesz dotacji"))

# operator not
income = float(input("Jaki masz dochód ?"))
emploee = int(input("Ile osób zatrudniasz ?"))
support_answer = input("Czy otrzymałeś już dotacje kiedykowiek? T/N")

if support_answer == "T":
    support_used = True
else:
    support_used = False

if not support_used and (income < 155000 or emploee >= 3):
    print("Możesz otrzymać dotacje ")
else:
    print("Nie możesz otrzymać dotacji")




