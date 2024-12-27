# Task: Banking SystemCreate a parent class BankAccount with methods for deposit() and withdraw().
# Create child classes SavingsAccount and CheckingAccount.
# SavingsAccount should add a method add_interest().
# CheckingAccount should have a method write_check().

# Parent class BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, check_limit=1000):
        super().__init__(account_holder, balance)
        self.check_limit = check_limit

    def write_check(self, amount):
        if amount <= self.balance and amount <= self.check_limit:
            self.balance -= amount
            print(f"Check written for ${amount}. New balance: ${self.balance}")
        else:
            print(f"Cannot write check. Either insufficient funds or check exceeds limit.")

savings = SavingsAccount("Alice", 1000)
savings.deposit(500)
savings.add_interest()

checking = CheckingAccount("Bob", 1500)
checking.deposit(200)
checking.write_check(800)
checking.write_check(1000)

# 9. Task: School ManagementCreate a parent class Person with attributes like name and age.
# Create child classes Student and Teacher.
# Student should have a method study().
# Teacher should have a method teach().

class  Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Student(Person):
    def study(self):
        return f'student {self.name} is studying, (s)he is {self.age}'

class Teacher(Person):
    def teach(self):
        return f'teacher {self.name} is teaching, (s)he is {self.age}'

student=Student('Karlson', 12)
print(student.study())

teacher=Teacher('Alex', 35)
print(teacher.teach())