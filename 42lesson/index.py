from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectange(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        print(f"Area of rectangle {self.height * self.width}")
    def perimeter(self):
        print(f"Perimeter of rectangle {2*(self.height * self.width)}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area of  circle {math.pi * self.radius**2}")
    def perimeter(self):
        print(f"Perimeter of circle {2*math.pi * self.radius}")
rectange = Rectange(4, 5)
circle = Circle(5)

rectange.area()
circle.area()








