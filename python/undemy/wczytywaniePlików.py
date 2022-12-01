#Wczytaj plik
#1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
#pary imiona/nazwiska
#2) zapisz imiona do pliku imiona.txt
#3) zapisz nazwiska do pliu nazwiska.txt
#Zastanów się jak rozwiązać problem,
#gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
#zapsywał nazwiska do pliku nazwiska.txt

#[
 #("Arkadiusz", "Włodarczyk"),
#("Jakis", "Ziom")
#]

with open("imionanazwska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)