size = 7
for i in range(size):
    row = [' '] * size
    row[i] = '*'  
    row[size - i - 1] = '*'
    print(''.join(row))

