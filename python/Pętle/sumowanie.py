#sumowanie liczb
numbers = [1, 3, 5, 35, 48, 123, 510]
numbers_sum = 0 #zmienna która będzie sumą
numbers_indeks = 0 #zmienna dzięki której będziemy przeskakiwać przez poszczegółny element listy
while numbers_indeks < len(numbers):
    numbers_sum += numbers[numbers_indeks]    ##  += TO skrót OD numbers_sum = numbers_sum + number[number_index]
    numbers_indeks += 1                        #  += GDY CHCEMY COŚ ZWIĘKSZYĆ O 1
print(f"Suma{numbers_sum}")

name = "Aneta"
# pierwsza litera
print("Pierwsza ltera imienia to", name[0])
print("Ostatnia litera imienia to:", name[-1])
print("Pierwsze 3 litery imienia to:", name[:3])
print("Wszystkie litery imienia poza pierwszą to:", name[1:])

# nie zadziała !!!

#    name[0] = N
#    print(name[0])

#nie podmieni nam w ten sposób A na N ale można to zrobić tak :
# nie modyfikuje zapisu ale tworzy nowy zapis

name = "N" + name[1:]
print(name)

# metoda .split()  = ROZBIJE NAM ZDANIE NA LISTĘ
words = "To jest całe zdanie" .split()
print(words)
print("Pierwsze słowo to:", words[0])
