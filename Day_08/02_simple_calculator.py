n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Enter operator(allowed : +,-,*,/):")

match operator:
    case "+":
        print("sum is",n1+n2)
    case "-" :
        print("subtraction is",n1-n2)
    case "*" :
        print("multiplication is",n1*n2)
    case "/" :
        print("division is",n1/n2)
    case _ :
        print("Invalid Operator")