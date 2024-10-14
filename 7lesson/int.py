numbers = [5, 8, 11, 12,22]

for i in range(0, len(numbers)):
    if numbers[i] % 2:
        numbers[i] = 'odd'
    else:
        numbers[i] = 'even'

# for i in numbers:
#     if i % 2 == 0:
#         numbers.insert(numbers.index(i), 'even')
#         numbers.remove(i)
#     else:
#         numbers.insert(numbers.index(i), 'odd')
#         numbers.remove(i)
        

# numbers = ['odd' if number % 2 else 'even' for number in numbers]
print(numbers)