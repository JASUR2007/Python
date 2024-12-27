# Task: Employee Hierarchy
# Create a parent class Employee with attributes like name and salary, and a method work().
# Create child classes Manager and Developer.
# Manager should have a method hold_meeting().
# Developer should have a method write_code().

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f'Name is {self.name}\nsalary is ${self.salary}')

class Manager(Employee):
    def hold_meeting(self):
        super().work()
        return f'manager is holding meeting\n'

class Developer(Employee):
    def write_code(self):
        super().work()
        return f'the developer is writing code'

manager1=Manager('Aminjon', 98500000)
print(manager1.hold_meeting())

coder=Developer('Dev', 80000)
print(coder.write_code())