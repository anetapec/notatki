
import re
def run_example():
    adres_email= ["nazwa@domena.pl", "aneta32@gmail.pl", "wikusia14@o2.com"]
    uncorect_email = ["anetapecka@gmailcom", "nazwadomena.com", "wikusiacom"]

    pattern = re.compile(r"\w+@\w+\.\w+")

    for adres in adres_email:
        print(pattern.findall(adres))

    for adres in uncorect_email:
        print(pattern.findall(adres))


if __name__ == '__main__':
    run_example()



