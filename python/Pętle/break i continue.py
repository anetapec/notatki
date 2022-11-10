#podaj oceny a wyliczę średnią
#max 5 prób

grades = []
while len(grades) < 5:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X'")
    if grade_input == 'X':
        break
    grade = int(grade_input)
    grades.append(grade)
else:
    print("Wystarczy tych prób")


grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja średnia wynosi {average:.2f}")

