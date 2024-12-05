from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return f"Dikdörtgen: Uzunluk={self.__length}, Genişlik={self.__width}, Alan={self.get_area()}, Çevre={self.get_perimeter()}"