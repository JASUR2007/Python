# 1. Task: Create a ProjectManagement System
# Create a Project class with:
# •  Attributes:
# o  name (string)
# o  deadline (datetime object)
# o  tasks (list of Task objects)
# •  Methods:
# o  add_task(task): Adds a Task object to the project.
# o  remove_task(task_name): Removes a task by its name.
# o  get_progress(): Returns the percentage of completed tasks.
# Create a Task class with:
# •  Attributes:
# o  name (string)
# o  status (boolean, default False for incomplete)
# •  Methods:
# o  mark_complete(): Marks the task as complete.
# Objective: Practice class relationships (composition) and calculating progress dynamically.
# """
# #
# #
class Task:
    def init(self, name):
        self.name = name
        self.status = False

    def mark_complete(self):
        self.status = True



class Project:
    def init(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            self.tasks.remove(task)
            break

    def get_progress(self):
        completed_tasks = 0
        for task in self.tasks:
            if task.status:
                completed_tasks += 1
        total_tasks = len(self.tasks)
        progress = (completed_tasks / total_tasks) * 100
        return progress



project = Project("Qadam", "24.10")
task1 = Task("1")
task2 = Task("2")
task3 = Task("3")

project.add_task(task1)
project.add_task(task2)
project.add_task(task3)

task1.mark_complete()
print(project.get_progress())




# 2. Task: Create a BankSystem with Multiple Account Types
# Create a BankAccount class with:
# •  Attributes:
# o  account_number (string)
# o  balance (float)
# o  account_type (string, choices: "Savings", "Current")
# •  Methods:
# o  deposit(amount): Adds the amount to the balance.
# o  withdraw(amount): Withdraws the amount if the balance is sufficient.
# o  apply_interest(): Applies interest (different rates for savings and current accounts).
# Objective: Implement conditional logic based on the account type.
# """

class BankAccount:
    def init(self, account_number: str, balance: float, account_type: str):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def apply_interest(self):
        if self.account_type == "Savings":
            self.balance *= 1
        elif self.account_type == "Current":
            self.balance *= 2



savings_account = BankAccount("938724269", 1000, "Savings")
savings_account.deposit(500)
savings_account.apply_interest()
print(savings_account.balance)
# 3. Task: Create a Chess Game
# Create a ChessPiece class with:
# •  Attributes: 
# o  name (string, e.g., "Pawn", "Queen", etc.)
# o  position (tuple, e.g., (1, 1) for a1 on a chessboard)
# •  Methods: 
# o  move(new_position): Updates the position, but only if the move is valid for the piece.
# Create a ChessGame class with:
# •  Attributes: 
# o  pieces (list of ChessPiece objects)
# •  Methods: 
# o  add_piece(piece): Adds a new piece to the board.
# o  is_checkmate(): Returns True if the king is in checkmate (simplified logic).
# Objective: Implement rules and constraints for moving chess pieces.
# ________________________________________
class Chess:
    def ChessPiece(self, name: str, position: tuple):
        self.name = name
        self.position = position
    def move(new_position):
        return 1
class ChessGame:
    def __init__():
        pieces = []
    def add_piece(piece):
        return piece
    def is_checkmate():
        return True


class Student:
    def __init__(self, name: str, grades: dict):
        self.name = name
        self.grades = grades
    def add_grade(self, subject: str, grade: int):
        self.grades[subject] = grade
        print(f"Added grade {grade} for subject {subject}.")
    def calculate_gpa(self):
        grades_list = list(self.grades.values()) 
        if grades_list:
            gpa = sum(grades_list) / len(grades_list)
            return f"The average grade (GPA) for {self.name}: {gpa}"
        else:
            return f"No grades available for {self.name}."

student1 = Student("Jas", {"math": 5, "chemistry": 4, "physics": 3})
subject = input("Enter the name of the subject: ")
grade = int(input("Enter a grade: "))
student1.add_grade(subject, grade)
print(student1.calculate_gpa())
# 5. Task: Create a Marketplace System
# Create a Product class with:
# •  Attributes: 
# o  name (string)
# o  price (float)
# o  stock (integer)
# Create a Seller class with:
# •  Attributes: 
# o  name (string)
# o  products (list of Product objects)
# •  Methods: 
# o  add_product(product): Adds a product to the seller’s inventory.
# o  remove_product(product_name): Removes a product by name.
# Create a Marketplace class with:
# •  Attributes: 
# o  sellers (list of Seller objects)
# •  Methods: 
# o  list_all_products(): Lists all products available in the marketplace.
# o  purchase_product(seller_name, product_name, quantity): Deducts the stock of the product and simulates a purchase.
# Objective: Model a marketplace system using relationships and transactions between classes.
# ________________________________________
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def dock(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.stock}"

class Seller:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        return product
    def remove_product(self, product):
        self.products.remove(product)
        return product
    def show(self):
        return self.products
class Marketplace(Seller):
    def __init__(self):
        super().__init__(Seller)
        self.sellers = []
    def list_all_products(self):
        return self.sellers
    def purchase_product(self, product_name, quantity):
        self.sellers.append(product_name)
        return f"Products:{product_name},  quantity: {quantity}"

product = Product('tomato',4.3, True)
seller = Seller('Akobir')
market = Marketplace()

print(product.dock())
print(market.purchase_product('tomato', 5))
print(seller.add_product('tomato'))
print(seller.add_product('orange'))
print(seller.remove_product('tomato'))
print(seller.show())
print(market.list_all_products())

# 6. Task: Create product_nameHospitalManagement System
# Create a Patient class with:
# •  Attributes: 
# o  name (string)
# o  age (integer)
# o  medical_history (list of strings)
# •  Methods: 
# o  add_history(record): Adds a medical history record.
# Create a Doctor class with:
# •  Attributes: 
# o  name (string)
# o  specialization (string)
# o  patients (list of Patient objects)
# •  Methods: 
# o  assign_patient(patient): Adds a patient to the doctor’s list.
# o  get_patients(): Returns a list of the doctor’s patients.
# Objective: Implement many-to-many relationships between doctors and patients.
# ________________________________________

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []
        self.doctors = set()
    def add_history(self, record):
        self.medical_history.append(record)
        return record
    def assign_doctor(self, doctor):
        self.doctors.add(doctor)

    def __repr__(self):
        return f"Patient(name={self.name}, age={self.age})"


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = set()
    def assign_patient(self, patient):
        """Assign a patient to the doctor and ensure bidirectional assignment."""
        self.patients.add(patient)
        patient.assign_doctor(self)
    def get_patients(self):
        """Return a list of all patients."""
        return list(self.patients)
    def __repr__(self):
        return f"Doctor(name={self.name}, specialization={self.specialization})"


patient1 = Patient("Rock", 20)
patient2 = Patient("Sam", 30)

doctor1 = Doctor("Akobir", "Cardiology")
doctor2 = Doctor("Albert", "Neurology")

patient1.add_history("20.05.2024: Check-up")
patient2.add_history("21.05.2024: Headache treatment")

doctor1.assign_patient(patient1)
doctor1.assign_patient(patient2)

doctor2.assign_patient(patient1) 

print(f"Doctor {doctor1.name}'s patients: {doctor1.get_patients()}")
print(f"Doctor {doctor2.name}'s patients: {doctor2.get_patients()}")
print(f"Patient {patient1.name}'s doctors: {list(patient1.doctors)}")
print(f"Patient {patient2.name}'s doctors: {list(patient2.doctors)}")

# 7. Task: Create a LibrarySystem with Borrowing Rules
# Create a Book class with:
# •  Attributes: 
# o  title (string)
# o  author (string)
# o  available_copies (integer)
# Create a Library class with:
# •  Attributes: 
# o  name (string)
# o  books (list of Book objects)
# o  borrowed_books (dictionary mapping user names to borrowed book titles)
# •  Methods: 
# o  add_book(book): Adds a new book to the library.
# o  borrow_book(book_title, user_name): Reduces the available copies and records the borrow.
# o  return_book(book_title, user_name): Increases the available copies and removes the borrow record.
# Objective: Model a borrowing system and manage book availability dynamically.
# ___________________

class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', available_copies={self.available_copies})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.borrowed_books = {}
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, book_title, user_name):
        if user_name in self.borrowed_books:
            return f"{user_name} a book. Please return it before borrowing a new one."
        for book in self.books:
            if book.title == book_title:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    self.borrowed_books[user_name] = book_title
                    return f"{user_name} borrowed '{book_title}'."
                else:
                    return f"Sorry, '{book_title}' is currently unavailable."
        return f"Book '{book_title}' not found in the library."
    def return_book(self, book_title, user_name):
        if user_name not in self.borrowed_books:
            return f"{user_name} did not borrow any book."
        if self.borrowed_books[user_name] == book_title:
            for book in self.books:
                if book.title == book_title:
                    book.available_copies += 1
                    del self.borrowed_books[user_name]
                    return f"{user_name} returned '{book_title}'."
        
        return f"{user_name} did not borrow '{book_title}'."
    def get_available_books(self):
        return [book for book in self.books if book.available_copies > 0]


