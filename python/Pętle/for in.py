#operacje na listach

#wypisz klucze ze słownika
expenditures = {
    'prąd': 250,
    'woda': 50,
    'czynsz': 500,
    'zakupy': [25, 64.45, 260]
}
for expenditure_element in expenditures:
    print(expenditure_element)

#wypisz klucze i ich wartości
for expenditure_element in expenditures:
    print(f"{expenditure_element} -> {expenditures[expenditure_element]}")

#klucze i wartości bezpośrednio
# drugi sposób item
for expenditure_element, expenditure in expenditures.items():
    print(f"{expenditure_element} -> {expenditure}")


#wypisz wartości
for expenditure in expenditures.values():
    print(expenditure)

#wypisujemy kod pocztowy wraz z informacją o kolejności
post_code = input("Jaki jest Twój kod pocztowy? ")
for index, letter in enumerate(post_code):
    print(f"{index} -> {letter}")

#wypisywanie co drugiego sportu
favorite_sports = ["bieganie", "pływanie", "jazda na rowerze" ,"jazda konno"]
for index, sport in enumerate(favorite_sports):
    if index % 2 == 0:
        print(sport)

#zmieniamy kod pocztowy by zawsze był zgodny z formatem XX-XX-XX
post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
for index, letter in enumerate(post_code):
    if index % 2 and index != 0:
        formatted_post_code += "-"
        formatted_post_code += letter
    print(formatted_post_code)