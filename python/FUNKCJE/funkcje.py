unprinted_projects = ['etui na telefon', 'spongebob', 'zabawka']
complited_projects  = []
#symulujemy wydruk niezrealizowanych projektów dopóki nie znajdą się na liście complited_project
while unprinted_projects:
    current_project = unprinted_projects.pop()    #nowa zmienna current_project
    print(f"Wydruk modelu: {current_project}")    # !!
    complited_projects.append(current_project)    #dodajemy do listy complited_projects


#wyświetlenie wszystkich wydrukowanych modeli:

print("\nWydrukowane zostały następujące modele:")
for complited_project in complited_projects:
    print(complited_project)



