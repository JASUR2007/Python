# Task 1: List yaratish va elementlar bilan ishlash
# Quyidagi listni yarating: numbers = [10, 20, 30, 40, 50].
# Listdagi birinchi elementni 100 ga o'zgartiring.
# Listning oxiriga 60 ni qo'shing.
# Listning uzunligini aniqlang va ekranga chiqaring.

def elements():
    numbers = [10, 20, 30, 40, 50]
    numbers[0] = 100
    numbers.append(60)
    print(f'Length: {len(numbers)}')
elements()

# Task 2: Listdagi elementlarni qo'shish va tahrirlash
# Quyidagi listni yarating: fruits = ['apple', 'banana', 'cherry'].
# Listga orange va kiwi mevalarini qo'shing.
# banana ni mango ga o'zgartiring.
# Listdagi barcha mevalarni alfabetik tartibda joylang.

def fruits():
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('orange')
    fruits.append('kiwi')
    fruits[1] = 'mango'
    fruits.sort()
    print(fruits)
fruits()


# Task 3: Listning indekslari bilan ishlash
# Quyidagi listni yarating: students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina'].
# Zarina qaysi indeksda ekanini toping.
# Listdagi birinchi va oxirgi elementlarni chiqaring.

def index_find():
    students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina']
    students.index('Zarina')
    print(students[0], students[-1])
index_find()

# Task 4: Tuple yaratish va tahlil qilish
# Quyidagi tuple'ni yarating: my_tuple = (5, 10, 15, 20, 25).
# Tuple'dagi uchinchi elementni chiqaring.
# Tuple'da nechta element borligini aniqlang.
def tuple_fun():
    my_tuple = (5, 10, 15, 20, 25)
    print(my_tuple[2])
    print(len(my_tuple))
tuple_fun()