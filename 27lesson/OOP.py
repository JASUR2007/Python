class Book():
    def __init__(self, title, author,year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_description(self):
        return f"The book {self.title} was written by {self.author} in {self.year}. It is a {self.genre} book"
        
book1 = Book('Samurai without sword', 'Kitamni  Massao', '1463', 'authobiography')
book2 = Book('FairyTales', 'Brother Grim', '1443', 'Fantasy')
book3 = Book('Tuesdays with Morrie', 'Mitch Albon', '1***', 'Story')

print(book1.get_description())
print(book2.get_description())
print(book3.get_description())



class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):        
        return f"Area is {self.width * self.height}, perimeter is {2*(self.width + self.height)}"

per1 = Rectangle(4,3)
print(per1.area()) 

class Car:
    def __init__(self, model, color):
        self.model = model  
        self.color = color  
        self.speed = 0

    def accelerate(self, increase):
        self.speed += increase
        print(f"Автомобиль ускорился до {self.speed} км/ч.")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0  
        print(f"Автомобиль замедлился до {self.speed} км/ч.")

    def get_info(self):
        return f"Модель: {self.model}, Цвет: {self.color}, Текущая скорость: {self.speed} км/ч."

my_car = Car("Tesla Model S", "черный")
print(my_car.get_info()) 

my_car.accelerate(50)
my_car.accelerate(30) 
my_car.brake(20)  
my_car.brake(70)  




def F(n):
    if n < 2:
        return 0
    if n % 2 == 0:
        return int(3 * F(n / 2) + n / 4 * (n / 2 - 1))
    return int(2 * F((n - 1) / 2) + F((n + 1) / 2) + ((n - 1) / 4) * ((n + 1) / 2))

n = int(input())
print(F(n))

