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

#grades_sum = sum(grade)

#poproś użytkownika o nr tel i sformatuj go XXX-XXX-XXX

phone_number = input("Podaj swój numer telefonu")
phone_number = phone_number.replace("-", "")
phone_number_formated = ""

for number ,digit in enumerate(phone_number):
    if number % 3 == 0 and number != 0:
        phone_number_formated += "-"
    phone_number_formated += phone_number[number]

print (f"Twój numer telefonu to: {phone_number_formated}")



