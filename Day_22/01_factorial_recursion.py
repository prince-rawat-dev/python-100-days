# Starting Lecture - 30(Recursion)
# Using Recursion - find factorial
def factorial(n):
    '''\nGenerates Factorial\n'''

    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print("\n---Factorial---\n")
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))




# practice lec- 30 , Using Recursion - find a particular no. at index = n in Fibonacci Sequence
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("\n---Fibonacci Sequence---\n")
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))


