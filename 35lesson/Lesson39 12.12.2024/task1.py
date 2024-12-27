# 1. Task: Shapes and Areas
# Create a parent class Shape with a method area() that returns 0 (a default value).
# Create child classes Rectangle and Circle.
# Rectangle should calculate the area of a rectangle.
# Circle should calculate the area of a circle.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self, a,b):
        return a*b
class Circle(Shape):
    def area(self, radius):
        return 3.14*radius**2
rectangle=Rectangle()
print(rectangle.area(10,5))

circle=Circle()
print(circle.area(2))