lib = Library('My Library')

book1 = Book('1984', 'George Orwell', 5)
book2 = Book('To Kill Akobir', 'Omadbek', 3)
lib.add_book(book1)
lib.add_book(book2)

print(lib.borrow_book('1984', 'Rain')) 
print(lib.borrow_book('1984', 'Smoke')) 
print(lib.borrow_book('To Kill a Mockingbird', 'Bob'))
print(lib.return_book('1984', 'Smoke')) 
print(lib.return_book('To Kill a Mockingbird', 'Bob')) 
print(lib.get_available_books()) 

# 8. Task: Create an EventManagement System
# Create an Event class with:
# •  Attributes: 
# o  name (string)
# o  date (datetime object)
# o  attendees (list of strings)
# •  Methods: 
# o  add_attendee(name): Adds an attendee to the event.
# o  list_attendees(): Lists all attendees.
# Create an EventManager class with:
# •  Attributes: 
# o  events (list of Event objects)
# •  Methods: 
# o  schedule_event(event): Adds an event to the schedule.
# o  cancel_event(event_name): Removes an event from the schedule.
# Objective: Work with datetime and implement event scheduling.
# Event Class
class Event:
    def __init__(self, name, date):
        self.name = name  
        self.date = date  
        self.attendees = []     

    def add_attendee(self, name):
        self.attendees.append(name)
    
    def list_attendees(self):
        if self.attendees:
            print(f"Attendees for {self.name}:")
            for attendee in self.attendees:
                print(attendee)
        else:
            print(f"No attendees for {self.name} yet.")
    
    def get_event_details(self):
        return f"Event: {self.name}, Date: {self.date}"

