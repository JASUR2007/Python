list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
repeated_elements = []
for element in list1:
    if element in list2 and element not in repeated_elements:
        repeated_elements.append(element)
print(repeated_elements)

#    [3, 4]  # (Common elements)
   
