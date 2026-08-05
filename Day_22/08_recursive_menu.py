# Recursive Menu

# for factorial of n
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
    

# for sum upto n
def sum_recursion(n):
    if(n==0):
        return 0
    else:
        return n + sum_recursion(n-1)

# for power finding
def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base,exponent-1)

def menu():
    print("\n--MENU--\n1. Factorial\n2. Sum\n3. Power\n4. Exit")
    n = int(input("Enter the no.(out of 1,2,3,4) you want from this menu: "))
    match n:
        case 1:
            n1 = int(input("Enter the number for factorial: "))
            print(f"Factorial of {n1}:",factorial(n1))
        case 2:
            n2 = int(input("Enter the number up to which you need sum: "))
            print(f"Sum upto {n2}:",sum_recursion(n2))
        case 3:
            base = int(input("Base value: "))
            exponent = int(input("Exponent value: "))
            print("Value of power:",power(base,exponent))
        case 4:
            print("\nThankyou\n")
            exit
    menu()

menu()

