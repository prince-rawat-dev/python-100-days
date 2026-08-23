# Now we import (my_module) module here and use it
# And we use (as) for renaming module and for renaming function and variables

# for renaming module:-
import my_module as mm

print(f"Name: {mm.name}")
print(f"Age: {mm.age}")

mm.greet()

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
print("Addition:",mm.add(n1,n2))



# for renaming functions and varibales
from my_module import add as addition

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
print("Addition:",addition(n1,n2))
