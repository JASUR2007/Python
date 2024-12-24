def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if are_anagrams(word1, word2):
    print(f"'{word1}' и '{word2}'  анаграммы.")
else:
    print(f"'{word1}' и '{word2}' не  анаграммы.")


num = [2,2,1,3,4,0]
def max_num(num):
    if len(num) <= 3:
        return sorted(num)[0]
    return sorted(list(set(num)))[len(num) - 4]

print(max_num(num))
    
nums = [4,4,3,45,65,3,34,5,6, 65]
def highest(nums):
    res = {}
    for i in range(0, len(nums)):
        if res.get(nums[i]) == None:
            res[nums[i]] = 1
        else:
            res[nums[i]] += 1
    max_num = -1
    for num, count in res.items():
        if count == 1 and num > max_num:
            max_num = num
    print(res)
    # return max_num
print(highest(nums))
nums = [4, 4, 3, 45, 65, 3, 34, 5, 6]

