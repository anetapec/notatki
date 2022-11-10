#Utwórz listę zawierającą różne liczby i skorzystaj z instrukcji continue, aby wypisać tylko liczby nieparzyste.

numbers = [35, 12, 134, 123, 53, 97]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

