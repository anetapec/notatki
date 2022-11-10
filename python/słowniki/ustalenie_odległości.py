#monitorowanie położenia obcego , który porusza się z RÓŻNĄ SZYBKOŚCIĄ

#w słowniku przechowaj BIEŻĄCĄ SZYBKOŚĆ i użyj do ustalenia ODLEGŁOŚCI

alien_0 = {'x_position': 0, 'y_position':25, 'speed': 'średnio'}
print(f"Początkowa wartość x-position: {alien_0['x_position']}")

#przesunięcie obcego w prawo
#ustalenie odległości,jaką powinien pokonac obcy poruszający się z daną szybkością

if alien_0['speed'] == 'wolno':
    x_increment = 1
elif alien_0['speed'] == 'śednio':
    x_increment = 2
else:
    #to musi być szybki obcy
    x_increment = 3
#nowe położenie to suma dotychczasowego położenia i wartości x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Nowa wartość x_position: {alien_0['x_position']}")