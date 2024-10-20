# <!-- <!-- Task 8: List va tupledagi umumiy amal
# Quyidagi tuple va listni yarating:
# num_list = [10, 20, 30, 40]
# num_tuple = (50, 60, 70, 80)
# 2. Ikkisini birlashtirib yangi ro'yxat yarating.
# 3.Yaratilgan ro'yxatdan eng katta va eng kichik qiymatni toping. -->

def min_max():
    num_list = [10, 20, 30, 40]
    num_tuple = (50, 60, 70, 80)
    unified = num_list + list(num_tuple)
    print(f'max: { max(unified)}  min: {min(unified)}')

min_max()

# <!-- Task 9: Tuple ichida tuple bilan ishlash
# Quyidagi tuple'ni yarating: nested_tuple = (1, 2, (3, 4, 5), 6, 7).
# Ichkaridagi tuple'dagi elementlarni ekranga chiqaring.
# Tuple'dagi barcha elementlarni sikl orqali chiqarib bering.

nested_tuple_data = (1, 2, (3, 4, 5), 6, 7)
print(type(nested_tuple_data))

def nestedTuple(nested_tuple):
    for i in nested_tuple:
        if type(i) == tuple:
            nestedTuple(i)
        else: 
            print(i)

nestedTuple(nested_tuple_data)




# Task 10: Listdagi sonlarni ko'paytirish
# Quyidagi listni yarating: numbers = [2, 4, 6, 8, 10].
# Har bir elementni 2 ga ko'paytiring va yangi ro'yxat hosil qiling  -->
def mulitpying():
    numbers = [2, 4, 6, 8, 10]
    new_list = []
    for i in numbers:
        new_list.append(i * 2)
    print(new_list)
mulitpying()