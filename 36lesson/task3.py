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
    def __init__(self, name:str, salary:float):
        self.name=name
        self.salary=salary
    def display_info(self):
        return f'employee {self.name} gets ${self.salary} salary'

class Manager(Employee):
    def __init__(self, name:str, salary:float, department:str):
        super().__init__(name,salary)
        self.department=department
    def display_info(self):
        return f'{super().display_info()}, department is {self.department}'
class Developer(Employee):
    def __init__(self, name:str, salary:float, programming_languages:list):
        super().__init__(name, salary)
        self.programming_languages=programming_languages
    def display_info(self):
        
        return f'{super().display_info()}, programming languages: {self.programming_languages}'

class EmployeeSystem():
    def __init__(self, employees:list):
        self.employees=employees
    def add_employee(self,employee):
        self.employees.append(employee)
        return f'a new employee {employee.name} has been hired'
    def get_all_employees_info(self):
        for employee in self.employees:
            print(employee.display_info())

manager=Manager('Aminjon', 8500, 'HR')
full_stack=Developer('Hackerboy', 5000, ['HTML', "CSS", "JS", "Python", 'Flutter'])

employeeSystem=EmployeeSystem([])
print(employeeSystem.add_employee(manager))
print(employeeSystem.add_employee(full_stack))
print('\n')
employeeSystem.get_all_employees_info()