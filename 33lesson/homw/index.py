# Library Book System
# Create a Book class with attributes like title, author, and publication year. Include a method to display book details.
# Create a Library class that can add and remove books, and display all available books.
# Book class to store information about a book
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(f"{book.display_details()} !")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_books()
library.remove_book("The Great Gatsby")
library.display_books()

    

# Student Grades Tracker
# Create a Student class with attributes for name, age, and a list of grades. Include methods to add grades, calculate the average grade, and display student details.

class Student:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self, grade: int):
        self.grades.append(grade)
    
    def average_grade(self):
        if not self.grades:
            return 0
        average = sum(self.grades) / len(self.grades)
        return average
    
    def display_details(self):
        average = self.average_grade()
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")
        print("-" * 30)

student1 = Student("Akobir", 17)
student2 = Student("Jack", 22)

student1.add_grades(30)
student1.add_grades(33)
student1.add_grades(71)

student2.add_grades(71)
student2.add_grades(90)


student1.display_details()
student2.display_details()

# Car Rental System
# Create a Car class with attributes like make, model, and availability status. Include methods to rent a car (which changes its status to unavailable) and return it (making it available again). You can also add a rental price per day attribute and calculate the total rental cost.
class Car:
    def __init__(self,make, model, availability):
        self.make = make
        self.model = model 
        self.availability = availability
    
# ATM System
# Design an ATM class with a balance attribute. It should have methods for checking balance, depositing money, and withdrawing money, ensuring the balance doesn't go below zero.

class ATM:
    def __init__(self, balance):
        self.balance = balance
    
    def check_balance(self):
        print(f"Current Balance: ${self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

atm = ATM(1000)

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: $"))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: $"))
        atm.withdraw(amount)
    elif choice == "4":
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")


# Inventory Management
# Create an Item class with attributes for name, quantity, and price. Implement methods to update the quantity when items are added or sold and calculate the total value of the items in inventory.

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Updated quantity of {self.name}: {self.quantity}")
    
    def calculate_total_value(self):
        return self.quantity * self.price

item1 = Item("Laptop", 10, 800)

while True:
    print("\nInventory Menu:")
    print("1. View Total Value of Items")
    print("2. Add Items")
    print("3. Sell Items")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    if choice == "1":
        print(f"Total value of {item1.name}: ${item1.calculate_total_value()}")
    elif choice == "2":
        amount = int(input("Enter the number of items to add: "))
        item1.update_quantity(amount)
    elif choice == "3":
        amount = int(input("Enter the number of items to sell: "))
        item1.update_quantity(-amount)
    elif choice == "4":
        print("Exiting Inventory System.")
        break
    else:
        print("Invalid choice. Please try again.")


# Employee Management System
# Design an Employee class with attributes for name, job title, and salary. Include methods for giving a raise and displaying employee details.

class Employee:
    def __init__(self, name, title, job, salary):
        self.name = name 
        self.title = title
        self.job = job
        self.salary = salary

    def raise_salary(self, money):
        self.salary += money
    
    def details(self):
        return f"Name: {self.name},\nTitle: {self.title},\nJob: {self.job},\nSalary: {self.salary} "
    
employee = Employee('Rock', "About him", 'developer', 10)
employee.raise_salary(40)
employee.raise_salary(10)
print(employee.details())

