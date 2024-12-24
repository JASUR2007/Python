# 4. Public and Private: Temperature Converter
# Task: Create a class Temperature with:
# Public variables celsius and fahrenheit.
# Methods to:
# Convert Celsius to Fahrenheit and display the result.
# Convert Fahrenheit to Celsius and display the result.
# Ensure direct modification of variables affects the conversions.

class Temperature:
    def __init__(self, celsius=0, fahrenheit=32):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def celsius_to_fahrenheit(self):
        self.fahrenheit = (self.celsius * 9/5) + 32
        print(f"{self.celsius}°C is equal to {self.fahrenheit}°F")

    def fahrenheit_to_celsius(self):
        self.celsius = (self.fahrenheit - 32) * 5/9
        print(f"{self.fahrenheit}°F is equal to {self.celsius:.2f}°C")

temperature = Temperature(celsius=25)
temperature.celsius_to_fahrenheit()  
temperature.fahrenheit_to_celsius()  

temperature.celsius = 30
temperature.celsius_to_fahrenheit()  



# 5. Private Variable: Gym Membership
# Task: Create a class GymMembership with a private variable __member_id and public variables name and age. Add methods to:
# Set and display the member ID.
# Ensure the age is at least 18 during initialization or modification.

class GymMembership:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__member_id = None 

        if self.age < 18:
            print("At least 18 to register for a gym membership.")
            self.age = 18

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def display_member_id(self):
        print(f"Member ID: {self.__member_id}")

    def display_member_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


gym_member = GymMembership("Drake wan dyke", 25)
gym_member.set_member_id("M12345")
gym_member.display_member_id()
gym_member.display_member_info()

gym_member_underage = GymMembership("Jane Doe", 16)



# 6. Public Variables: Circle Properties
# Task: Create a class Circle with public variables radius and color. Add a method to calculate and display the circle’s area. Allow the radius to be directly modified and observe the effect.



class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        print(f"Radius {self.radius} and color {self.color}, an area of {area:.2f}")

circle = Circle(5, "red")
circle.calculate_area()

circle.radius = 10
circle.calculate_area()


# 7. Encapsulation: Bank Interest Rate
# Task: Create a class BankAccount with:
# Public variable account_number.
# A private variable __interest_rate.
# Add methods to:
# Set a valid interest rate (0-100).
# Calculate and display interest based on a given balance.
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.__rate = 0

    def set_rate(self, rate):
        if 0 <= rate <= 100:
            self.__rate = rate
        else:
            print("Invalid interest rate. It should be between 0 and 100.")

    def calculate_rate(self, balance):
        interest = (balance * self.__rate) / 100
        return interest

    def display_interest(self, balance):
        interest = self.calculate_rate(balance)
        print(f"Account Number: {self.account_number}")
        print(f"Interest Rate: {self.__rate}%")
        print(f"Balance: ${balance}")
        print(f"Calculated Interest: ${interest:.2f}")

account = BankAccount("123456789")
account.set_rate(5)
account.display_interest(1000)
account.set_rate(120) 

# 8. Public and Private: Inventory Stock
# Task: Create a class Product with:
# Public variables name and price.
# A private variable __stock.
# Add methods to:
# Increase or decrease the stock.
# Prevent stock from going below zero.

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def increase_stock(self, quantity):
        if quantity > 0:
            self.__stock += quantity
        else:
            print("Quantity to increase must be greater than zero.")

    def decrease_stock(self, quantity):
        if quantity > 0:
            if self.__stock >= quantity:
                self.__stock -= quantity
            else:
                print("Not enough stock available.")
        else:
            print("Quantity to decrease must be greater than zero.")

    def display_product(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: ${self.price}")
        print(f"Stock Available: {self.__stock}")

product = Product("Laptop", 1000, 50)

product.display_product()
product.increase_stock(20)
product.display_product()
product.decrease_stock(30)
product.display_product()
product.decrease_stock(100)  

# 9. Encapsulation with Validation: Marks Calculator
# Task: Create a class Student with:
# Public variables name and roll_number.
# Private variables __math_marks, __science_marks, and __english_marks.
# Add methods to:
# Set marks for each subject (validate: 0-100).
# Calculate and display the total and average marks.

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.__math_marks = 0
        self.__science_marks = 0
        self.__english_marks = 0

    def set_math_marks(self, marks):
        if 0 <= marks <= 100:
            self.__math_marks = marks
        else:
            print("Invalid marks for Math. It must be between 0 and 100.")

    def set_science_marks(self, marks):
        if 0 <= marks <= 100:
            self.__science_marks = marks
        else:
            print("Invalid marks for Science. It must be between 0 and 100.")

    def set_english_marks(self, marks):
        if 0 <= marks <= 100:
            self.__english_marks = marks
        else:
            print("Invalid marks for English. It must be between 0 and 100.")

    def calculate_total(self):
        return self.__math_marks + self.__science_marks + self.__english_marks

    def calculate_average(self):
        total = self.calculate_total()
        return total / 3

    def display_marks(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Math Marks: {self.__math_marks}")
        print(f"Science Marks: {self.__science_marks}")
        print(f"English Marks: {self.__english_marks}")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average Marks: {self.calculate_average():.2f}")


# Example usage
student = Student("John Doe", "12345")
student.set_math_marks(85)
student.set_science_marks(90)
student.set_english_marks(78)
student.display_marks()

# 10. Public Variables: Laptop Specifications
# Task: Create a class Laptop with public variables brand, model, and price. Write methods to:
# Display laptop details.
# Allow direct modifications of variables and observe the results.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

laptop = Laptop("Asus", "Rog strix", 1200)
print("Initial Laptop Details:")
laptop.display_details()

laptop.brand = "Apple"
laptop.model = "MacBook Pro"
laptop.price = 1500
print("\nModified Laptop Details:")
laptop.display_details()
