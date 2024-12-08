# ### 2. Product Class  
# Create a Product class that has private attributes for the product name, price, and quantity.  
# - Implement methods to get and set each attribute.  
# - Add a method to apply a discount to the price (should not allow negative prices or quantities).

# ---
class Product:
    def __init__(self, name, price, quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity
    def get_name(self):
        return f'the name is {self.__name}'
    def get_price(self):
        return f'the price is {self.__price}'
    def get_quantity(self):
        return f'the quantity is {self.__quantity}'
    
    def set_name(self, new_name):
        self.name=new_name
        return f'the name has been changed to {new_name}'
    def set_price(self, new_price):
        self.__price=new_price
        return f'the prcie has been changed to {new_price}'
    def set_quantity(self, new_quantity):
        self.__price=new_quantity
        return f'the quantity has benn changed to {new_quantity}'
    def discount(self, discount_amount):
        if discount_amount>0:
            return f"you have got discount of {discount_amount}% in price {(self.__price)-(discount_amount*self.__price/100)}"
product1=Product('laptop',200, 10 )
print(product1.get_name())
print(product1.get_price())
print(product1.get_quantity())
print(product1.set_name('Iphone'))
print(product1.set_price(50))
print(product1.set_quantity(5))
print(product1.discount(10))
# ### 3. Bank Account  
# Create a BankAccount class with private attributes for account number and balance.  
# - Implement methods to deposit and withdraw money (ensure the balance cannot go below zero).  
# - Create a method to transfer money between two accounts.  
# - Add a method to check the balance.

# ---
class BankAccount:
    def __init__(self, acc_number, balance):
        self.__acc_number = acc_number
        self.__balance = balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            return f'Deposited, new balance is {self.__balance}.'
        else:
            return 'Deposit amount should be positive.'

    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0 and self.__balance >= withdraw_amount:
            self.__balance -= withdraw_amount
            return f'Withdrawn, the current amount of money you have is {self.__balance}.'
        else:
            return 'no enough amount.'

    def transfer(self, target_account, transfer_amount):
        if transfer_amount > 0 and self.__balance >= transfer_amount:
            self.__balance -= transfer_amount
            target_account.__balance += transfer_amount
            return f'Transferred {transfer_amount} to account number {target_account.__acc_number}. Your new balance is {self.__balance}.'
        else:
            return 'no enough amount'

    def check_balance(self):
        return f'Account number {self.__acc_number} has {self.__balance}.'

account1 = BankAccount(122, 5000)
account2 = BankAccount(111, 1000)

print(account1.deposit(50))
print(account1.deposit(-10))
print(account1.withdraw(20))
print(account1.withdraw(800))
print(account1.transfer(account2, 100))
print(account1.transfer(account2, 200))
print(account1.check_balance())
print(account2.check_balance())

# """### 4. Temperature Conversion  
# Create a Temperature class with private attributes for Celsius and Fahrenheit.  
# - Implement methods to get and set the Celsius and Fahrenheit values.  
# - Ensure that setting one temperature automatically updates the other based on conversion (Celsius to Fahrenheit and vice versa).
# """



class Temperature:
    def __init__(self, celsius=0.0):
        self.__celsius = celsius
        self.__fahrenheit = self.__celsius_to_fahrenheit(celsius)

    def __celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def __fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        self.__celsius = value
        self.__fahrenheit = self.__celsius_to_fahrenheit(value)

    def get_fahrenheit(self):
        return self.__fahrenheit

    def set_fahrenheit(self, value):
        self.__fahrenheit = value
        self.__celsius = self.__fahrenheit_to_celsius(value)


temp = Temperature(0)
print(f"{temp.get_celsius()} °C = {temp.get_fahrenheit()} °F")

temp.set_fahrenheit(100)
print(f"{temp.get_fahrenheit()} °F = {temp.get_celsius()} °C")




# """### 5. Student Grades  
# Create a Student class with private attributes for name and a list of grades.  
# - Implement methods to add grades, get the grades, and calculate the average grade.  
# - Ensure that the grades are between 0 and 100.
# """


class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

    def get_grades(self):
        return self.__grades

    def calculate_average_grade(self):
        if len(self.__grades) == 0:
            return 0
        else:
            return sum(self.__grades) / len(self.__grades)

student = Student('Жасур')
student.add_grade(5)
student.add_grade(3)
student.add_grade(3)
print(student.calculate_average_grade())

# """### 6. Employee Class  
# Create an Employee class with private attributes for employee name, salary, and position.  
# - Implement public methods to get and set the name, salary, and position.  
# - Ensure the salary cannot be negative, and the position must be one of the following: "Manager," "Developer," "Intern."
# """


class Employee:
    def __init__(self, name, salary, position):
        self.__name = name
        self.__salary = salary
        self.__position = position

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
        if self.__salary < 0:
            self.__salary = 0
        else:
            print("salary should not be negative")

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if position in ["Manager", "Developer", "Intern"]:
            self.__position = position
        else:
            print("Invalid position. Position must be 'Manager', 'Developer', or 'Intern'.")

employee = Employee('Жасур', '200', 'Employee')
print(employee.get_name())
employee.set_name('Акобир')
print(f"employee: {employee.get_name()}, salary: {employee.get_salary()}, position: {employee.get_position()}")


# ### 7. Car Class  
# Create a Car class with private attributes for make, model, and year.  
# - Implement public methods to get and set the make, model, and year of the car.  
# - Add a method to display the car details in a formatted string.

# ---
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    def setMake(self, make):
        self.__make = make
    def getMake(self):
        return self.__make
    def setModel(self, model):
        self.__model = model
    def getModel(self):
        return self.__model
    def setYear(self, year):
        self.__year = year
    def getYear(self):
        return self.__year
    def details(self):
        return f'Make = {self.__make}\nModel = {self.__model}\nYear = {self.__year}'

car = Car('GM', 'Nexia 3', 2022)
print(car.details())
car.setMake('Fake')
car.setModel('Zaparoj')
car.setYear(2002)
print(car.getMake())
print(car.getModel())
print(car.getYear())

# ### 8. Library Book  
# Create a Book class with private attributes for the book title, author, and publication year.  
# - Implement public methods to get and set these attributes.  
# - Add a method to check if the book is available (boolean) and implement the logic for borrowing and returning the book.

# ---


class Book:
    def __init__(self, title, author, publication_year):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__available = True

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Year: {self.__publication_year}"

    def check_availability(self):
        return self.__available

    def borrow_book(self):
        if self.__available:
            self.__available = False
            return f"You have successfully borrowed '{self.__title}'."
        else:
            return f"Sorry, '{self.__title}' is currently unavailable."

    def return_book(self):
        if not self.__available:
            self.__available = True
            return f"You have successfully returned '{self.__title}'."
        else:
            return f"The book '{self.__title}' was not borrowed !!!"



book = Book("The Maze Runner", "James Dashner", 2012)
book2 = Book("Looking for Alaska", "John Green", 2005)
book3 = Book(" All Quiet on the Western Front", "Erich Maria Remarque", 1928)

print(book.get_details())
print(book.borrow_book())
print(book2.get_details())
print(book2.borrow_book())
print(book3.return_book())

# ### 9. Wallet Class  
# Create a Wallet class with a private attribute for the balance.  
# - Implement methods to add money, remove money, and check the balance.  
# - Ensure that money cannot be withdrawn if there is insufficient balance.

# ---
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        if amount < 0:
            return "Error: Cannot add negative money."
        
        self.__balance += amount
        return f"Added money: ${amount}."

    def get_balance(self):
        return self.__balance

    def remove_balance(self, amount):
        if amount < 0:
            return "Error: Cannot add negative money."
        self.__balance -= amount
        return f"Removed money: ${amount}."
        

            

user_add_money = int(input("Enter an amount of money you want to add: $"))
user_balance = int(input("Enter ur current balance: $"))
user_remove_money = int(input("Enter an amount of money you want to remove: $"))
wallet = Wallet(user_balance)
result = wallet.add_money(user_add_money)
wallet.remove_balance(user_remove_money)
print(result)
print(f"Current balance: ${wallet.get_balance()}")

# ### 10. Circle Class  
# Create a Circle class with a private attribute for the radius.  
# - Implement methods to get and set the radius.  
# - Add a method to calculate and return the area and circumference of the circle.

# ---
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return f"radius: {self.__radius}"
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def area(self):
        return f"area: {3.14 * self.__radius}"
    
    def circumference(self):
        return f"circumference: {2 * 3.14* self.__radius}"
# ### 11. Rectangle Class  
# Create a Rectangle class with private attributes for length and width.  
# - Implement methods to set and get the dimensions of the rectangle.  
# - Add methods to calculate and return the area and perimeter of the rectangle.
# ---
class Rectangle:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width
    
    def set(self, len: int, wid:int):
        self.__length = len
        self.__width = wid

    def get(self):
        return f"length: {self.__length}, width: {self.__width}"
    
    def area(self):
        return f"area: {self.__length * self.__width}"
    
    def perimeter(self):
        return f"perimeter {(self.__length + self.__width) * 2}"
    
rec = Rectangle(6,7)
print(rec.area())
rec.set(3,4)
print(rec.get())
print(rec.perimeter())
print(rec.get())
# ### 12. Account Holder  
# Create an AccountHolder class with private attributes for name, account number, and balance.  
# - Implement methods to get and set each of these attributes.  
# - Add a method to display the account details in a formatted string.

# ---
class AccountHolder:
    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance
    
    def display_account_details(self):
        return f"Account Holder: {self.__name}\nAccount Number: {self.__account_number}\nBalance: ${self.__balance:.2f}"

account = AccountHolder("Albert", "1231231", 13)
print(account.set_account_number(2020))
print(account.display_account_details())

# ### 13. Person with Address  
# Create a Person class that includes a private attribute for the address.  
# - Implement methods to set and get the address.  
# - Ensure that the address is a string containing at least one character.

# ---
class Person:
    def __init__(self, address:str):
        self.__address = address
    def setAddress(self, address):
            self.__address = address
    def getAddress(self):
        if len(self.__address) > 0:
            return self.__address
        else:
            return 'String must contain at least 1 character'

person = Person('chilonzor 12 9 daha 13refschbidjvn')
print(person.getAddress())
person.setAddress('')
print(person.getAddress())

# ### 14. Bookstore Inventory  
# Create an Inventory class to track books in a bookstore.  
# - Implement private attributes for book name, price, and quantity.  
# - Implement methods to update the quantity and price of a book, and get the total inventory value.

class Bookstre:
    def __init__(self, book_name, price, quantity):
        self.__book_name=book_name
        self.__price=price
        self.__quantity=quantity
    def update(self,  price,quantity ):
        self.__price=price
        self.__quantity=quantity
        return f'changed to quantity= {self.__quantity}, price= {self.__price}'
    def get_total(self):
        return f'we have got book {self.__book_name}, price: {self.__price}, quantity: {self.__quantity}'

book1=Bookstre('Harry Potter', 150, 200)
print(book1.get_total())
print(book1.update(250,300))
print(book1.get_total())
