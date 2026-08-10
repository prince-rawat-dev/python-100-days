try:
    n1 = int(input("\nEnter a no.: "))
    print(100/n1)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program Finished\n")