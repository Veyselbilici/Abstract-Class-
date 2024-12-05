from Shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return f"Çember: Yarıçap={self.__radius}, Alan={self.get_area()}, Çevre={self.get_perimeter()}"