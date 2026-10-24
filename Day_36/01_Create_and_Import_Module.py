# Starting (Day 36)Lecture - 44(How Importing Works in Python)
 
#  now we import (my_module) module here and use it

import my_module

print(my_module.name)
print(my_module.age)

my_module.greet()

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
result = my_module.add(n1,n2)
print(f"Result : {result}")





# Tranning :-
# importing module
# import math
# n = int(input("Enter any no.: "))
# result = math.sqrt(n)
# print("Result: ",result)

# importing module using from(used for specific calling):-
# from math import sqrt,pi
# n = int(input("Enter any no.: "))
# result = sqrt(n)
# result2 = sqrt(n)*pi
# print("Result: ",result)
# print("Result * pi: ",result2)

# rename module and methods and use :-
# import math as m
# result = m.sqrt(25)
# print(result)

# from math import pi , sqrt as s
# result = s(64)
# print(result*pi)
# print(result)

# dir function shows all methods presnt in math module:-
# import math 
# print(dir(math))

# kis function ka type dekhna hai example("nan" function):-
# import math
# print(math.nan, type(math.nan))

