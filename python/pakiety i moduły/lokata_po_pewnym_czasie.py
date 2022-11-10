#kalkulator lokaty po pewny czasie
#Żle!!! poprawić!!!!
import kalkulator
def ask_for_int_value(message):
    value = int(input(message))
    return value

print("Kalkulator wartości lokaty z rocznym oprocentowaniem")
# start_capital
start_capital = ask_for_int_value(("Jaką kwotę wpłaciłeś?"))
percentage = ask_for_int_value("Jakie ma być oprocentowanie?")
time = ask_for_int_value("Ile lat trwa lokata?")

finnal_value = calc_location.value(initial_value,percentage,time)
print(f"Po {time} latach , wartość lokaty będzie wynosić {finnal_value:.2f} zł.")
