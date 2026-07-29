# revision of factorial
n = int(input("Enter a no. for factorial: "))
fact = 1
i = 1
while(i<=n):
    fact = fact *i
    i = i+1
print ("its factorial is", fact)


# revision of multiplication table
n = int(input("Enter a no. for table making: "))
i = 0
while(i<10):
    i += 1
    print(n ,"x",i, "=", n*i)


# revision of calculator(using match case)
n1 = int(input("Enter a 1st no. : "))
n2 = int(input("Enter a 2nd no. : "))
operator = input("Enter an operator(valid only = =,-,*,/): ")

if operator in "+-*/":
    match operator:
        case "+":
            print("additon: ", n1+n2)
        case "-":
            print("subtraction: ", n1-n2)
        case "*":
            print("multiplication: ",n1*n2)
        case "/":
            print("division: ", n1/n2)

else:
    print("Invalid Operator")
