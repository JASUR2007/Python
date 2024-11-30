#  3. Task: Create a `Dog` Class with Methods
# Create a `Dog` class that has:
# - An attribute `name` (string).
# - An attribute `age` (integer).
# - A method `bark()` that prints `"Woof!"`.
# - A method `get_age_in_human_years()` that returns the dog's age in human years (1 dog year = 7 human years).

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
    def get_age_in_human_years(self):
        return f'My dog is {self.age * 7} years old'
    
animal = Dog('San', 17)
print(animal.bark())
print(animal.get_age_in_human_years())

#  4. Task: Create a `Car` Class with Methods
# Create a `Car` class that has:
# - `make` (string)
# - `model` (string)
# - `year` (integer)
# - `mileage` (integer)

# Add methods to
# - `drive(distance)`: This method should add the distance to the car’s `mileage` attribute.
# - `get_info()`: This method should return a string containing the car's make, model, year, and current mileage.

# Objective: This Task allows you to practice modifying attributes and working with methods that alter the state of the object.
class Car():
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage 
    def drive(self, distance):
        self.mileage += distance
        return self.mileage
    def get_info(self):
        return f'model: {self.model}, make: {self.make}, year: {self.year}, mileage: {self.mileage}'
cars = Car('we', 'lamborgini', '2023', 30)
print(cars.drive(30))
print(cars.get_info())


# 5. Task: Create a `Person` Class with `__init__`
# Create a `Person` class with:
# - `first_name` (string)
# - `last_name` (string)
# - `age` (integer)

# The `__init__` method should initialize the person's name and age. 
# Add a method `introduce()` that prints: `"Hello, my name is [first_name] [last_name], and I am [age] years old."`
class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f"name: {self.first_name}, surname: {self.last_name}, age: {self.age}"
    
per = Person('Jasur',"Rosov", 17)
print(per.introduce())

#  6. Task: Create an `Account` Class
# Create an `Account` class with:
# - `balance` (float)
# - `account_holder` (string)

# Add methods to
# - `deposit(amount)`: This method should increase the balance by the amount deposited.
# - `withdraw(amount)`: This method should decrease the balance by the withdrawal amount, but only if the balance is enough.
# - `get_balance()`: This method should return the current balance.

# Objective: This Task is designed to practice working with methods that modify 
# the state of an object and ensure the balance is correctly updated.

class Account():
    def __init__(self, balance, account_holder):
        self.balance = balance
        self.account_holder = account_holder
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
    def get_balance(self):
        return self.balance

acc = Account(1000, 'John')
print(acc.deposit(200))
print(acc.withdraw(500))
print(acc.get_balance())

#  7. Task: Inheritance - Create `Animal` and `Cat` Classes
# Create a `Animal` class with:
# - `name` (string)
# - `species` (string)
# Add a method `make_sound()` that returns a generic animal sound (e.g., `"Animal makes a sound"`).

# Create a `Cat` class that inherits from `Animal`. In the `Cat` class:
# - Override the `make_sound()` method to return `"Meow!"`.
# - Add a `purr()` method that returns `"Purr..."`.
# class Animal():
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def make_sound(self):
#         return "Animal makes a sound"
    
class Animal:
    def __init__(self, name, species):
        self.name = name     
        self.species = species  
    def make_sound(self):
        return "Animal makes a sound"
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")
    def make_sound(self):
        return f"{super().make_sound()} Meow!"
    def purr(self):
        return "Purr..."

animal = Animal("Akobir", "Unknown")
cat = Cat("Whiskers")

print(animal.make_sound()) 
print(cat.make_sound())   
print(cat.purr())     

#  8. Task: Create a `Student` Class
# Create a `Student` class with:
# - `name` (string)
# - `age` (integer)
# - `grades` (list of integers)
# Add methods to
# - `add_grade(grade)`: Adds a grade to the `grades` list.
# - `average_grade()`: Returns the average grade of the student.
# - `get_info()`: Returns a string with the student's name, age, and average grade.
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def average_grage(self):
        return sum(self.grades) / len(self.grades)
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Average Grade: {sum(self.grades) / len(self.grades)}"
    
student = Student("Lol", 18)
student.add_grade(90)
student.add_grade(85)
print(student.average_grage())
print(student.get_info())
#  9. Task: Create a `Library` Class
# Create a `Library` class that contains:
# - `name` (string)
# - `books` (list of strings)

# Add methods to
# - `add_book(book)`: Adds a book to the library's list of books.
# - `remove_book(book)`: Removes a book from the library's list.
# - `list_books()`: Prints all books in the library.

class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    def list_books(self):
        return f"books: {self.books}"

library = Library("Humo")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
print(library.list_books())
library.remove_book("1984")
print(library.list_books())
#  10. Task: Create a `Bank` Class with Multiple Accounts
# Create a `Bank` class with:
# - `bank_name` (string)
# - `accounts` (a list to store instances of `Account`)
# Add methods to
# - `create_account(account_holder)`: Creates a new account and adds it to the list of accounts.
# - `get_account(account_holder)`: Returns the account for a specific holder if it exists.
# - `transfer_funds(from_account, to_account, amount)`: Transfers a specific amount from one account to another, if funds are available.

class Bank:
    def __init__(self, bank_name, accounts):
        self.bank_name = bank_name
        self.accounts = accounts

    def create_account(self, account_holder):
        account = Account(0, account_holder)
        self.accounts.append(account)

    def get_account(self, account_holder):
        for account in self.accounts:
            if account.account_holder == account_holder:
                return account
            else:
                return "It's not your account"


    def transfer_funds(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            return "Transfer successful"
        else:
            return "Funds are not available"



bank = Bank("Jasur", [])
bank.create_account('Jasur')
account1 = bank.get_account('Jasur')
print(bank.transfer_funds(account1, account1, 500))