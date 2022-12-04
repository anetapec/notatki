#Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.
#Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.
#Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.
#Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.

def open_file(name_file):

    try:
        with open(name_file, "r", encoding='utf-8') as file_object:
            return file_object.read()

    except FileNotFoundError:
        print("Nie znaleziono pliku ,podaj właściwą scieżkę")
name_file = input("Jaki plik chcesz otworzyć?")
openen_file = open_file(name_file)


