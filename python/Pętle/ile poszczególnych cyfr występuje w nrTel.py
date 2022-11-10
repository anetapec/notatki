# metoda count - podaje liczbę wystąpień danego znaku

 #poproś użytkownika o podanie numeru telefonu ,następnie wypisz informacje ile razy występuje w nich kazda cyfra
phone_number = input("Podaj numer telefonu: ")
for digit in range(10):
    digit_times_in_number = phone_number.count(str(digit))   #zamieniamy na stringa bo in range
    print(f"Cyfra{digit} występuje w Twoim imieniu {digit_times_in_number} razy.")