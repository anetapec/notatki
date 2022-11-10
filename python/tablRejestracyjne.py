# modyfikacja tablic rejestracyjnych by miały format wielkie litery bez spacji

ford = "abc12033"
mazda = "HHH 0987"
hundai = "kkK-0876"

ford = ford.upper()
mazda = mazda.upper().replace(" ", "")
hundai = hundai.upper().replace("-", "")

print(f"Ford: {ford}")
print(f"Mazda: {mazda}")
print(f"Hundai: {hundai}")

