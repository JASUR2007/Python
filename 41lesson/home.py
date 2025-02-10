# 1. Animal Sounds
# Create a base class Animal with a method make_sound.
# Subclasses Dog, Cat, and Cow should override the make_sound method to print "Woof!", "Meow!", and "Moo!", respectively.
# Create a list of animals and call the make_sound method on each.

# 2. Vehicle Speeds
# Create a base class Vehicle with a method speed.
# Subclasses Car, Bike, and Train should override speed to return "Fast", "Moderate", and "Very Fast", respectively.
# Write a function to print the speed of any vehicle passed to it.
# 3. Payment System
# Create a base class Payment with a method process_payment.
# Subclasses CreditCardPayment, PaypalPayment, and CashPayment should override the method to print different messages (e.g., "Processing credit card payment").
# Create a list of payment methods and call process_payment on each.
# 4. Library Books
# Create a base class Book with a method get_details.
# Subclasses FictionBook and NonFictionBook should override get_details to print specific details about the type of book.
# Write a function to display details of a list of books.

class Book():
    def get_details():
        pass

class FictionBook():
    def __init__(self, type_of_book):
        self.type_of_book = type_of_book
    
# class NonFictionBook():
    # def __init__(self,)