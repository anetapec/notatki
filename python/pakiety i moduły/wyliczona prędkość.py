import avg_speed



distance = float(input("Ile kilometrów przebiegłeś ?"))
time = float(input("Ile godzin Ci to zajęło?"))
avg_speed = avg_speed.avg_speed(distance,time)
print(f"Biegłeś ze srednią prędkością {avg_speed} km/h . ")

