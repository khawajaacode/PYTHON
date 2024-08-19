"""
def greet():
    print("Hello,World")



def parameter(name):
       print(f"hello,{name}")

def add(a,b):
    return a+b

def my_function():
    var = 52
    print(var)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



greet()
parameter("Python")
print(add(12,32))
my_function()

num = float(input("Enter a number: "))
print(f"the factorial of {num} is {factorial(num)}")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


def maximum(a, b , c):
    return max(a, b, c)

def minimum(a, b , c):
    return min(a, b, c)


var1 = float(input("Enter a number 1: "))
var2 = float(input("Enter a number 2: "))
var3 = float(input("Enter a number 3: "))

maximum = maximum(var1, var2, var3)
minimum = minimum(var1, var2, var3)
print(f"The maximum value is {maximum}")
print(f"The minimum value is {minimum}")



def sum_list(lst):
    return sum(lst)


arr = [1,2, 34,4, 5,6 ,43]

print(f"The sum of {arr} is {sum_list(arr)}")
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
num = int(input("Enter the position in the Fibonacci sequence: "))
print(f"The {num}th Fibonacci number is {fibonacci(num)}")
