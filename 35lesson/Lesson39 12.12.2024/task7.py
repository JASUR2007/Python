# 7. Task: Banking SystemCreate a parent class BankAccount with methods for deposit() and withdraw().
# Create child classes SavingsAccount and CheckingAccount.
# SavingsAccount should add a method add_interest().
# CheckingAccount should have a method write_check().

class BankAccount:
    def deposit(self, amount):
        pass
    def withdraw(self,amount):
        pass

class SavingsAccount(BankAccount):
    def add_interest(self, amount):
        super().deposit()
        return f'interest {self.amount}% has been added={amount}'

class CheckingAccount(SavingsAccount):
    def write_check(self):
        return ''
    