from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        pass