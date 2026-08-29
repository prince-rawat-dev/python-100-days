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