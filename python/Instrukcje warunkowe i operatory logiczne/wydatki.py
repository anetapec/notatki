wydatki_jedzenie = float(input("Ile wydajesz miesięcznie na jedzenie ?"))
wydatki_rozrywka = float(input("Ile wydajesz miesięcznie na rozrywkę ?"))
wydatki_oplaty = float(input("Ile wydajesz miesięcznie na opłaty ?"))
wydatki_inne = float(input("Ile wydajesz na pozostałe rzeczy ?"))
wszystkie_wydatki = wydatki_jedzenie + wydatki_rozrywka + wydatki_oplaty + wydatki_inne

procentowy_udzial = {
    "jedzenie": wydatki_jedzenie * 100 / wszystkie_wydatki,
    "rozrywka": wydatki_rozrywka * 100 / wszystkie_wydatki,
    "oplaty": wydatki_oplaty * 100 / wszystkie_wydatki,
    "pozostale": wydatki_inne * 100 / wszystkie_wydatki
}


najwazniejsza_kategoria = "jedzenie"

if procentowy_udzial["rozrywka"] > procentowy_udzial[najwazniejsza_kategoria]:
    najwazniejsza_kategoria = "rozrywka"
if procentowy_udzial["oplaty"] > procentowy_udzial[najwazniejsza_kategoria]:
    najwazniejsza_kategoria = "oplaty"
if procentowy_udzial["pozostale"] > procentowy_udzial[najwazniejsza_kategoria]:
    najwazniejsza_kategoria = "pozostale"
if procentowy_udzial["pozostale"] > procentowy_udzial[najwazniejsza_kategoria]:
    najwazniejsza_kategoria = "pozostale"
print(f"Najwięcej wydajesz na {najwazniejsza_kategoria} - {procentowy_udzial[najwazniejsza_kategoria]:.0f} % wszystkich wydatków.")