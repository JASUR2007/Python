# # Basic Lambda Usage:

# # 1. Write a lambda function to add 10 to a given number and test it with the input 5.
# #    Example usage:
# #    add_10(5) -> 15

# x = lambda x: x + 10
# print(x(5))
# # 2. Create a lambda function that checks if a number is even and returns True or False.
# #    Example usage:
# #    is_even(4) -> True
# #    is_even(5) -> False
# y = lambda y: y % 2 == 0
# print(y(2))
# # 3. Write a lambda function that takes two arguments and returns their product.
# #    Example usage:
# #    multiply(3, 4) -> 12

# multiply  = lambda z,q: z*q
# print(multiply(3,4))
# # Using Lambda with Built-In Functions:

# # 4. Use a lambda function with map() to square each number in the list [1, 2, 3, 4, 5].
# #    Example result: [1, 4, 9, 16, 25]
# number = [1, 2, 3, 4, 5]
# numbers = list(map(lambda x: x ** 2, number))
# print(numbers)


# # 5. Filter a list of numbers [1, 2, 3, 4, 5, 6] using a lambda function with filter() to keep only odd numbers.
# #    Example result: [1, 3, 5]
# num = [1, 2, 3, 4, 5, 6]
# filtering = list(filter(lambda x: x%2 == 1,num))
# print(filtering)
# # 6. Sort a list of tuples [(2, 5), (1, 7), (4, 1)] by the second value in each tuple using sorted() and a lambda function.
# #    Example result: [(4, 1), (2, 5), (1, 7)]
# # tupled_num = [(2, 5), (1, 7), (4, 1)]
# # cm_results = list(map(lambda x, y: x[1] > y[1], tupled_num, tupled_num))
# # print(cm_results) 
# tupled_num = [(2, 5), (1, 7), (4, 1)]
# sorted = sorted(tupled_num, key=lambda x: x[1])
# print(sorted)
# # Lambda in Data Processing:

# # 7. Create a list of strings ['apple', 'banana', 'cherry'] and use map() with a lambda function to capitalize each word.
# #    Example result: ['Apple', 'Banana', 'Cherry']
# capitalized = ['apple', 'banana', 'cherry']
# print(list(map(lambda x: x.capitalize(), capitalized)))

# # 8. Use a lambda function to find the maximum value in a list of dictionaries based on a specific key.
# #    Example data: [{'name': 'A', 'score': 50}, {'name': 'B', 'score': 85}]
# #    Task: Find the dictionary with the highest score.
# #    Example result: {'name': 'B', 'score': 85}
# max_value = [{'name': 'A', 'score': 50}, {'name': 'B', 'score': 85}]
# print(max(max_value, key=lambda x: x['score']))
# # Lambda with Custom Conditions:

# # 9. Filter a list of names ['Alice', 'Bob', 'Charlie', 'David'] to include only names that have more than 3 characters using a lambda function.
# #    Example result: ['Alice', 'Charlie', 'David']

# names = ['Alice', 'Bob', 'Charlie', 'David']
# print(list(filter(lambda x: 3 < len(x), names)))

# # 10. Write a lambda function to calculate the result of x^2 + 2x + 1 for any given value of x.
# #     Example usage:
# #     quadratic(2) -> 9
# ex = lambda x: x**2 + 2*x + 1
# print(ex(2))



# res = 100
# while res > 1:
#     res -=1 
#     print(res)



# a = int(input())
# for i in range(a):
#     stroka = input()
#     if len(stroka) > 10:
#         result = stroka[0]+str(len(stroka[1:-1]))+stroka[-1]
#     else:
#         result = stroka

#     print(result)


# a = input()
# # while a:
# num = str(a)
# for i in num:
#     for k in range(1, 4):
#         if num[k] == num[-k]:
#             print('soidihvjosdv')

#         else:
#             print('gay')


# a = input()
# for i in range(int(a)+1, 10000):
#     if len(set(str(i))) == len(str(i)):
#         print(i)
#         break

        

a = int(input())  
res = ''

for i in range(a):
    if i % 2 == 0:  
        res += "I hate"
    else:  
        res += "I love"
    if i < a - 1:
        res += " that "
    else:
        res += " it"

print(res)  


