#znajdz liczby podzielne przez 7 ale nie przez 5 ze zbioru 100 do 470

numbers = (
    number
    for number in range(100,471)
    if (number % 7 == 0)
    if (number % 5 != 0)
    )
for number in numbers:

    print(number)

