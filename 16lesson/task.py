# You take input from user
# Input is a data in the following format --> 01.04.2024

# You need to show which season it is
# If it is winter:
#      If it is an even day:
           # Print ('It is snowing)
#      Else:
#            Print ('It is not snowing)
# If it is an autumn:
#       If it is an even day:
#            Print ('It is raining')
#       Else:
#            Print('It is not raining')
# If it is a summer or spring:
#      Print('It is spring or summer')

def user():
    date = input("write date: ")

    month = int(date.split('.')[1])
    day = int(date.split('.')[0])
    if month == 1 or month == 2 or month == 12:
        if day % 2 == 0:
            print("it is snowing")
        else:
            print('it is not snowing')
    elif month > 8 and month < 12:
        if day % 2 == 0:
            print("it is raining")
        else:
            print('it is not raining')
    elif month > 2 and month < 6:
           print('It is spring')
    else:
        print('It is summer')      
# user()



# Take phone number from user
# Identify which company it is

# Input: 998931234567
# Ouput: Your company is UCell

# Input: 998113456789
# Output: Such company doesn't exist

# Input: 998a12345678
# Output: Wrong Number format
def phone_number():
    phone = input("write phone number: ")
    srez = int(phone[3:5])

    if phone.isdigit() == False: 
        if srez == 90 or srez == 91:
            print('Your company is Beeline')
        elif srez == 95: 
            print('Your company is Uzmobile')
        elif srez == 97:
            print("Your company is UMS")
        elif srez == 93 or srez  == 94:
            print("Your company is Ucell")
        elif srez == 69:
            print("It is home number")
        else:
            print('Such company doesn"t exist')
    else:
        print("Wrong number format")
phone_number()