# Now we import (my_module) module here and use it
# And here we import specific functions and variables from module not the whole module
# Here we will see the difference of requirement Dot notation  

from my_module import name, age, greet, add

print(f"Name: {name}")
print(f"Age: {age}")

greet()

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))
result = add(n1,n2)
print(f"Result : {result}")