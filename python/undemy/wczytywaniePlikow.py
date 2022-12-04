#wczytaj imiona i nazwiska z pliku , zapisz je w listę krotek
#zapisz imiona do pliku imiona a nazwiska do pliku nazwiska

namesandsurnames = []
with open('imionanazwiska.txt', "r", encoding='utf-8') as file_object:
    for line in file_object:
        namesandsurnames.append(tuple(line.replace("\n", "").split(" ")))
        #usuwamy entery , rozdzielamy linie na krotki wzgledem spacji
print(namesandsurnames)
#tworzymy plik imiona
with open('imiona.txt', "w", encoding='utf-8') as file_object:
    for item in namesandsurnames:
        file_object.write(item[0] + "\n")
#tworzymy plik nazwiska
with open('nazwiska.txt', "w", encoding='utf-8') as file_object:
    for item in namesandsurnames:
        try:
            file_object.write(item[1] + "\n")
        except IndexError:
            file_object.write("\n")
