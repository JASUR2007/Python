
# ### **Tasks on Lists**

# 1. **Create a list of 5 numbers and find the total (sum) of all the numbers.**
#    - Example: `[1, 2, 3, 4, 5]` → Sum: `15`
def sum_cal():
    numbers = [1, 2, 3, 4, 5]
    result = sum(numbers)
    print(result)
sum_cal()

# 2. **Make a list of 3 favorite fruits and print each fruit on a new line.**
#    - Example: `['apple', 'banana', 'orange']`
def iterated():
    fruits = ['apple', "banana", "orange"]
    for i in fruits:
        print(i)
iterated()
# 3. **Write a program to add a new item to an existing list.**
#    - Example: Start with `[1, 2, 3]` → Add `4` → New list: `[1, 2, 3, 4]`
def item_add():
    numbers = [1,2,3]
    numbers.append(4)
    print(numbers)
item_add()
# 4. **Create a list of 5 numbers and find the largest number in the list.**
#    - Example: `[4, 2, 9, 1, 5]` → Largest number: `9`
def largest_num():
    numbers = [4,2,9,1,5]
    max_number = max(numbers)
    print(max_number)
largest_num()
# 5. **Remove the last item from a list and print the remaining list.**
#    - Example: `[1, 2, 3, 4]` → After removing last: `[1, 2, 3]`
def remove_last():
    numbers = [1,2,3,4]
    numbers.pop()
    print(numbers)
remove_last()
# ---

# ### **Tasks on Tuples**

# 6. **Create a tuple with 4 numbers and print the first and last numbers.**
#    - Example: `(10, 20, 30, 40)` → First: `10`, Last: `40`
def first_last():
    numbers = (10, 20, 30, 40)
    print(f"First: {numbers[0]}, Last:{numbers[-1]}")

# 7. **Make a tuple of 3 colors and check if a certain color is in the tuple.**
#    - Example: `('red', 'green', 'blue')` → Check if `'green'` is there: `True`
def check_color():
    colors = ('red', 'green', 'blue')
    if 'green' in colors: 
        print(True)
check_color()
# 8. **Create a tuple of 3 numbers and add them together.**
#    - Example: `(5, 10, 15)` → Sum: `30`
def add_numbers():
    numbers = (5, 10, 15)
    print(sum(numbers))
add_numbers()
# 9. **Write a program to find the length (number of elements) of a tuple.**
#    - Example: `('a', 'b', 'c')` → Length: `3`
def length_tuple():
    x = ('a','b','c')
    print(len(x))
length_tuple()
# 10. **Convert a list of numbers to a tuple.**
#     - Example: `[1, 2, 3]` → Tuple: `(1, 2, 3)`

# ---
def convert_list():
    numbers = [1, 2, 3]
    print(tuple(numbers))
convert_list()
# ### **Tasks on Dictionaries**

# 11. **Create a dictionary with 2 students and their grades, then print the grade of a specific student.**
#     - Example: `{'Alice': 85, 'Bob': 90}` → Print Bob's grade: `90`
def students():
    grade = {'Alice':85, 'Bob': 90}
    print(grade['Bob'])
students()

# 12. **Add a new item to a dictionary.**
#     - Example: Start with `{'apple': 50}` → Add `{'banana': 30}` → New dictionary: `{'apple': 50, 'banana': 30}`
def add_items():
    fruit = {'apple':50}
    fruit['banana'] = 30
    print(fruit)
add_items()

# 13. **Create a dictionary of 3 animals and their sounds, then print each animal’s sound.**
#     - Example: `{'dog': 'bark', 'cat': 'meow', 'cow': 'moo'}`
def soundsAnimal():
    animal = {'dog':'bark', 'cat':'meow', 'cow':'moo'}
    for animal, sound in animal.items():
        print(f'{animal}, sounds: {sound}')
soundsAnimal()
# 14. **Write a program to change the value (price) of an item in a dictionary.**
#     - Example: `{'apple': 50, 'banana': 30}` → Change apple's price to `60` → New dictionary: `{'apple': 60, 'banana': 30}`
def change_price():
    fruit = {'apple':50, 'banana':30}
    fruit['apple'] = 60
    print(fruit)
change_price()
# 15. **Make a dictionary of 3 countries and their capitals, and then remove one country.**
#     - Example: `{'France': 'Paris', 'Japan': 'Tokyo', 'India': 'Delhi'}` → Remove `Japan` → New dictionary: `{'France': 'Paris', 'India': 'Delhi'}`
def country_change():
    country = {'France':"Paris",'Japan':'Tokyo','India':'Delhi'}
    country.pop('Japan')
    print(country)
country_change()