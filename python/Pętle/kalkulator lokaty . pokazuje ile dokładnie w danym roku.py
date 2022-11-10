
print("Kalkulator wartości lokaty z roczną kapitalizacją")
initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś ?")
initial_value = int(initial_value_input)
time_input = input("Na jaki czas ?")
time = int(time_input)
percentage_input = input("Jakie jest oprocentowanie ?")
percentage = int(percentage_input)



for time in range (1,time + 5):
    final_value = initial_value * (1 + percentage / 100) ** time
    print(f"Po {time} latach Twoja lokata będzie warta {final_value:.2f}")