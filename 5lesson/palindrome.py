my_list = [1, 2, 3, 2, 1]
is_palindrome = True
for i in range(len(my_list) // 2):
    if my_list[i] != my_list[-(i + 1)]:
        is_palindrome = False
        break
print(is_palindrome)

#    True  # (The list is a palindrome)
