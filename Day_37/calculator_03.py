def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b


print("\nValue of __name__:", __name__)

if __name__ == "__main__":
    print("Calculator Test")

    n1 = int(input("Enter 1st no.:"))
    n2 = int(input("Enter 2nd no.:"))
    print("Addition:", add(n1,n2))
    print("Subtraction:", subtract(n1,n2))
    print("Multiplication:", multiply(n1,n2))
    print("Division:", divide(n1,n2))
    
