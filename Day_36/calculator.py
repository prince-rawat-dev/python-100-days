# It is for Program 6

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't be divided by 0")
    return a/b