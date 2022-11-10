#kalkulator budżetu miesięcznego
print("Kalkulator budżetu miesięcznego")
expenditures = {}
while True:
    category_name = input("podaj kategotię wydatków  albo zakończ podając 'X'")
    if category_name == 'X':
        break
    expenditures[category_name] = []

    while True:
        expenditure = (input(f"Podaj wartość następnego wydatku w kategori {category_name} lub zakończ 'X'")
        if expenditure == 'X':
            break

        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)

    total_expendures = 0
    for category_expendures in expenditures.values(): #dla wydatków z kazdej kategori
        for expenditure_value in category_expendures:
            total_expendures += expenditure_value
        #total_expendures += sum(expenditure_value)

expenditure_percentage = {}
for category_name, category_expendures in expenditure.items():
    #total_category_expendures = 0
    #for expenditure_value in category_expendures:
     #   total_category_expendures += expenditure_value
    total_category_expendures = sum(category_expendures)
    expenditure_percentage[category_name] = total_category_expendures * 100 / total_expendures

most_important_category = None
most_important_category_percentage = 0
for category, percentage in expenditure_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_category is None:
    print(f"Najwięcj wydajesz na {most_important_category} - {most_important_category_percentage}")
for category, percentage in expenditure_percentage.items():
    print(f"Na {category} wydajesz {percentage:.0f} % miesięcznych wydatków ")
