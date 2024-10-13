# Homework:
# Task 2: Remove Duplicates
# Write a function to remove duplicates while keeping the order.
# Example:
# strings = ['apple', 'banana', 'apple', 'orange', 'banana']
# print(remove_duplicates(strings))  # Output: ['apple', 'banana', 'orange'
# strings = ['apple', 'banana', 'apple', 1,'orange', 'banana',1,122,2,1]

# duplicate = [] 

# for i in range(len(strings)):
#     for k in range(i):
#         if strings[i] != strings[k]:
#             break
#     else:
#         duplicate.append(strings[i])
# print(duplicate)

strings = ['apple', 'banana', 'apple', 1, 'orange', 'banana']
unique_strings = list(set(strings))

print(unique_strings)