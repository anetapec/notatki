polisch_to_english = {
    "kot": "cat",
    "pies": "dog",
    "mleko": "milk"
}
print("Słownik polsko-angielski:", polisch_to_english)

#dostęp za pomocą klucza
print(f"Po polsku 'kot' to po angielsku '{polisch_to_english['kot']}'")

#można wykorzystać do tworzenia listy wydatków

wydatki = {
    "prąd": 50 ,
    "gaz": 23.68,
    "zakupy" : [34.5, 27.70, 99]
}
print(wydatki)

#słownik może zawierać inne słowniki
mix = {
    "kot": "cat",
    "pies": "dog",
    "mleko": "milk",
    "wydatki":  {
        "prąd": 50 ,
        "gaz": 23.68,
        "zakupy" : [34.5, 27.70, 99]
    }
}
print(mix)

#lista może zawierać słownik i słownik moze zawierać listę

students = [
    {
        "first_name": "Aneta",
        "last_name": "Gawron",

    },
    {
        "first_name": "Klaudia",
        "last_name": "Kowalska",
    }
]
print(students)
print(students [0])
print(students[1],["first_name"])

