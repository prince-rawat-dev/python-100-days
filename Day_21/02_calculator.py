# Calculator(made of functions,(docstring and printing docstring), f-string)


print("\n====================\n  Calculator  \n====================\n")

def add(a,b):
    '''(This prints sum of two no.'s)'''
    print(add.__doc__)

    sum = a+b
    print(f"Addition : {sum}\n")

def subtract(a,b):
    '''(This prints difference of two no.'s)'''
    print(subtract.__doc__)

    difference = a-b
    print(f"Subtraction : {difference}\n")

def multiply(a,b):
    '''(This prints product of two no.'s)'''
    print(multiply.__doc__)

    multiplication = a*b
    print(f"Multiplication : {multiplication}\n")

def divide(a,b):
    '''(This prints division of two no.'s)'''
    print(divide.__doc__)

    division = a/b
    print(f"Division : {division}\n")


add(453,423)
multiply(200,25)
divide(8000,4)
subtract(80,45)
print("====================\n")

