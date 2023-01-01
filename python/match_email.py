import re

def run_example():
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email_adress = input("Podaj swój adres email:")

    email_match = email_pattern.fullmatch(email_adress)

    print(f"Nazwa:", email_match.group(1))
    print(f"Domena:", email_match.group(2))
    print(f"Rozszerzenie domeny:", email_match.group(3))

if __name__ == '__main__':
    run_example()


