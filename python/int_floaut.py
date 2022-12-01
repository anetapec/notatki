#Wylosuj 6 liczb typu float z przedziału od -20 do 20
# oraz 3 liczby całkowite z przedziału od 1 do 10.
#Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
#Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej, drugiej i trzeciej
# wylosowanej liczby całkowitej.
import math
import random

def run_example():
    numbers_float = []
    for _ in range(6):
        numbers_float.append(random.uniform(-20,20))
    print(numbers_float)

    numbers_int = []
    for _ in range(3):
        numbers_int.append(random.randint(1,10))
    print(numbers_int)
# zaokrąglamy
    print(round(numbers_float[0]))
    print(math.ceil(numbers_float[1]))
    print(math.floor(numbers_float[2]))
#podnosimy do potęgi
    print(numbers_float[3] ** numbers_int[0])
    print(pow(numbers_float[4], numbers_int[1]))
    print(math.pow(numbers_float[5], numbers_int[2]))


if __name__ == '__main__':
    run_example()