# // ### 1. Basic Encapsulation  
# // Create a class called Person with private attributes for name and age. Implement public methods to get and set the name and age.  
# // - Ensure the name can be changed, but only if it is not empty.  
# // - Ensure the age can only be set to a positive integer.

# // ---
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_name(self, new_name):
        if not self.__name:
            return "The name is empty"
        else:
            self.__name = new_name 
            return f"The name changed to {new_name}"
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            return  f"{new_age} years added"
        else:
            return "The number cannot be negative"

ex_1 = Person('Adrian', 25)
print(ex_1.get_name())
print(ex_1.get_age())
# // ### 2. Product Class  
# // Create a Product class that has private attributes for the product name, price, and quantity.  
# // - Implement methods to get and set each attribute.  
# // - Add a method to apply a discount to the price (should not allow negative prices or quantities).

# // ---

# // ### 3. Bank Account  
# // Create a BankAccount class with private attributes for account number and balance.  
# // - Implement methods to deposit and withdraw money (ensure the balance cannot go below zero).  
# // - Create a method to transfer money between two accounts.  
# // - Add a method to check the balance.

# // ---

# // ### 4. Temperature Conversion  
# // Create a Temperature class with private attributes for Celsius and Fahrenheit.  
# // - Implement methods to get and set the Celsius and Fahrenheit values.  
# // - Ensure that setting one temperature automatically updates the other based on conversion (Celsius to Fahrenheit and vice versa).

# // ---

# // ### 5. Student Grades  
# // Create a Student class with private attributes for name and a list of grades.  
# // - Implement methods to add grades, get the grades, and calculate the average grade.  
# // - Ensure that the grades are between 0 and 100.

# // ---

# // ### 6. Employee Class  
# // Create an Employee class with private attributes for employee name, salary, and position.  
# // - Implement public methods to get and set the name, salary, and position.  
# // - Ensure the salary cannot be negative, and the position must be one of the following: "Manager," "Developer," "Intern."

# // ---

# // ### 7. Car Class  
# // Create a Car class with private attributes for make, model, and year.  
# // - Implement public methods to get and set the make, model, and year of the car.  
# // - Add a method to display the car details in a formatted string.

# // ---

# // ### 8. Library Book  
# // Create a Book class with private attributes for the book title, author, and publication year.  
# // - Implement public methods to get and set these attributes.  
# // - Add a method to check if the book is available (boolean) and implement the logic for borrowing and returning the book.

# // ---

# // ### 9. Wallet Class  
# // Create a Wallet class with a private attribute for the balance.  
# // - Implement methods to add money, remove money, and check the balance.  
# // - Ensure that money cannot be withdrawn if there is insufficient balance.

# // ---

# // ### 10. Circle Class  
# // Create a Circle class with a private attribute for the radius.  
# // - Implement methods to get and set the radius.  
# // - Add a method to calculate and return the area and circumference of the circle.

# // ---

# // ### 11. Rectangle Class  
# // Create a Rectangle class with private attributes for length and width.  
# // - Implement methods to set and get the dimensions of the rectangle.  
# // - Add methods to calculate and return the area and perimeter of the rectangle.

# // ---

# // ### 12. Account Holder  
# // Create an AccountHolder class with private attributes for name, account number, and balance.  
# // - Implement methods to get and set each of these attributes.  
# // - Add a method to display the account details in a formatted string.

# // ---

# // ### 13. Person with Address  
# // Create a Person class that includes a private attribute for the address.  
# // - Implement methods to set and get the address.  
# // - Ensure that the address is a string containing at least one character.

# // ---

# // ### 14. Bookstore Inventory  
# // Create an Inventory class to track books in a bookstore.  
# // - Implement private attributes for book name, price, and quantity.  
# // - Implement methods to update the quantity and price of a book, and get the total inventory value.
