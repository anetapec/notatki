#Poproś użytkownika o wprowadzenie ocen, które uzyskał/a.
# Jeśli wprowadzisz wszystkie ,daj X


grades= []

grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X'")
while grade_input != 'X':
    grade = int(grade_input)
    grades.append(grade)
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X'")

#oblicz średnią z podanych ocen
grades_sum = 0
for grade in grades:
    grades_sum += grade

average = grades_sum / len(grades)
print(f"Twoja średnia wynosi {average:.2f}")

### sumę możemy obliczyć też:

grades_sum = sum(grade)

