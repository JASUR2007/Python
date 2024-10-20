# Task 11: Listdan elementni olib tashlash
# Quyidagi listni yarating: my_list = ['apple', 'banana', 'cherry', 'date', 'fig'].
# Listdan cherry ni olib tashlang.
# Listdan oxirgi elementni olib tashlang va natijani chiqaring.
def fruits():
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
    my_list.remove('cherry')
    my_list.remove(my_list[-1])
    print(my_list)
fruits()

# Task 12: Listda elementlarni tartiblash
# Quyidagi listni yarating: ages = [34, 23, 45, 27, 56, 18].
# Listdagi elementlarni o'sish tartibida joylang.
# Keyin, listdagi elementlarni kamayish tartibida joylang.
def sorting():
    ages = [34, 23, 45, 27, 56, 18]
    ages.sort()
    print(ages)
    ages.reverse()
    print(ages)
sorting()



# Task 13: Listdagi takroriy elementlarni olib tashlash
# Quyidagi listni yarating: numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7].
# Listdagi takroriy elementlarni olib tashlang va yangi list yarating.
# Yangi listni ekranga chiqaring.
def duplicates():
    numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
    duplicate = list(set(numbers))
    print(duplicate)
duplicates()

# Task 14: Tuple'dagi eng katta va eng kichik qiymatlarni topish
# Quyidagi tuple'ni yarating: numbers = (10, 50, 25, 5, 100, 75).
# Tuple'dagi eng katta va eng kichik qiymatlarni toping.
def max_min(): 
    numbers = (10, 50, 25, 5, 100, 75)
    print(f"max: {max(numbers)}, min: {min(numbers)}")
    print('3')
max_min()
    
# Task 15: List elementlarini juftliklarga bo
# 'lish
# Quyidagi listni yarating: my_list = [10, 20, 30, 40, 50, 60].
# Listdagi elementlarni har ikkitadan juftlik qilib chiqaradigan kod yozing. Natija quyidagicha bo'lishi kerak: [(10, 20), (30, 40), (50, 60)].
