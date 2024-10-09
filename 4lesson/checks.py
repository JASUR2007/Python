char = input("Enter a single character: ")  
if len(char) == 1:
    if char.isalpha():
        print("The character is a letter.")
    elif char.isdigit():
        print("The character is a digit.")
    else:
        print("The character is neither a letter nor a digit.")
else:
    print("Please enter only a single character.")