import os
class ATM:
    def __init__(self):
        self.balance = 1000
        self.password = "1234"
        self.phone_payments = {}
        self.credit_payments = {}
        self.utility_payments = {}

    def authentificate(self):
        for i in range(3):
            entere_password = input("please enter password:")
            if entere_password == self.password:
                return True
            else:
                print("Try again!")
        print("Too many failed attempts. Your card is blocked")
        return False
    
    def clear_screen(self):
        os.system('cls' if os.name == "nt" else "clear")
        
    def display_menu(self):
        menu = [
            "1. Check balance",
            "2. Withdraw money",
            "3. Change password",
            "4. Pay phone fee",
            "5. Pay credit",
            "6. Utility bills",
            "7. Exit"
        ]

        for item in menu:
            print(item)

    def check_balance(self):
        self.clear_screen()
        
        while True:
            print(f"Your current blalance is ${self.balance}")
            if input("Press '0' to go back:") == "0":
                break
            else:
                print("Invalid option")
    
    def withdraw_money(self):
        self.clear_screen()
        while True:
            amount = int(input("Please enter the withdrawal amount or press '0' to go back:"))
            
            if amount == 0:
                break
            else:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Accepted!, your current balance is {self.balance}")
                else:
                    print("Not enough money")

    def change_passwor(self):
        self.clear_screen()
        while True: 
            old_password = input("Write your password or press '0' to go back:")
            if old_password == '0':
                break
            else:
                if old_password == self.password:
                    new_password = input('Please enter the new password:')

                    if new_password == input('Please enter the confirm password:'):
                        self.password = new_password
                        print("Successfully changed.")
                    else:
                        print('Incorrect cofirm password.')
                else:
                    print("You entered incorrect password.")


    def run(self):
        self.clear_screen()
        print("Welcome to ATM!")
        if self.authentificate():
            while True:
                self.display_menu()

                choice = input("Select a menu option: ")

                if choice == '1':
                    self.check_balance()
                elif choice == '2':
                    self.withdraw_money()
                elif choice == '3':
                    self.change_passwor()
                elif choice == '7':
                    print("Thank you for using our ATM. Bye-bye!")
                    break
                else:
                    print("Invalid option")

atm = ATM()
atm.run()