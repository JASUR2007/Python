new_set = set()
numbers = [1,2,3,4]
new_set.add(1)
new_set.update(tuple(numbers))
print(new_set)
new_set.remove(1)
new_set.discard(2)
print(new_set)

new_set.discard(1)
if 1 not in new_set:
    new_set.add(1)
print(new_set)

nums1 = [1,2,3,4,55,55,4,3,2,1,2]
print('Unique one: ', set(nums1))

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
union_result = set_1.union(set_2)
print(set_1 | set_2 ) #union
print(union_result) #intersection
print(set_1 & set_2)
difference1 = set_1.difference(set_2)
difference2 = set_2.difference(set_1)
# print(difference1)