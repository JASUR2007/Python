# 1. Create a list of 5 numbers, find the sum, and the average of the numbers.
#    - Example: [1, 2, 3, 4, 5] → Sum: 15, Average: 3
def sum_cal():
    numbers = [1, 2, 3, 4, 5]
    result = sum(numbers)
    print(result)
sum_cal()

# 2. Make a list of 5 fruits and print them in reverse order (without reversing the list itself).
#    - Example: ['apple', 'banana', 'cherry', 'date', 'elderberry'] → Output: 'elderberry', 'date', 'cherry', 'banana', 'apple'
def iterated():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(fruits[::-1])
iterated()
# 3. Write a program to insert a new item at the second position in a list.
#    - Example: Start with [1, 3, 4] → Insert 2 at position 2 → New list: [1, 2, 3, 4]
def new_item():
    x = [1, 3, 4]
    x.insert(1, 2)
    print(x)
new_item()
# 4. Create a list of numbers and print both the largest and smallest numbers in the list.
#    - Example: [4, 2, 9, 1, 5] → Largest: 9, Smallest: 1
def smallest_largest():
    numbers = [4, 2, 9, 1, 5]
    smallest = min(numbers)
    largest = max(numbers)
    medium = sum(numbers) / len(numbers)
    print(f"Smallest: {smallest}, Largest: {largest}, medium: {medium}")
smallest_largest()

# 5. Remove an item from a list based on its value, not its position.
#    - Example: [10, 20, 30, 40] → Remove 30 → New list: [10, 20, 40]

# ---
def remove_item():
    x = [10, 20, 30, 40]
    x.remove(30)
    print(x)
remove_item()
# ### Tasks on Tuples

# 6. Create a tuple with 5 numbers and print the second-to-last number.
#    - Example: (10, 20, 30, 40, 50) → Second-to-last number: 40
def second_to_last():
    x = (10, 20, 30, 40, 50)
    print(x[-2])
second_to_last()

# 7. Make a tuple of 4 colors, check if a color is not in the tuple, and print the result.
#    - Example: ('red', 'green', 'blue', 'yellow') → Check if 'purple' is not there: True
def color_checked():
    x = ('red', 'green', 'blue', 'yellow')
    if 'purple' not in x:
        print(True)
color_checked()
# 8. Write a program to multiply all elements in a tuple of 3 numbers.
#    - Example: (2, 4, 6) → Output: 2 * 4 * 6 = 48
def multiply():
    x = (2,4,6)
    result = 1
    for i in x:
        result = result * i
    print(result)        
multiply()

# 9. Create a tuple and use a loop to print each element with its index.
#    - Example: ('a', 'b', 'c') → Output: 0: 'a', 1: 'b', 2: 'c'
def index_element():
    loops = ('a', 'b', 'c')
    index = 0
    for value in loops:
        print(f"{index}: {value} ")
        index += 1
index_element()

# 10. Convert a tuple into a list, change an item in the list, and convert it back to a tuple.
#     - Example: (1, 2, 3) → Convert to list: [1, 2, 3], Change 2 to 5 → Back to tuple: (1, 5, 3)

# ---
def converting():
    q = (1, 2, 3)
    change = list(q)
    change[1] = 5
    x = tuple(change)
    print(x)
converting()
# ### Tasks on Dictionaries

# 11. Create a dictionary with 3 students and their grades, then find the average grade of all students.
#     - Example: {'Alice': 85, 'Bob': 90, 'Charlie': 78} → Average: 84.33
def average_student():
    x = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    average = 0
    for i in x.values():
        average += i
    print(average/len(x))
average_student()
# 12. Add multiple new items to a dictionary at once.
#     - Example: Start with {'apple': 50} → Add {'banana': 30, 'grape': 60} → New dictionary: {'apple': 50, 'banana': 30, 'grape': 60}
def multiplied():
    fruit = {'apple': 50}
    new_items = {'banana': 30, 'grape': 60}
    x = fruit | new_items
    print(x)
multiplied()
# 13. Create a dictionary of 3 countries and their capitals, then print the capital of a specific country entered by the user.
#     - Example: {'France': 'Paris', 'Japan': 'Tokyo', 'India': 'Delhi'} → User inputs Japan, Output: 'Tokyo'
def capital_country():
    capital = "Japan"
    # capital = input('Enter the coutry: ')
    capitals = {'France': 'Paris', 'Japan': 'Tokyo', 'India': 'Delhi'}
    print(capitals[capital])
capital_country()
# 14. Write a program to update the price of an item in a dictionary, only if the item exists.
#     - Example: {'apple': 50, 'banana': 30} → Update banana price to 40 → New dictionary: {'apple': 50, 'banana': 40}
def update_price():
    fruits = {'apple': 50, 'banana': 30}
    fruits['banana'] = 40
    print(fruits)
update_price()
# 15. Make a dictionary of 4 fruits and their prices, then delete a fruit chosen by the user.
#     - Example: {'apple': 50, 'banana': 30, 'grape': 60, 'orange': 25} → User deletes banana → New dictionary: {'apple': 50, 'grape': 60, 'orange': 25}
def delete_user():
    fruits = {'apple': 50, 'banana': 30, 'grape': 60, 'orange': 25}
    fruits.pop('banana')
    print(fruits)
delete_user()

def numbers():
    lists = [1,2,34,3,2,8,7,4,5,7,12,3,34]
    results = []
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    print(lists)
numbers()




n = [1, 4, 5, 7]

# 4
# for i in n:
    # print(i)
print(4)