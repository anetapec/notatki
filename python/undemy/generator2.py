#Nieskończony generator kolejnych liczb przemnożonych przez siebie (1,4,9,16,25,36 itd)
#Skorzystaj z funkcji generując 20 elementów,
# po czym wróć do momentu zakończenia i wygeneruj następnie 30 liczb.
# Zapisz wygenerowane elementy w tej samej liście.

def generator_even_numbers():
    x = 0
    while True:
        x = x + 1
        yield x * x

generate_numbers = []

number_generator = generator_even_numbers()
for _ in range(20):
    generate_numbers.append(next(number_generator))
print(generate_numbers)

for _ in range(30):
    generate_numbers.append(next(number_generator))
print(generate_numbers)
