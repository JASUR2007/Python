width = int(input("Enter your width "))
height = int(input("Enter your height "))
radius = int(input("Enter your radius "))

if radius == 0:
    if height == width:
        print(height * 4)
    else:
        print((height + width) * 2)
else:
    print(3.14 * radius**2)