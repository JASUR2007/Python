number = 1
if number % 2 == 0:
    print('hello')
    if number % 3 == 0:
        print("My friend")



#1 Ask user about his name, age, gender
#2 If username in account_list print "You are welcome"
#3 Record his data into history dictionary
#4 If username is not in account_list print "Username is incorrect"
#5 Record his data into failed_login dictionary
def program():
    name = input("What's your name? ")
    gender = input("What's your gender? ")
    age = int(input("How old are u? "))
    account_list = ['Admin', 'User', "Guest User", 'Host', "Sanjar", "PDP", "System"]
    history = {}
    status = ''
    failed_login = {}
    if name in account_list:
        print("U are welcome!")
        status = "Sucessfull login"
        history[name] = {'age':age, 'gender': gender, 'status': status}
        print(history)
    else:
        print("Wrong login")
        status = 'Failed login'
        failed_login[name] = {'age': age, 'gender': gender, 'status': status}
        print(failed_login)
# program()


# Ask user to input three digit number
# If all numbers are different Print (These numbers are different)
# If two numbers are similar Print(Two numbers are similar)
# If all numbers are similar Print(All numbers are similar)
# If user doesnt input number (string, float, True or False) Print(It is not a number)

# user --> 344
# print(Two numbers are similar)

# user --> 444
# print(All numbers are similar)

# user --> 123
# print(These numbers are different)

# user --> Hello
# print(It is not a number)
    if not one.isdigit():
        print("Please enter a valid number.")
        return
    
    for i in range(len(one)):
        for j in range(i + 1, len(one)):
            if one[i] == one[j]:
            