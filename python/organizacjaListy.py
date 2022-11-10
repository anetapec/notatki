places = ['Himalaje', 'Australia', 'Afryka', 'Kolorado', 'Bałtyk']
print("Oto lista pierwotna :", (places))
# sorted = alfabetycznie - tymczasowo
print("\nOto lista posortowana alfabetycznie:")
print(sorted(places))
print(places)

# reverse - trwale ale można odwrócic ponownie przez reverse. odwrotnie
places.reverse()
print(places)
places.reverse()
print(places)

lista = ['Ania', 'Kasia', 'Ola', 'Bartek', 'Marta']
len(lista)
print(lista)
#sprawdz czy wybrane jakieś miejsca są na liście
if 'Afryka' and 'Himalaje' in places:
    print("Afryka i Himalaje znajdują się na liście.")
else:
    print("Niestety ...")

if 'Mazury' in lista or 'Himalaje' in lista:
    print("Są")

#sprawdz czy na liście są np 2 pozycje z czego jednej nie ma :