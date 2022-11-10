#sprawdzamy czy użytkownik podał sensowną wartość

age = int(input("Ile masz lat?"))
while age < 1:
    if age < 1:
        print("Chyba nie ...\n")         #pamiętać o \n  !!!!!
        age = int(input("Ile masz lat?"))
if age < 18:
        print("Jeszcze nie możesz głosować")
else:
        print("Możesz już głosować !")

#drugi sposób:

age = int(input("Ile masz lat?"))
while age < 1:
    print("Chyba nie ...\n")  # pamiętać o \n  !!!!!
    age = int(input("Ile masz lat?"))

if age < 18:
    print("Jeszcze nie możesz głosować")
else:
    print("Możesz już głosować !")
