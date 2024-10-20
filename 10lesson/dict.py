num1 = {}
num1[0] = 1
num1[1] = 2
num1[2] = 3
num1[3] = 4
num1[4] = 5
print(num1)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwem']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)



# name = 'My name is Gustavo'
# d = name.split()


# name = input('Write smth:')
# d = name.split()
# print(f"first: {len(d[0])} last: {len(d[-1])} middle: {len(d[int(len(d) /2)])}")



counts = dict()
line = input('Enter a line of text:')
words = line.split()

print('Words', words)
print('Counting')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)