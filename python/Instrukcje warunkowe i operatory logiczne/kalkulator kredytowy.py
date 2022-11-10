'''
#sprawdz swoją zdolność kredytową

income = 4000
expenditures = 2000
age = 35

if age < 18 or income < expenditures :
    print("Nie możesz wziąć kredytu")
else:
    print("Możesz wziąć kredyt")
'''

###czy stać użytkownika na kredyt hipoteczny###
#Zapytaj o :
# kwotę kredytu
# oprocentowanie
# wartość wkładu własnego
# czas kredytowania w latach
# przychód miesięczny
# sumę wydatków w miesiącu

# oblicz ratę ze wzoru
#####(Kwota kredytu * oprocentowanie / 100) * 12 + kwota kredytu / (liczba lat * 12)

#dostępne środki = przychód - suma wydatków
#wartość nieruchomości = wkład własny + kwota kredytu

value_kredit = int(input("Jaką kwotę chcesz dostać?"))
percentage = int(input("Jakie ma być oprocentowanie kredytu?"))
own_contribution = int(input("Jaka jest wartość wkładu własnego"))
time = int(input("Na ile lat ma być kredyt ?"))
income = int(input("Jaki jest Twój przychód miesęczny?"))
expenses = int(input("Ile wynoszą Twoje miesięczne wydatki"))

installment_vallue = (value_kredit * percentage / 100) * 12 + value_kredit / (time * 12)
print(f"Rata miesięczna kredytu będzie wynosić {installment_vallue} zł.")

available_funds = income - expenses
value_of_the_property = own_contribution + value_kredit

own_contribution_part = own_contribution / value_of_the_property
money_over_installment = available_funds - installment_vallue

matching_higher_own_part = own_contribution_part >= 0.2 and money_over_installment >= 1000 #postawiony warunek
matching_lower_own_part = own_contribution_part >= 0.1 and money_over_installment >= 2000 #postawiony warunek

if matching_lower_own_part or matching_lower_own_part :
    print("Możesz dostać kredyt")
else:
    print("Niestety , nie dostaniesz kredytu.")


