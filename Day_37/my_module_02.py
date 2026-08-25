# in python, we can't import a file/module whose name starts with a no. ,
# we make file with name (my_module_02.py) instead of (02_my_module.py).
 

print("my_module_02.py is running")

print("Value of __name__: ", __name__)

if __name__ == "__main__":
    print("my_module_02.py was executed directly")