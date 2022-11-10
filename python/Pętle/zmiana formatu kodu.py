
# wypisujemy kod pocztowy - znak po znaku

post_code = input("Jaki jest Twój kod pocztowy? ")
letter_indeks = 0
while letter_indeks < len(post_code):
    print(f"[{letter_indeks}] -> {post_code[letter_indeks]}")
    letter_indeks += 1


#zamieniamy kod pocztowy by miał formay XX-XX-XX

post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formated_post_code = ""
letter_indeks = 0
while letter_indeks < len(post_code):
    if letter_indeks % 2 == 0 and letter_indeks != 0:  #do każdego codrugiego indeksu , o ile nie jest on na początku
        formated_post_code += "-"                         #dodajemy "-"
    formated_post_code += post_code[letter_indeks]     #pilnować wcięć!!!!!
    letter_indeks += 1
print(formated_post_code)
