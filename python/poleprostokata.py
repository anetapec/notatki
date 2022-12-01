#program obliczający pole prostokata str89 zadania

class Rectangle:

    def __init__(self):
        print("Program oblicza pole prostokąta dla bokó a i b")


    def read_data(self):
        self.a = float(input("Podaj długość boku a"))
        self.b = float(input("Podaj długość boku b"))

    def process_data(self):
        self.rectangle = self.a * self.b
        return self.rectangle

    def display_result(self):
        print(f"Pole prostokąta o długości a: {self.a} i b: {self.b} wynosi {self.rectangle}")

def run_rectangle():
    rectangle1 = Rectangle



    rectangle1.read_data()
    rectangle1.process_data()
    rectangle1.display_result()

if __name__ == '__main__':
    run_rectangle()