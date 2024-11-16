import math
def reversed_string(name):
    return name[::-1]
print(reversed_string('apple'))

def min_change(min):
    return (min // 60, min % 60,)
print(min_change(130))

def pythagorean(a, b):
    return math.sqrt(math.pow(a,2) * math.pow(b, 2))
print(pythagorean(3,4))

def leap_year(year):
    if 0 == year % 4 and 0 != year % 100 or 0 == year % 400:
        return True
    else:
        return False
print(leap_year(int(input("Write year: "))))

def password_strength_checker(password: str):
    strength1 = len(password) > 8
    strength2 = any(char.islower() for char in password)
    strength3 = any(char.isupper() for char in password)
    strength4 = any(char.isdigit() for char in password)
    strength5 = any(char in '!@#$%^&*()' for char in password)
    over_strength = strength1 + strength2 + strength3 + strength4 + strength5
    return over_strength

password = input('Write the password: ')
print(password_strength_checker(password))

def char_frequency(string,char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return f'times of the character {count}'
print(char_frequency(input('write some string: ').lower(),input('Write the char which you are searching: ').lower()))


def caesar_cipher(name, num):
    namer = name.casefold()  
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dock = list(alphabet)  
    result = []
    for i in range(0, len(namer)): 
        if namer[i] in dock: 
            current = dock.index(namer[i])
            shifted = (current + num) % len(dock)  
            result.append(dock[shifted])
        else:
            result.append(namer[i])
    return ''.join(result)  
print(caesar_cipher("Jasurz", 2))

def digit_sum(number):
    if number < 0:
        return "it is negative"
    else:
        return sum([int(i) for i in str(number)])
print(digit_sum(23))

def email_validator(email):
    if '@' in email and '.' in email and email.index('@') < email.index('.'):
        return True
    else:
        return False

email = input('Write the email: ')
print(email_validator(email))

def text_obfuscator(a: str):
    vowels = 'aeiou'
    result = ''
    for char in a:
        if char.lower() in vowels:
            result += '*'
        else:
            result += char
    return result

a = input('write the string: ')

print(text_obfuscator(a))

