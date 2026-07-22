# Bonus Challenge
n = input("Enter the Grade you got:")

match n:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Need Improvement")
    case _:
        print("Invalid Grade")