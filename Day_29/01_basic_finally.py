# Lecture - 37("finally" keyword(a short topic from lecture - 36))

try:
    n = int(input("Enter a number: "))
    print(100/n)
except ZeroDivisionError:
    print("Zero se divide nhi ho sakta")
finally:
    print("Program Finished")