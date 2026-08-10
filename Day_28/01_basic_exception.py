# Starting Lecture - 36(Exception Handling)

n1 = int(input("\nEnter numerator: "))
n2 = int(input("Enter denominator: "))

try:
    print(n1/n2)
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte")
    
print("Program Finished\n")