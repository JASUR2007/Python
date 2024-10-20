# Task 5: Tuple va list orasidagi farqlar
# Quyidagi tuple va listni yarating:
# my_tuple = (1, 2, 3)
# my_list = [1, 2, 3]
# 2. Listga 4 raqamini qo'shing, lekin tuple'ga qo'shib bo'lmasligini tushuntiring.
# 3. List va tuple o'rtasidagi asosiy farqlarni tushuntirib bering.
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]



# Task 6: List va tuple orasida konvertatsiya qilish
# Quyidagi tuple'ni yarating: colors = ('red', 'green', 'blue').
# Tuple'ni ro'yxatga o'zgartiring va unga yangi rang yellow ni qo'shing.
# Ro'yxatni yana tuple'ga o'zgartiring va natijani chiqaring.
def tupling():
    colors = ('red', 'green', 'blue')
    listing = list(colors)
    listing.append('yellow')
    listing = tuple(listing)
    print(listing)
tupling()

# Task 7: Elementlarni qo'shish va teskari qilish
# Quyidagi listni yarating: numbers = [5, 10, 15, 20, 25].
# Listga 30 raqamini qo'shing va listdagi elementlarni teskari tartibda joylang.
# Shuningdek, tuple yaratib, uni ham teskari qilib chiqaring: my_tuple = (10, 20, 30, 40).

def elements():
    numbers = [5, 10, 15, 20, 25]
    numbers.append(30)
    numbers.reverse()
    my_tuple = (10, 20, 30, 40)
    tupler = list(my_tuple)
    tupler.reverse()
    tuple(tupler)
    print(tupler)  
elements()
# print()