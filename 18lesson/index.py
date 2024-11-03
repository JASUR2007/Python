# Homework:

# Multiplication Table
# Description: Create a while loop to print the multiplication table of a given number up to 10.
# Example Input/Output:
# Input: 5
# Output:
# Copy code
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50
def multi_table(x):
    i = 0
    while i < 11:
        print(x * i)
        i+=1 
# multi_table(5)

#  Count Vowels in a String

# Description: Ask the user to input a string and use a while loop to count the number of vowels in it.
# Example Input/Output:
# Input: hello world
# Output:
# Number of vowels: 3
def count_vowel():
    words = input("Write text: ").casefold()
    vowels = 'aeiou'
    i = 0
    check = 0
    while i < len(words):
        if words[i] in vowels:
            check += 1
        i += 1
    print("\nNumber of vowels:", check)    
# count_vowel()

# Description: Ask the user to enter a number and use a while loop to calculate the factorial of that number.
# Example Input/Output:
# Input: 5
# Output:
# The factorial of 5 is 120
def factorial():
    rost = int(input("Enter a number: "))
    i = 0
    sum = 1
    while i < rost:
        i +=1
        sum *= i
    print(sum)
# factorial()
# 18. Find Divisors of a Number
# Description: Ask the user to enter a positive integer, and use a while loop to print all its divisors.

# Input: 12

# Output: Divisors: 1, 2, 3, 4, 6, 12
def find_divisors():
    num = int(input("Enter a positive integer: "))
    i = 1
    if num < 1:
        print("Invalid")
    else: 
        while i <= num:
            if num % i == 0:
                print(i)
            i += 1
find_divisors()