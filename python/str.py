#Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30
# podzielne kolejno przez 3 oraz przez 5.
#To znaczy, że na pierwszej liście powinny znaleźć się liczby od 1 do 30 podzielne przez 3,
# a na drugiej liście liczby od 1 do 30 podzielne przez 5.
#Następnie, połącz obie listy w jedną i wypisz wynik.

def run_homework():
    numbers_divisible_by3 = [number for number in range(30) if number % 3 == 0]
    print(numbers_divisible_by3)
    numbers_divisible_by5 = [number for number in range(30) if number % 5 == 0]
    print(numbers_divisible_by5)
    #liczby podzielne przez 3 i podzielne przez 5 od 1 do 30
    searched_numbers = numbers_divisible_by3 + numbers_divisible_by5
    print(searched_numbers)

if __name__ == '__main__':
    run_homework()