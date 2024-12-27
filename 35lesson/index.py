class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def Bark(self):
        print(f"{self.name} is barking")


dog = Dog("rels", 5)
dog.Bark()


class Students():
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def info(self):
        return f"Name: {self.name}, address: {self.address}, age: {self.age}"

class Sherzod(Students):
    def hobby(self):
        print(f"{self.name}'s is football.")


student1 = Students('SHera', 'Polman 1', 30)


# . Task: Shapes and Areas
# Create a parent class Shape with a method area() that returns 0 (a default value).
# Create child classes Rectangle and Circle.
# Rectangle should calculate the area of a rectangle.
# Circle should calculate the area of a circle.
    
class Shape:
    def area(self):
        return 0 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)  

rectangle = Rectangle(4, 5)
print(f"Area Rectangle: {rectangle.area()}") 
    
circle = Circle(3)
print(f"Area Circle: {circle.area()}") 