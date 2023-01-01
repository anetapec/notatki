import re

def run_example():
    number_at_begin_txt = "+48 415 765 786 <- to jest numer"
    number_patern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    number_match = number_patern.match(number_at_begin_txt)

    #całe dopasowanie

    print(number_match.group())
    print(number_match.group(0))

    #poszczególne grupy

    print("Grupa 1:", number_match.group(1))
    print("Grupa 2:", number_match.group(2))

    print(number_match[1])

    for group_number, group in enumerate(number_match.groups()):
        print(f"Grupa {group_number + 1}:", group)

    print("*" * 30)

    #pozycja znalezionych dopasowań

    print(number_match.start(),number_match.end())
    print(number_match.start(1), number_match.end(1))
    print(number_match.start(2), number_match.end(2))




if __name__ == '__main__':
    run_example()