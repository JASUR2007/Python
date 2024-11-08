import math
from math import ceil, pow, sqrt, pi
# a = 4
# b = 10
# c = 3

# d = math.sqrt(b**2 - 4 * a * c)

# if d > 0:
#     x1 = (-b + d) / (2 * a)
#     x2 = (-b - d) / (2 * a)
#     print(f"x1 = {x1}, x2 = {x2}")
# elif d == 0:
#     x1 = -b / (2 * a)
#     print(f"x = {x1}")
# elif d < 0:
#     print('Discriminant is less than 0')
# else:
#     print("Nothing")

# x = int(input('Write radius: '))
# y = int(input('Write number to root it: '))
# z = int(input('Write number to: '))

x = 3
y = 4
print(f"Radius: {x}, area: {pi * x**2:.1f}")
print(f"{sqrt(y):.1f}")


pizza1 = 30
pizza2 = 30

pizza3 = 45

area1 = pi * pow(pizza1/2, 2)
area2 = pi * pow(pizza2/2, 2)
area3 = pi * pow(pizza3/2, 2)
print(area1,area2,area3)
if  area1 + area2 < area3:
   print('45 diametr: more than 2 30 diametr pizza ')
elif area1 + area2 > area3:
    print('45 radius: less ')
else:
    print('equal')

