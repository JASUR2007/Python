# 1. Create a Book Class
# Define a class Book with a constructor that initializes title and author.
# Add a method describe() that prints the book title and author.
# Create two instances of Book and call the describe() method.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book1.describe()
book2.describe()

# 2. Design a Student Class
# Define a class Student with a constructor to initialize name and grade.
# Add a method greet() that prints a greeting with the student’s name.
# Add another method is_passing() that checks if the grade is greater than or equal to 50.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def greet(self):
        print(f"Name: {self.name}, grade: {self.grade}")
    def is_passing(self):
        if self.grade > 50:
            return 'great'
        else:
            return 'less than 50'

# 3. Create a Circle Class
# Define a class Circle with a constructor that initializes radius.
# Add a method area() to calculate and return the circle’s area (use 3.14 * radius * radius).
# Add another method circumference() to calculate the circumference (2 * 3.14 * radius).

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    
    def area(self):
        if self.radius < 0:
            return "Circle cant be less than 0"
        else: 
            return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(7)

print(f"Area: {circle.area()}")
print(f"circumference: {circle.circumference()}")
# 4. Build a Car Class
# Define a class Car with a constructor to initialize brand and mileage.
# Add a method display_info() that prints the brand and mileage.
# Add another method drive() that increases the mileage by a specified amount.

class Car:
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage
    
    def display_info(self):
        return(f"Brand: {self.brand}, Mileage: {self.mileage}")
    def drive(self, amount):
        self.mileage += amount
        return self.display_info()

car = Car("Matiz", 100)

print(car.display_info())
print(car.drive(30))

# Tasks
# 5. Design a Pet Class
# Define a class Pet with a constructor to initialize name and species.
# Add a method introduce() that says "I am a [species] and my name is [name]."
# Create multiple pet objects and call their introduce() method.

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def introduce(self):
        return f"Species: {self.species}, name: {self.name}."

pet1 = Pet("Shpic", "Dog")

print(pet1.introduce())

pet2 = Pet("Like", "Cat")

print(pet2.introduce())

# 6. Create a TemperatureConverter Class
# Define a class TemperatureConverter with no attributes.
# Add a method celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit (celsius * 9/5 + 32).
# Add another method fahrenheit_to_celsius(fahrenheit) that converts Fahrenheit to Celsius.

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9/5 + 32
    
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

converter = TemperatureConverter()

print(converter.celsius_to_fahrenheit(32))
print(converter.fahrenheit_to_celsius(86))

# 7. Build a Person Class
# Define a class Person with a constructor to initialize name and age.
# Add a method birthday() that increments the age by 1.
# Add another method introduce() to print "Hi, I am [name] and I am [age] years old."

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1
        return self.age
    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

person = Person("Akobir", 30)
print(person.introduce())
print(person.birthday())
print(person.introduce())

# 8. Create a Rectangle Class
# Define a class Rectangle with a constructor to initialize width and height.
# Add a method area() to calculate the area (width * height).
# Add another method scale(factor) to multiply both width and height by a scaling factor.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        return f"Scaling width: {self.width}, height: {self.height}"

# 9. Design a ShoppingCart Class
# Define a class ShoppingCart with an empty list as an attribute to hold items.
# Add a method add_item(item) to add an item to the list.
# Add another method view_cart() to print all items in the shopping cart.

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def view_cart(self):
        for item in self.items:
            print(item)
        return item

shop = ShoppingCart()

shop.add_item('Mokicj')
shop.add_item('Rocl')
print(shop.view_cart())


    
# 10. Create a BankAccount Class
# Define a class BankAccount with a constructor to initialize account_holder and balance (default to 0).
# Add a method deposit(amount) to increase the balance by amount.
# Add another method withdraw(amount) to decrease the balance by amount.
# Add a method check_balance() to display the current balance.


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Insufficient funds"
    def check_balance(self):
        return self.balance

bank = BankAccount("jasur", 20)
bank.deposit(400)
bank.withdraw(300)

print(bank.check_balance())


