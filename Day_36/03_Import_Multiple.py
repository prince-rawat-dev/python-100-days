# Now we import (my_module) module here and use it
# And here we import specific functions and variables from module not the whole module
# And we will use (*) for importing multiple function of a module

# first importing specific ones:-
from my_module import name,add

print(f"Name: {name}")

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
print("Addition:", add(n1,n2))


# second importing using (*):-
from my_module import *

print(f"Name: {name}")
print(f"Age: {age}")

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
print("Addition:", add(n1,n2))