# Shopping Cart
# Create a Product class with attributes for name, price, and quantity. Then create a ShoppingCart class that can add products, remove products, and calculate the total price of items in the cart.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"{self.name} - ${self.price:.2f} (Quantity: {self.quantity})"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product_name):
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                print(f"{product_name} has been removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def calculate_total(self):
        total_price = sum(product.price * product.quantity for product in self.cart)
        return total_price

    def display_cart(self):
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Items in your cart:")
            for product in self.cart:
                print(product)
            print(f"Total price: ${self.calculate_total():.2f}")

product1 = Product("Laptop", 999.99, 1)
shopping_cart = ShoppingCart()
shopping_cart.add_product(product1)
shopping_cart.display_cart()
shopping_cart.remove_product("Headphones")
shopping_cart.display_cart()
total_price = shopping_cart.calculate_total()
print(f"Total price after removal: ${total_price:.2f}")

# Ticket Booking System
# Create a MovieTicket class with attributes for movie title, showtime, and price. Include a method to print the ticket details. Then, create a Booking class that manages the number of tickets available and handles bookings (ensuring no overbooking).

class MovieTicket:
    def __init__(self, title, showtime, price):
        self.title = title
        self.showtime = showtime
        self.price = price
    
    def print_ticket_details(self):
        print(f"Movie Title: {self.title}")
        print(f"Showtime: {self.showtime}")
        print(f"Price: ${self.price:.2f}")
        print("-" * 30)

class Booking:
    def __init__(self, movie_ticket, total_tickets):
        self.movie_ticket = movie_ticket
        self.total_tickets = total_tickets
        self.booked_tickets = 0

    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Please select a positive number of tickets.")
        elif self.booked_tickets + number_of_tickets > self.total_tickets:
            print("Sorry, not enough tickets available.")
        else:
            self.booked_tickets += number_of_tickets
            remaining_tickets = self.total_tickets - self.booked_tickets
            print(f"Successfully booked {number_of_tickets} tickets!")
            print(f"Remaining tickets: {remaining_tickets}")
    
    def cancel_booking(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Please select a positive number of tickets to cancel.")
        elif self.booked_tickets - number_of_tickets < 0:
            print("You cannot cancel more tickets than you have booked.")
        else:
            self.booked_tickets -= number_of_tickets
            remaining_tickets = self.total_tickets - self.booked_tickets
            print(f"Successfully canceled {number_of_tickets} tickets!")
            print(f"Remaining tickets: {remaining_tickets}")
    
    def show_available_tickets(self):
        remaining_tickets = self.total_tickets - self.booked_tickets
        print(f"Available tickets: {remaining_tickets}")


movie_ticket = MovieTicket("Avengers: Endgame", "7:00 PM", 15.99)
booking_system = Booking(movie_ticket, 100)

while True:
    print("\n--- Ticket Booking System ---")
    print("1. View Movie Details")
    print("2. Book Tickets")
    print("3. Cancel Booking")
    print("4. Show Available Tickets")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        movie_ticket.print_ticket_details()
    
    elif choice == "2":
        booking_system.show_available_tickets()
        try:
            number_of_tickets = int(input("Enter the number of tickets you want to book: "))
            booking_system.book_ticket(number_of_tickets)
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "3":
        try:
            number_of_tickets = int(input("Enter the number of tickets you want to cancel: "))
            booking_system.cancel_booking(number_of_tickets)
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "4":
        booking_system.show_available_tickets()
    
    elif choice == "5":
        print("Exiting the system...")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")


# Bank Loan System
# Create a Loan class with attributes for loan amount, interest rate, and loan duration. Include methods to calculate the total repayment amount, interest, and monthly payment.
class Loan:
    def __init__(self, loan_amount, interest_rate, loan):
        self.loan_amount = loan_amount 
        self.interest_rate = interest_rate  
        self.loan = loan  

    def calculate_interest(self):
        total_interest = (self.loan_amount * self.interest_rate * self.loan) / 100
        return total_interest

    def calculate_total_repayment(self):
        total_interest = self.calculate_interest()
        total_repayment = self.loan_amount + total_interest
        return total_repayment

    def calculate_monthly_payment(self):
        total_repayment = self.calculate_total_repayment()
        months = self.loan * 12  
        monthly_payment = total_repayment / months
        return monthly_payment

    def loan_details(self):
        total_interest = self.calculate_interest()
        total_repayment = self.calculate_total_repayment()
        monthly_payment = self.calculate_monthly_payment()

        return (f"Loan Amount: ${self.loan_amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%\n"
                f"Loan Duration: {self.loan} years\n"
                f"Total Interest: ${total_interest:.2f}\n"
                f"Total Repayment Amount: ${total_repayment:.2f}\n"
                f"Monthly Payment: ${monthly_payment:.2f}")

loan = Loan(10000, 5, 10)  
print(loan.loan_details())

# Room Reservation System
# Design a Room class with attributes like room number, type (single/double), and price per night. Create a Reservation class that books rooms and calculates the total cost for the reservation.
# Room Reservation System

# Room Reservation System

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number  
        self.room_type = room_type  
        self.price = price

class Reservation:
    def __init__(self):
        self.reservations = []  

    def book_room(self, room, nights):
        total_cost = room.price * nights
        self.reservations.append({"room": room, "nights": nights, "total_cost": total_cost})
        print(f"Room {room.room_number} booked for {nights} nights. Total cost: ${total_cost:.2f}")

    def calculate_total_cost(self):
        total_cost = sum(reservation['total_cost'] for reservation in self.reservations)
        return total_cost

    def display_reservations(self):
        if not self.reservations:
            print("No reservations made.")
        else:
            print("Reservations:")
            for reservation in self.reservations:
                room = reservation["room"]
                nights = reservation["nights"]
                total_cost = reservation["total_cost"]
                print(f"Room {room.room_number} ({room.room_type.capitalize()}), {nights} nights, Total Cost: ${total_cost:.2f}")
            print(f"All Reservations: ${self.calculate_total_cost():.2f}")

room1 = Room(101, "single", 100)  
reservation_system = Reservation()
reservation_system.book_room(room1, 3)  
reservation_system.display_reservations()
