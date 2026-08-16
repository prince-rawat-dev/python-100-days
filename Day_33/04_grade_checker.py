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
    grade = "Excellent" if marks >= 90 else "Good" if marks >= 60 else "Pass" if marks >= 33 else "Fail"

    print(f"Grade of {name}: {grade}")