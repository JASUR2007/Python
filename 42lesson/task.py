from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary():
        pass

class PartTime(Employee):
    def __init__(self,name, amount_for_hour, hour, employee_id):
        super().__init__(name, employee_id)
        self.hour = hour
        self.amount_for_hour = amount_for_hour
    
    def calculate_salary(self):
        return f"Amount of salary for {self.name} is: {self.hour * self.amount_for_hour}, employee_id: {self.employee_id}"

class FullTime(Employee):
    def __init__(self, name, employee_id, days, amount_for_days):
        super().__init__(name, employee_id)
        self.days = days
        self.amount_for_days = amount_for_days

    def calculate_salary(self):
        return f"Amount of salary for {self.name} is: {self.days * self.amount_for_days}"

partTime = PartTime("Otabek", 13, 14, 5)
fullTime  = FullTime("Kimdir", 13, 4,5)
print(partTime.calculate_salary())
print(fullTime.calculate_salary())

