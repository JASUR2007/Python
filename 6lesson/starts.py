height = 10
for i in range(height):
    print(' ' * (height - i - 1), end='')
    print('*' * (2 * i + 1))
    if i == height-1:
        print(' ' * i + '*') 

