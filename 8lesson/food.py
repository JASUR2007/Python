food = input("What do you want to eat? ").casefold()
meals = ["lavash",'hamburger','niga sheyk']

if food in meals:
    print("This is your food")
else:
    print("not found")

drink = input("What do you want to eat? ").casefold()
drinks = ['tea','viska','coffee','coke']
if drink in drinks:
    print("This is your drink")
else:
    print("not found")