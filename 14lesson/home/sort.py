# 1.
# # Given a list of numbers. Find the index of every occurences of "k" element
# # Input: numbers = [9,1,2,9,3,4,5,9], # k = 9
# # Output: 9 is located at index 0, 3, 7

gather = []
def find_index(k):
    numbers = [9,1,2,9,3,4,5,9]
    for i in range(len(numbers)): 
        if numbers[i] == k:
            gather.append(i)
    print(f'{k} is located at index', gather)

find_index(9)


# 2.Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
def target_index(nums, target):
    if target in nums:
        print(nums.index(target))
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                print(i)
                return
        print(len(nums)) 
target_index([1,3,5,6], 2)



# 3. Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3,3,4,5,6,5,5,4,4,4,4,4], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

def frequent_elements(nums, k):
    finding = {}
    for num in nums:
        if num in finding:
            finding[num] += 1
        else:
            finding[num] = 1
    result = []
    for _ in range(k):
        max_num = 0
        most_of = None
        for num, freq in finding.items():
            if freq > max_num:
                max_num = freq
                most_of = num
        result.append(most_of)
        finding[most_of] = -1
    print(result)

frequent_elements([1, 1, 1, 2, 2, 3,5,5,5], 3) 