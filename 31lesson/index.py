class BankAccount:
    # __balance = 1000
    _balance = 100

    def __display_balance(self):
        return (f"Your balance is: {self.__balance}")

    def access_balance(self):
        return self.__display_balance()
    
class User(BankAccount):
    def disp(self):
        return self._balance
bank = BankAccount()
# print(bank.access_balance())
print(User().disp())