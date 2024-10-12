height = 0
z = 6
for i in range(z, height, -1):
    if i == z:
        print('*' * z)
    print(' ' * (i-1), end='')
    print('*')
    if i == 1:
        print('*' * z)




# if i == 6 or i == 1: