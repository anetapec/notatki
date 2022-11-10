#tworzenie listy liczb

numbers = list(range(1, 6))
print(numbers)

# range() by pominąć liczby w podanym zakresie DODAJĄC TRZECI ARGUMENT FUNKCJI range()

# lista liczb parzystych od 1 do 10

numbers = list(range(2, 11, 2))
print(numbers)

# lista kwadratów pierwszych 10 liczb

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# lub prościej
square = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# lista składana
squares = [value ** 2 for value in range(1, 11)]
print(squares)
#