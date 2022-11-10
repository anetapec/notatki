#poproś o listę zakupów i określ czy lista jest długa

shoping_elements = input("Wprowadź listę zakupów ,oddzielając pozycje przecinkami ")
shoping_list = shoping_elements.split(",")
is_shoping_list_longht = len(shoping_list) > 4
print(f"Czy uważam, że Twoja lista zakupów jest długa ? {is_shoping_list_longht}")