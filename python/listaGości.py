#lista gości , zaproszenie każdego z osobna
#czy da się to zrobić 1 komunikatem ??

#3.4 str 83

lista = ['Ania', 'Kasia', 'Ola']
message0 = f"Witaj {lista[0].title()} chciałam zaprosić Cię na obiad"
print(message0)
message1 = f"Witaj {lista[1]} chchciałam zaprosić Cię na obiad"
print(message1)
message2 = f"Witaj {lista[2]} chciałam zaprosić Cię na obiad"
print(message2)

# zastąpienie 1 gościa ćwicz 3.5
lista = ['Ania', 'Kasia', 'Ola']
change = f"Niestety {lista[1]} nie może przyjść."
print(change)
lista[1] = 'Gosia'
print(lista)

invite0 = f"Witaj {lista[0]} chciałam zaprosić Cię na obiad"
print(invite0)
invite1 = f"Witaj {lista[1]} chciałam zaprosić Cię na obiad"
print(invite1)
invite2 = f"Witaj {lista[2]} chciałam zaprosić Cię na obiad"
print(invite2)

#zaproś więcej gości 3.6
change = "Masz większy stół. Możesz zaprosić dodatkowo 3 osoby"
print(change)
lista1=lista
print(lista1)
lista1.insert(0, 'Bartek')
print(lista1)
lista1.insert(2, 'Marta')
print(lista1)
lista1.append('Marta')
print(lista1)

#3.7 zostało miejsce jedynie dla 2 gości

change1 = "Niestety większy stół nie został dostarczony . Możesz zaprosić jedynie 2 osoby "
print(change1)
popped_lista1 = lista1.pop
print(lista1)
print(popped_lista1)

print(f"Na liście jest" , len(lista1), "osób.")

