# Mini project(mini ATM menu) - Rawat's ATM
print("\nWELCOME TO Rawat's ATM\n")
balance = 100000
print(" 1.Check Balance\n 2.Deposit\n 3.Withdraw\n 4.Exit")
choice = int(input("Enter you choice number: "))

match choice:
    case 1:
        print("Current Balance:",balance)
    case 2:
        amount = int(input("Enter the deposit amount: "))
        balance += amount
        print("Current Updated Balance:",balance)
    case 3:
        withdraw = int(input("Enter the amount you withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Current amount after withdraw:",balance)
        else:
            print("Insufficient Balance")
    case 4:
        print("Thank You For Visiting Rawat's ATM")
    case _:
        print("Invalid Choice")

