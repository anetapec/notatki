class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.hight = height

    def count_surface_area(self):
        return self.width * self.hight

class Square(Rectangle):
    def __init__(self, sideLenght):
        super().__init__(sideLenght, sideLenght)


class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return super().count_surface_area() * self.hight

cube = Cube(2)
print(cube.count_surface_area())