class EventManager:
    def __init__(self):
        self.events = []  
    
    def schedule_event(self, event):
        self.events.append(event)
        print(f"Event '{event.name}' scheduled for {event.date}")
    
    def cancel_event(self, event_name):
        event_to_cancel = None
        for event in self.events:
            if event.name == event_name:
                event_to_cancel = event
                break
        if event_to_cancel:
            self.events.remove(event_to_cancel)
            print(f"Event '{event_name}' has been cancelled")
        else:
            print(f"Event '{event_name}' not found in schedule")
    
    def list_events(self):
        if not self.events:
            print("No events")
        else:
            for event in self.events:
                print(event.get_event_details())


manager = EventManager()

event1 = Event("Python Workshop", "2024-12-05 10:00:00")
event2 = Event("Tech Conference", "2024-12-12 09:00:00")

manager.schedule_event(event1)
manager.schedule_event(event2)

event1.add_attendee("Albert")
event1.add_attendee("Jasur")
event2.add_attendee("Akobir")

print("Events:")
manager.list_events()

print("Attendees:")
event1.list_attendees()
event2.list_attendees()

print("\nCancelling the 'Tech Conference' event:")
manager.cancel_event("Tech Conference")

print("\nScheduled Events after cancellation:")
manager.list_events()

# 9. Task: Create a TravelAgency System
# Create a Destination class with:
# •  Attributes: 
# o  name (string)
# o  cost_per_day (float)
# Create a Trip class with:
# •  Attributes: 
# o  destination (an instance of Destination)
# o  days (integer)
# o  traveler (string)
# •  Methods: 
# o  calculate_cost(): Returns the total cost of the trip (cost per day * days).
# Objective: Create a system with interdependent classes and cost calculations.

