# program licący wartość lokaty + zaokrąg do 2 miejsc po przecinku

print("Kalkulator wartości lokaty z rocznym oprocentowaniem")
initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś ?")
initial_value = int(initial_value_input)
time_input = input("Na jaki czas ?")
time = int(time_input)
percentage_input = input("Jakie jest oprocentowanie ?")
percentage = int(percentage_input)

final_value = initial_value * ( 1 + percentage / 100) ** time

print(f"Wartość lokaty po okresie " , time, "lat będzie wynosić: final_value:.2f ")
print(final_value)
capital_growth = final_value - initial_value
capital_growth_percentage = ( capital_growth / initial_value ) * 100
print("Po", time, "latach Twoja lokta będzie wynosić" , final_value )
print(f"Czy wartość Twojej lokaty wzrośnie w planowanym okresie o 10% lub więcej ? {capital_growth_percentage >= 10}")