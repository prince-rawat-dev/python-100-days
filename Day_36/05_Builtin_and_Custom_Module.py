# now we will use both built-in modules and own modules(my_module) here


import math
import random
import my_module

number = 25

print("\n----Using Bulit-In Module----")
print("Square root:", math.sqrt(number))
print("Random Number:", random.randint(1, 100))


print("\n----Using my own module----")
print("Name:", my_module.name)

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
print("Addition:", my_module.add(n1,n2))