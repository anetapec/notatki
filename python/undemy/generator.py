#zsumuj liczby od 0 do 100 podniesione do potęgi 2

#usuń imiona zaczynające się od litery b ze zbioru

squared = (
    element ** 2
    for element in range(101)
    )
print(squared)


numbers_generator = (squared
                    for squared in range(101)
                     )

print(sum(numbers_generator))

