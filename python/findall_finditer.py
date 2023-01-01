import re

def run_example():
    example_text = "To są adresy email: anetapecka@gmail.com, jakis@hot.pl, kod@haha.com.pl"
    find_all_emails(example_text)

def find_all_emails(text):
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email_matches = email_pattern.findall(text)
    for email_match in email_matches:
        print_email_details(email_match)

def print_email_details(email_match):
    print("_" * 30)
    print(f"Adres email:")
    print(f"Nazwa:", email_match[0])
    print(f"Domena", email_match[1])
    print(f"Rozszerzenie domeny:", email_match[2])


if __name__ =='__main__':
    run_example()