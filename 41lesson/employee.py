class Employee():
    def getSalary():
        pass

class Manager(Employee):
    def __init__(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary
    
class Developer(Employee):
    def __init__(self,hours, hour_bill):
        self.hours = hours
        self.hour_bill = hour_bill
    def getSalary(self):
        return self.hour_bill * self.hours
    

emp = [Manager(120), Developer(3, 15)]
for i in emp:
    print(i.getSalary()) 
    # Manager(120).getSalary()
    # Developer(3,15).getSalary()

        