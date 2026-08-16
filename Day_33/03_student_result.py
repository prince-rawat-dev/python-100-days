name = input("Enter your name: ")

try:
    marks = int(input("Enter your total marks(out of 100) : "))
    if marks <0:
        raise ValueError("Marks can't be negative")
    
except ValueError as e:
    print("Error:",e)

else:
    print("Valid marks")

    # assigning the result to a variable
    result = "Passed" if marks > 33 else "Failed"

    print(f"{name} has {result} the Exam.")