class Destination:
    def __init__(self, name, cost_per_day):
        self.name = name
        self.cost_per_day = cost_per_day

    def __str__(self):
        return f"dest: {self.name}, per day: ${self.cost_per_day}"

class Trip:
    def __init__(self, destination, days, traveler):
        self.destination = destination
        self.days = days
        self.traveler = traveler

    def calculate_cost(self):
        return self.destination.cost_per_day * self.days

    def __str__(self):
        return f"traveler: {self.traveler}, trip: {self.destination.name}, days: {self.days}, cost: ${self.calculate_cost()}"

tashkent = Destination("Tashkent", 150.0)
moscow = Destination("Moscow", 200.0)

toTashkent = Trip(tashkent, 5, "Albert")
toMoscow = Trip(moscow, 7, "Akobir")

print(toTashkent)
print(toMoscow)

print(f"Cost of first trip: ${toTashkent.calculate_cost()}")
print(f"Cost of second trip: ${toMoscow.calculate_cost()}")




# 10. Task: Create a WeatherForecast System
# Create a WeatherDay class with:
# •  Attributes: 
# o  date (datetime object)
# o  temperature (float)
# o  condition (string, e.g., "Sunny", "Rainy")
# •  Methods: 
# o  is_freezing(): Returns True if the temperature is below 0.
# Create a Forecast class with:
# •  Attributes: 
# o  location (string)
# o  days (list of WeatherDay objects)
# •  Methods: 
# o  add_day(weather_day): Adds a WeatherDay object to the forecast.
# o  get_average_temperature(): Calculates the average temperature over all days.
# Objective: Work with datetime, lists, and numeric data.

class WeatherDay:
    def __init__(self, date, temperature, condition):
        self.date = date
        self.temperature = temperature
        self.condition = condition
    
    def is_freezing(self):
        if self.temperature < 0:
            return True
        else:
            return False

class Forecast:
    def __init__(self, location):
        self.location = location
        self.days = []
    
    def add_day(self, weather_day):
        self.days.append(weather_day)
    
    def get_average_temperature(self):
        if len(self.days) == 0:
            return 0
        total_temperature = 0
        for day in self.days:
            total_temperature += day.temperature
        return total_temperature / len(self.days)

weather_day1 = WeatherDay("2024-11-25", -5.0, "Snowy")
weather_day2 = WeatherDay("2024-11-26", 12.0, "Sunny")
weather_day3 = WeatherDay("2024-11-27", 8.0, "Cloudy")

forecast = Forecast("Tashkent")

forecast.add_day(weather_day1)
forecast.add_day(weather_day2)
forecast.add_day(weather_day3)

print(f"Weather forecast for {forecast.location}:")
for day in forecast.days:
    print(f"Date: {day.date}, Condition: {day.condition}, Temperature: {day.temperature}°C, Freezing: {day.is_freezing()}")

average_temp = forecast.get_average_temperature()
print(f"\nThe average temperature: {average_temp}°C")

