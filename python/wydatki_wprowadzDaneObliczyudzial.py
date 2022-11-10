#zapytaj ile wydaje miesiecznie pieniedzy na..
#oblicz % udział kategorii w wydatkach
#poproś użytkownika o wybranie kategori i podaj % udział w wydatkach

wydatki_jedzenie = float(input("Ile wydajesz miesięcznie na jedzenie ?"))
wydatki_rozrywka = float(input("Ile wydajesz miesięcznie na rozrywkę ?"))
wydatki_oplaty = float(input("Ile wydajesz miesięcznie na opłaty ?"))
wydatki_inne = float(input("Ile wydajesz na pozostałe rzeczy ?"))

wszystkie_wydatki = wydatki_jedzenie + wydatki_rozrywka + wydatki_oplaty + wydatki_inne

procentowy_udział = {
    "jedzenie": wydatki_jedzenie * 100 / wszystkie_wydatki,
    "rozrywka": wydatki_rozrywka * 100 / wszystkie_wydatki,
    "oplaty": wydatki_oplaty * 100 / wszystkie_wydatki,
    "pozostale": wydatki_inne * 100 / wszystkie_wydatki
}

poszczegolna_kategoria = input("Wybierz jedną z kategori wydatków (jedzenie / rozrywka / oplaty / pozostałe): ")
print(f"Na {poszczegolna_kategoria} wydajesz {procentowy_udział[poszczegolna_kategoria]:.0f} % wszystkich wydatków"
