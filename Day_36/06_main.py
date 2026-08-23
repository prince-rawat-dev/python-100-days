# now we import (calculator) module here and use it
# Calculator Menu (this programs is made up of while True,
# import module, match case, try-except, break)

import calculator

while True:
    print("\n----Using Calculator----")
    print(
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Exit\n"
    )

    n1 = int(input("Enter 1st no.:"))
    n2 = int(input("Enter 2nd no.:"))
    select = int(input("Select the operation no.(out of 1 to 5) you want to perform: "))


    match select:
        case 1:
            print("Addition:", calculator.add(n1,n2))

        case 2:
            print("Subtraction:", calculator.subtract(n1,n2))

        case 3:
            print("Multiplication:", calculator.multiply(n1,n2))

        case 4:
            try:
                print("Division:", calculator.divide(n1,n2))
            except Exception as e:
                print("Error:",e)
        case 5:
            print("\n----(Thank-You)----\n")
            break
        case _:
            print("Invalid Selection")
