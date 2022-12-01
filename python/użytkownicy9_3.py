#użytkownicy

class User():
    def __init__(self, first_name, last_name, age, sex,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print(f"Imię: {self.first_name.title()}, nazwisko: {self.last_name.title()}, wiek{self.age}, płeć {self.sex}")

    def greet_user(self):
        print(f"Witaj {self.first_name.title()} {self.last_name.title()}")

user_1 = User('aneta','gawron', 37, 'kobieta' )
user_1.describe_user()
user_1.greet_user()