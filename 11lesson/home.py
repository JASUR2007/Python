zora = {'a':100, 'b': 200, "c": 300}
sum = 0
for i,j in zip(zora.keys(), zora.values()):
    sum += j
print(sum)

# zora = {'a':100, 'b': 200, "c": 300}
# sum = 0
# for j in zora.values():
#     sum += j
# print(sum)