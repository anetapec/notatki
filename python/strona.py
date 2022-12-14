import re

def run_example():
    matching_page = ["http://www.jakasstrona.pl", "https://www.infoshareacademy.pl"]
    unmatching_page = ["www.jakasstrona.pl", "https:/www.infoshareacademy.pl" ]

    pattern = re.compile(r"https?://www.\w+\.\w+")
    pattern1 = re.compile(r"(?:(http|https)://)?www\.(\w+)\.(\w+)")
    for adres in matching_page:
        print(pattern.findall(adres))

    for adres in unmatching_page:
        print(pattern.findall(adres))

    print("#" * 30)
    for adres in matching_page:
        print(pattern1.findall(adres))

    for adres in unmatching_page:
        print(pattern1.findall(adres))

if __name__ == '__main__':
    run_example()