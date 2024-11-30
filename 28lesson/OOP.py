# 11. Task: Create a Course Class
# Create a Course class with:
# •  name (string)
# •  instructor (string)
# •  students (list of strings)
# Add methods to:
# •  add_student(student_name): Adds a student to the course.
# •  remove_student(student_name): Removes a student from the course.
# •  list_students(): Prints all students in the course.
# Objective: Practice working with lists and managing class attributes dynamically.


class Course():
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.students = []
    def add_students(self, student):
        self.students.append(student)
    def remove_student(self, student):
        self.students.remove(student)
    def list_students(self):
        return self.students

course = Course('Aka', 'Sanjar Teacher')

course.add_students('Rocka')
course.add_students('Akobir')
course.remove_student('Akobir')

print(course.list_students())


# 12. Task: Create a Movie Class
# Create a Movie class with:
# •  title (string)
# •  director (string)
# •  year (integer)
# •  rating (float)
# Add methods to:
# •  get_summary(): Returns a string describing the movie, e.g., "Inception, directed by Christopher Nolan, was released in 2010 with a rating of 8.8."
# •  update_rating(new_rating): Updates the movie’s rating.
# Objective: Practice creating and modifying attributes, including handling floating-point data.
# ________________________________________

class Movie():
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
    def get_summary(self):
        return f"{self.title}, directed by {self.director}, was released in {self.year} with a rating of {self.rating}."
    def update_rating(self, new_rating):
        self.rating = new_rating

movie = Movie('Avatar 2', 'Camron', 2023, 8.6)

print(movie.get_summary())
movie.update_rating(5.4)
print(movie.get_summary())
# 13. Task: Create a ShoppingCart Class
# Create a ShoppingCart class with:
# •  items (list of dictionaries with keys name and price)
# Add methods to:
# •  add_item(name, price): Adds an item to the cart.
# •  remove_item(name): Removes an item by name from the cart.
# •  calculate_total(): Returns the total price of all items.
# Objective: Manage a list of dictionaries and perform calculations on the data.
# ________________________________________

class ShoppingCart():
    def __init__(self):
        self.item = {}
    def add_item(self,name,price):
        self.item[name] = price
    def remove_item(self,name):
        self.item.pop(name)
    def calculate_total(self):
        return self.item

shop = ShoppingCart()
shop.add_item('tomato', 3.4)
shop.add_item('cucumber', 2.4)
shop.remove_item('cucumber')
print(shop.calculate_total())

# 14. Task: Create a Game Class
# Create a Game class with:
# •  name (string)
# •  max_players (integer)
# •  players (list of strings)
# Add methods to:
# •  add_player(player_name): Adds a player to the game if the maximum number of players hasn’t been reached.
# •  remove_player(player_name): Removes a player from the game.
# •  start_game(): Prints "Game started!" if there are at least two players.
# Objective: Practice implementing business logic and conditional checks.
# ________________________________________

class Game():
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.players = []
    def add_player(self, player_name):
        if len(self.players) < self.max_players:
            self.players.append(player_name)
        else:
            return 'limited users'
    def remove_player(self, player_name):
        self.players.remove(player_name)
    def start_game(self):
        if (len(self.players) < 3):
            return "Insufficient players"
        else:
            return f"Game: {self.name} started {self.players}, max: {self.max_players} "

game = Game('Mario', 10)
game.add_player('Albert')
game.add_player('Akobir')
game.add_player("Jasur")
game.add_player("Omad")
game.remove_player('Omad')
print(game.start_game())

# 15. Task: Create a House Class
# Create a House class with:
# •  address (string)
# •  rooms (integer)
# •  price (float)
# Add methods to:
# •  describe(): Returns a string describing the house, e.g., "This house at 123 Main St has 4 rooms and costs $250,000."
# •  apply_discount(discount_percentage): Reduces the price by a specified percentage.
# Objective: Work with numeric data and percentages in methods.
# ________________________________________

class House():
    def __init__(self, adress, rooms, price):
        self.adress = adress
        self.rooms = rooms 
        self.price = price
    def describe(self):
        return f'This house at {self.adress} has {self.rooms} rooms and costs ${self.price}.'
    def apply_discount(self, discount_percentage):
        self.price = self.price - (self.price * discount_percentage/100)

house = House('Sergeli 8', 4, 250000)
house.apply_discount(20)
print(house.describe())

