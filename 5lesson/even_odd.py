numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(f"Even numbers: {even_numbers}\nOdd numvers: {odd_numbers}")

# Even numbers: [2, 4, 6]
# Odd numbers: [1, 3, 5]
   
