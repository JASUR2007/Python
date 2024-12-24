class ATM():
    __password = 100
    attempts = 3
    money = 0
    def deposit(self, password, deposit):
        if self.attempts == 0:
            return "Attempts finished"
        if self.__password == password:
            self.money += deposit
            return f"deposit: {self.money}"
        else:
            return "Incorrect password"
    def setPassword(self, old_password, new_pass):
        if self.attempts == 0:
            return "Attempts finished"
        if old_password == self.__password:
            self.__password = new_pass
            return "Password changed"
        else:
            self.attempts = self.attempts - 1 
            return "Incorrect number"
        
        
    def withdrawal(self, withdrawal, password):
        if self.attempts == 0:
            return "Attempts finished"
        if self.__password == password:
            self.money -= withdrawal
            return f"deposit: {withdrawal}"
        else:
            return "Incorrect password"

atm = ATM()
print(atm.setPassword(int(input("Old password: ")), int(input("New password: "))))
print(atm.setPassword(int(input("Old password: ")), int(input("New password: "))))

print(atm.deposit(100, int(input("Write deposit: "))))
print(atm.withdrawal(50, 120))
print(atm.withdrawal(50, 120))
print(atm.withdrawal(50, 120))
print(atm.withdrawal(50, 120))


