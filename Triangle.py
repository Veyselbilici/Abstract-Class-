from Shape import Shape
import math
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def set_side1(self, side1):
        self.__side1 = side1

    def get_side2(self):
        return self.__side2

    def set_side2(self, side2):
        self.__side2 = side2

    def get_side3(self):
        return self.__side3

    def set_side3(self, side3):
        self.__side3 = side3

    def get_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Üçgen: Kenar1={self.__side1}, Kenar2={self.__side2}, Kenar3={self.__side3}, Alan={self.get_area()}, Çevre={self.get_perimeter()}"