#czy zdasz do następnej klasy:
#Wczytaj oceny do listy.
#Jeżeli jest jakakolwiek jedynka to klasę trzeba powtórzyć.
#W przeciwnym razie należą się gratulacje.

subjects = ["matematyka", "fizyka", "polski", "historia", "angielski"]
grades = []
for subject in subjects:
    grade = int(input(f"Jaka jest Twoja końcowa ocena z {subject}?"))
    grades.append(grade)

for grade in grades:
    if grade == 1:
        print("Niestety...")
        break         #pamiętać
else:
        print("Gratulacje, zdałeś !!!")

#drugi sposób

subjects = ["matematyka", "fizyka", "polski", "historia", "angielski"]
grades = []
for subject in subjects:
    grade = int(input(f"Jaka jest Twoja końcowa ocena z {subject}?"))

    if grade == 1:
        print("Niestety...")
        break         #pamiętać
else:
        print("Gratulacje, zdałeś !!!")

