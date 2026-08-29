# work of (listdir()) function in os module.
# it gives list of files or folders from your main directory thats opened in VScode - means Python-Practice


import os

items = os.listdir()

print("\nFiles and folders:")

for item in items:
    print(item)




# a new experiment:- 
items = os.listdir(".")
# here this - listdir(".") also do same work as listdir()

for item in items:
    print(item)
