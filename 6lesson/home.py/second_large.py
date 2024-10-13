# Write a function that finds the second largest number in a list of integers.
# lst = [5, 3, 9, 7, 9, 5]
# print(second_largest(lst))  # Output: 7

lst = [5, 3, 9, 7, 9, 5]
numbers = []
for number in lst:
    if max(lst) != number:
        numbers.append(number)
print(max(numbers))