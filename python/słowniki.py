#słowniki
alien_0 = {'colour': 'zielony', 'points': 5}
print(alien_0)
print(alien_0['colour'])
print(alien_0['points'])

#jeżeli gracz zestrzeli obcego przyznajemy mu punkty
alien_0 = {'colour': 'zielony', 'points': 5}
new_points = alien_0['points']
print(f"Gratulacje zdobyłeś {new_points} punktów !")

#dodanie nowej pary klucz-wartość
alien_0 = {'colour': 'zielony', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#rozpoczęcie od pustego słownika
#JAK TWORZYĆ SŁOWNIK,DODAWAĆ SŁOWA KLUCZ-WARTOŚĆ
alien_0 = {}
alien_0['colour'] = 'zielony'
alien_0['points'] = 5
print(alien_0)

#modyfikowanie WARTOŚCI SŁOWNIKA
#ZMIEN KOLOR ZIELONY NA ZÓŁTY
alien_0 = {'colour': 'zielony'}
print(f"Obcy ma kolor {alien_0['colour']}") # POWSTANIE :Obcy ma kolor zielony
alien_0['colour'] = 'żółty'  #pamiętaj by dodać całe alien_0['colour']
print(f"Obcy ma teraz kolor {alien_0['colour']}")
