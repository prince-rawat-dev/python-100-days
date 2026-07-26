# Calculator using (user defined function,match case, if-else)
n1 = int(input("Enter 1st no.: "))
n2 = int(input("Enter 2nd no.: "))
operator = input("Enter an operator(valid: +,-,*,/): ")

def add(a,b):
    sum = a+b
    print("Addition =",sum)

def subtract(a,b):
    diff = a-b
    print("Subtraction =",diff)

def multiply(a,b):
    product = a*b
    print("Multiplication =",product)

def divide(a,b):
    division = a/b
    print("Division =",division)

if operator in "+-*/":
    match operator:
        case "+":
            add(n1,n2)
        case "-":
            subtract(n1,n2)
        case "*":
            multiply(n1,n2)
        case "/":
            divide(n1,n2)
else:
    print("Invalid Operator!!!!!!!!!!!!!!")
