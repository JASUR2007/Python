name = ['James', 'Alex', 'John']
surname = ["Bond", 'Mercer', 'Smith']
full_name = []
for (x, y) in zip(name, surname):
    full_name.append(x)
    full_name.append(y)
print(full_name)