number = int(input("Enter the number: "))
def get_number(number):
    if number % 2:
        return "Нечетное"
    else: 
        return "Четное"

print(get_number(number))