from datetime import datetime
age = int(input('Write your age '))
current_year = datetime.now().year

print(current_year - age)