my_list = ['a', 'b', 'c', 'd']
element = 'c'
try:
    index = my_list.index(element)
    print(" the index of 'c' is", index)
except ValueError:
    print(-1)
   
