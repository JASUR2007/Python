    # You are given two strings s and t.

    # String t is generated by random shuffling string s and then add one more letter at a random position.

    # Return the letter that was added to t.

    # Example 1:

# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:

# Input: s = "", t = "y"
# Output: "y"



# s = "abcd"
# t = "abcde"
# count = {}

# for word in t:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1

# for add in s:
#     if add in count:
#         count[add] -= 1

# for counter in count:
#     if count[counter] == 1:
#         added_char = counter

# print(added_char)

s = "abcd"
t = "eabcd"

for i in t:
    if i not in s: 
        print(i)
