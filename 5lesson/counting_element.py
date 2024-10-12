my_list = [1, 2, 2, 3, 4, 2, 5]
element = 3
# (The number 2 appears three times in the list)
counter = 0
for number in my_list:
    if element == number:
        counter+=1   
print(f'The number {element} appears {counter} times in the list')