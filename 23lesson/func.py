def peri_rectangular(a,b):
    print(2*(a+b)) 

peri_rectangular(2,3)


def area_rectangular(a,b):
    print(a*b) 

area_rectangular(2,3)


def odd_even(number):
    if number % 2:
        print("is odd")
    else:
        print("is even")

odd_even(2)    

def find_max(num1, num2, num3):
    print(max(num1, num2, num3))

find_max(3,2,32223)

def factorial(n):
    sum = 1
    if n>0:
        for i in range(n, 1, -1):
            sum *= i
        print(sum)
    else:
        print('negative num')
        
factorial(1)


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)

fibonacci(4)