def calc_equation(a,b,c):

    value_x = (c - b) / a
    return value_x

a = float(input("Podaj wartość a:"))
b = float(input("Podaj wartość b:"))
c = float(input("Podaj wartość c:"))
if a != 0:
    value_x = calc_equation(a,b,c)
    print(f"Dla a = {a}, b = {b}, c ={c}, wartość x wynosi: {value_x:.2f}")
else:
    print("Wartość parametru a musi być różna od 0.")
