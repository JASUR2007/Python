# Task 1: Library Management System
# Create a LibraryItem base class with:

# Attributes:
# title (string)
# author (string)
# publication_year (int)
# Methods:
# display_info(): Prints the item's details.
# Create subclasses for Book and Magazine:

# Book:
# Additional attribute: genre (string)
# Override display_info() to include genre.
# Magazine:
# Additional attribute: issue_number (int)
# Override display_info() to include issue number.
# Objective: Practice creating subclasses and overriding methods.

# Task 2: Vehicle Rental System
# Create a Vehicle base class with:

# Attributes:
# make (string)
# model (string)
# rental_rate (float)
# Methods:
# display_vehicle_info(): Prints the vehicle details.
# Create subclasses for Car and Motorcycle:

# Car:
# Additional attribute: num_seats (int)
# Override display_vehicle_info() to include the number of seats.
# Motorcycle:
# Additional attribute: engine_capacity (cc, int)
# Override display_vehicle_info() to include engine capacity.
# Add a RentalService class with:

# Attributes:
# vehicles (list of Vehicle objects)
# Methods:
# add_vehicle(vehicle): Adds a vehicle to the list.
# get_all_vehicle_info(): Prints details of all vehicles.
# Objective: Practice inheritance, composition, and method overriding.

class Vehicle:
    def __init__(self, make:str, model:str, rental_rate:float):
        self.make = make
        self.model = model
        self.rental_rate = rental_rate

    def display_vehicle_info(self):
        print(f"make: {self.make}, model: {self.model}, rental_rate: {self.rental_rate}")

class Car(Vehicle):
    def __init__(self, make, model, rental_rate, num_seats):
        super().__init__(make, model, rental_rate)
        self.num_seats = num_seats

    def display_vehicle_info(self):
        print(f"{super().display_vehicle_info()}, num_seats:{self.num_seats}")

car = Car()
# Task 3: Employee Hierarchy
# Create an Employee base class with:

# Attributes:
# name (string)
# salary (float)
# Methods:
# display_info(): Prints employee name and salary.
# Create subclasses for Manager and Developer:

# Manager:
# Additional attribute: department (string)
# Override display_info() to include department.
# Developer:
# Additional attribute: programming_languages (list of strings)
# Override display_info() to include programming languages.
# Create an EmployeeSystem class with:

# Attributes:
# employees (list of Employee objects)
# Methods:
# add_employee(employee): Adds an employee to the system.
# get_all_employees_info(): Prints details of all employees.
# Objective: Understand hierarchical relationships in classes and how to manage collections of subclass objects.

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"name: {self.name}, salary: {self.salary}")
class Manager(Employee):
    def __init__(self, department, name, salary):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.programming_language = []
    def display_info(self):
        print(f"{super().display_info()}, {self.programming_language}")
class EmployeeSystem:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
# Task 4: Animal Kingdom Simulation
# Create an Animal base class with:

# Attributes:
# name (string)
# age (int)
# Methods:
# make_sound(): Prints a generic animal sound.
# Create subclasses for Dog and Cat:

# Dog:
# Additional attribute: breed (string)
# Override make_sound() to print "Woof!"
# Cat:
# Additional attribute: color (string)
# Override make_sound() to print "Meow!"
# Add a Zoo class with:

# Attributes:
# animals (list of Animal objects)
# Methods:
# add_animal(animal): Adds an animal to the zoo.
# make_all_sounds(): Calls make_sound() for every animal in the zoo.
# Objective: Practice method overriding and polymorphism.

# Task 5: Online Course Platform
# Create a Course base class with:

# Attributes:
# title (string)
# instructor (string)
# Methods:
# get_description(): Prints course title and instructor.
# Create subclasses for ProgrammingCourse and MathCourse:

# ProgrammingCourse:
# Additional attribute: languages (list of programming languages)
# Override get_description() to include languages.
# MathCourse:
# Additional attribute: difficulty_level (string)
# Override get_description() to include difficulty level.
# Add a CoursePlatform class with:

# Attributes:
# courses (list of Course objects)
# Methods:
# add_course(course): Adds a course to the platform.
# list_all_courses(): Prints details of all courses.
# Objective: Train students to work with inheritance and manage collections of objects.