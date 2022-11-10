# Funkcja in pozwala sprawdzć czy dana litera znajduje się w napisie

name = "Katarzyna"
if "r" in name:
    print("W imieniu jest 'r'")
else:
    print("W imieniu nie ma 'r'")

# możemy za jej pomocą sprawdzić czy element jest na liście

favorit_name = ["katarzyna", "ola", "ewa", "adam"]
if "ola" in favorit_name:
    print("Ola jest na liście")
else:
    print("Oli nie ma na liście.")

#oraz czy klucz występuje w słowniku

person = {"first_name": "Aneta","last_name": "Gawron", "age": 37, "pesel": "987654329"}
if "first_name" in person:
    print(person["first_name"])

#można sprawdzić też przez negację

if not "pesel" in person:
    print("Brak podanego peselu")
else:
    print(f"Pesel:",person["pesel"])
#można też czytelniej
if "pesel" not in person:
    print("Brak podanego peselu")
else:
    print(f"Pesel:",person["pesel"])