# 16. Task: Create a School Class
# Create a School class with:
# •  name (string)
# •  teachers (list of strings)
# •  students (list of strings)
# Add methods to:
# •  add_teacher(teacher_name): Adds a teacher to the school.
# •  add_student(student_name): Adds a student to the school.
# •  list_all(): Prints all teachers and students in the school.
# Objective: Manage multiple lists and implement aggregation logic.
# ________________________________________
class School():
    def __init__(self, name):
        self.name = name
        self.teachers = []  
        self.students = []  

    def add_teacher(self, teacher_name):
        self.teachers.append(teacher_name)

    def add_student(self, student_name):
        self.students.append(student_name)

    def list_all(self):
        print(f"School Name: {self.name}")
        print("Teachers:")
        for teacher in self.teachers:
            print(f"- {teacher}")
        print("Students:")
        for student in self.students:
            print(f"- {student}")

school = School("PDP")

school.add_teacher("Sanjar")
school.add_teacher("Faruh")
school.add_student("Albert")
school.add_student("Jasur")
school.add_student('Akobir')

school.list_all()

# 17. Task: Create a Robot Class
# Create a Robot class with:
# •  name (string)
# •  battery_level (integer, default 100)
# Add methods to:
# •  charge(): Sets the battery level to 100.
# •  work(hours): Reduces the battery level by hours * 10 but not below 0. Print a message when the robot is out of battery.
# Objective: Practice updating and validating numeric attributes.
# ________________________________________
class Robot():
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100

    def work(self, hours):
        if self.battery_level >= hours * 10:
            self.battery_level -= hours * 10
            return f"{self.name} is working for {hours} hours. The battery level is {self.battery_level}"
        else:
            return f"{self.name} has run out of battery"


robot1 = Robot("IOS")
print(robot1.work(3))
# 18. Task: Create a Trip Class
# Create a Trip class with:
# •  destination (string)
# •  distance (integer, in kilometers)
# •  duration (float, in hours)
# Add methods to:
# •  get_speed(): Calculates and returns the average speed (distance/duration).
# •  update_duration(new_duration): Updates the duration of the trip.
# Objective: Implement calculations and attribute modifications.
# ________________________________________
class Trip():
    def __init__(self, destination, distance, duration):
        self.destination = destination
        self.distance = distance
        self.duration = duration

    def get_speed(self):
        return self.distance / self.duration

    def update_duration(self, new_duration):
        self.duration = new_duration
        return f"New duration is {self.duration}"



trip1 = Trip("Tashkent", 1000, 5)
print(trip1.get_speed())
print(trip1.update_duration(5))
# 19. Task: Create a University Class
# Create a University class with:
# •  name (string)
# •  departments (list of strings)
# •  students (list of strings)
# Add methods to:
# •  add_department(department_name): Adds a department to the university.
# •  enroll_student(student_name): Enrolls a student.
# •  list_all_info(): Prints the university name, departments, and students.
# Objective: Work with strings, lists, and formatted output.
# ________________________________________

class University:
    def __init__(self, name):
        self.name = name  
        self.departments = []
        self.students = [] 

    def add_department(self, department_name):
        self.departments.append(department_name)

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def list_all_info(self):
        print(f"University: {self.name}")
        print("Departments:")
        for department in self.departments:
            print(f" - {department}")
        print("Students:")
        for student in self.students:
            print(f" - {student}")

university = University("PDP")
university.add_department("Computer Science")
university.add_department("Math")
university.enroll_student("Akobir")
university.enroll_student("Jasur")

university.list_all_info()
# 20. Task: Create a Restaurant Class
# Create a Restaurant class with:
# •  name (string)
# •  menu (dictionary with items as keys and prices as values)
# Add methods to:
# •  add_item(item, price): Adds an item to the menu.
# •  remove_item(item): Removes an item from the menu.
# •  get_menu(): Prints the current menu in a readable format.
# Objective: Practice managing dictionaries dynamically and printing formatted output.

class Restaurant():
    def __init__(self, name, menu: dict):
        self.name = name
        self.menu = menu

    def add_item(self, item, price):
        self.menu[item] = price

    def remove_item(self, item):
        del self.menu[item]

    def get_menu(self):
        """in readable format"""
        for item in self.menu:
           print(f"Item: {item}, Price: {self.menu[item]}")



restaurant1 = Restaurant("KFC", {"Chicken": 500, "Pizza": 800})


restaurant1.add_item("Salad", 400)
restaurant1.remove_item("Pizza")
restaurant1.get_menu()