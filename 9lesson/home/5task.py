# Task 16: Tuple'ni slicing (kesish) orqali ishlatish
# Quyidagi tuple'ni yarating: alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g').
# Tuple'dan faqat birinchi uchta elementni kesib oling va yangi tuple yarating.
# Oxirgi uchta elementni kesib oling va chiqaring.
def slicing():
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    slicer = slice(3)
    print(alphabet[slicer])
slicing() 

# Task 17: Listni for sikli orqali chiqarish
# Quyidagi listni yarating: names = ['Ali', 'Olim', 'Zarina', 'Jasur'].
# for sikli yordamida har bir ismdan keyin " - talaba" so'zini qo'shib chiqaring. Masalan: Ali - talaba.
def sikl():
    names = ['Ali', 'Olim', 'Zarina', 'Jasur']
    for i in names:
        print(i + " - talaba")
sikl()

# Task 18: Tuple'ni for sikli orqali chiqarish
# Quyidagi tuple'ni yarating: temperatures = (22, 25, 28, 30, 27, 23).
# Tuple'dagi har bir harorat qiymatini ekranga chiqaring.
def siklni_for_tuple():
    temperatures = (22, 25, 28, 30, 27, 23)
    for i in temperatures:
        print(i)
siklni_for_tuple()
# Task 19: Listdagi sonlarni topib yig'ish
# Quyidagi listni yarating: my_list = [1, 5, 'banana', 10, 'apple', 20].
# Faqat raqamlar yig'indisini toping va natijaniьюооь chiqaring.
def gather_number():
    my_list = [1, 5, 'banana', 10, 'apple', 20]
    my_number = []
    for i in my_list:
        if type(i) == int:
            my_number.append(i)
    print(my_number)    
gather_number()
# Task 20: Tuple va listda elementlarni almashtirish
# Quyidagi listni yarating: my_list = [10, 20, 30].
# Quyidagi tuple'ni yarating: my_tuple = (40, 50, 60).
# Birinchi elementlarini almashtiring. Yani my_list[0] va my_tuple[0] qiymatlarini bir-biriga almashtiring va natijani chiqaring.
def metamorphose():
    my_list = [1, 5, 'banana', 10, 'apple', 20]
    my_tuple = (40, 50, 60)
    my_rock = list(my_tuple)
    my_list[0], my_rock[0] = my_tuple[0], my_list[0]
    my_tuple = my_rock
    print(my_list, my_tuple)
metamorphose()