#poproś użytkownika o oceny końcowe
#można zdać gdy nie ma żadnej 1
#lub gdy ma jedną 1 ale średnia jest > od 3,5

final_grades_maths = float(input("Podaj ocenę końcową z matematyki"))
final_grades_polish = float(input("Podaj ocenę końcową z polskiego"))
final_grades_physics = float(input("Podaj ocenę końcową z fizyki"))
final_grades_biology = float(input("Podaj ocenę końcową z biologi"))

number_of_failures = 0

if final_grades_maths < 2:
    number_of_failures = number_of_failures + 1
if final_grades_polish < 2:
    number_of_failures = number_of_failures + 1
if final_grades_physics < 2:
    number_of_failures = number_of_failures + 1
if final_grades_biology < 2:
    number_of_failures = number_of_failures + 1

if number_of_failures == 0:
    print("Gratulacje , zdałeś do następnej klasy !")
else:

    if number_of_failures == 1:
        average = (final_grades_maths + final_grades_polish + final_grades_physics + final_grades_biology) / 4
        if average > 3.5:
            print("Gratulacje, zdałeś do następnej klasy!")
        else:
            print("Niestety....")
    else: print("Niestety...")