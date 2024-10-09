word = input('Write word: ')
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word.lower():
    if letter in vowels:
        print("Гласная: " + letter)