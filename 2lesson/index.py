# name = input('ENter your name ')
# age = input('Enter you r age  ')
# gender = input('Enter your gender ')

# print("Your name is ", name, "\nYou are ", age, "years old.\nYou are", gender)
# print(f"Your name is  {name} \nYou are {age} years old.\nYou are {gender}")

# number = input('Enter your name ')
# result = number.capitalize()
# print(result)
# print(number)

name = input('Enter your name ')
surname = input('Enter your surname ')
result = name.capitalize() + ' ' + surname.replace(surname, "smith").capitalize()
print(result)