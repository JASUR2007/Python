# Shopping List Price Calculator

# Create a program where the user can enter items and their prices to build a shopping list.
# Use a loop to prompt the user to enter the item name and price until they type "done." Store each item in a list of tuples (item, price).
# After finishing, calculate and print the total price, the average price per item, and the most expensive item in the list.
# Example:
# Input: "apple 1.5", "banana 0.8", "milk 2.3", "done"
# Output: Total: 4.6, Average: 1.53, Most Expensive: milk, Cheapest: banana

def shopping():
    products = []

    while True:
        product = input('Enter item and price (or type "done" to finish): ').strip()

        if product.lower() == 'done':
            break

        input_parts = product.split()

        if len(input_parts) == 2: 
            item = input_parts[0]
            price = input_parts[1]

            if price.replace('.', '', 1).isdigit():
                products.append((item, float(price)))
            else:
                print("Invalid price.")
        else:
            print("Enter like 'apple 1.5'.")

    if len(products) == 0:
        print("No items entered.")
        return

    total_price = 0
    most_expensive_price = 0
    cheapest_price = float('inf')
    expensive = ""
    cheap = ""

    for product in products:
        item, price = product
        total_price += price

        if price > most_expensive_price:
            most_expensive_price = price
            expensive = item

        if price < cheapest_price:
            cheapest_price = price
            cheap = item

    average_price = total_price / len(products)

    print(f"\nTotal price: {total_price: 1f}")
    print(f"Average price per item: {average_price: 1f}")
    print(f"Most expensive item: {expensive}")
    print(f"Cheapest item: {cheap}")

# shopping()






# Sanjar Shukurov, [07.11.2024 9:35]
# Write a function find_pairs(nums, target) that takes a list of integers nums and an integer target. 
# The function should find all unique pairs of numbers that add up to the target and return them as a list of tuples.
# Example:
# Input: nums = [2, 4, 3, 5, 7, -1, 8], target = 7
# Output: [(2, 5), (4, 3), (-1, 8)]

# Sanjar Shukurov, [07.11.2024 9:35]
# price = []
# item = []
# shop_dict = {}
# nums = []
# flag = True
# while True:
#     shop_list = input('Enter the item:')
#     shop_price = float(input('Enter the price:'))
        
#     if shop_list != 'done':
#         item.append(shop_list)
#         price.append(shop_price)
#     else:
#         break
# for i,j in zip(item,price):
#     shop_dict[i] = j
#     print(i, j)
#     # nums.append(j)

nums = [2, 4, 3, 5, 7, -1, 8,3]
targets = len(nums)
for i in nums:
    for j in nums:
        if i + j == targets:
            print(i, j)


a = set()
b = set()

for num in nums:
    complement = targets - num
    if complement in a:
        b.add(tuple(sorted((num, complement))))
    a.add(num)

print(b)



# input 3
# output [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]]]
# n = int(input('Write the num: '))
# b = [i for i in range(1, n**n+1 )]

# while b:
#     for x in b:
#         if len(b)%n == 0:
#             b = [b]



