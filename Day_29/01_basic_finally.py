try:
    n = int(input("Enter a number: "))
    print(100/n)
except ZeroDivisionError:
    print("Zero se divide nhi ho sakta")
finally:
    print("Program Finished")