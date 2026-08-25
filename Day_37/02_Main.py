import my_module_02
# After importing my_module_02 the (__name__) inside my_module_02.py file,
# it will give(my_module_02) because python assume my_module_02 as a module 
# after importing it, so (__name__) of my_module_02.py was being executed from 
# that my_module_02 module so it gives my_module_02 .

print("Main file is running")

# this will give (__main__) because it is directly running from this file
print("Value of __name__:", __name__)