# Mini Validation System("using functions,if-elif, try,except,else,raise,finally")

try:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))
    if age <4:
        raise ValueError("Age can't be less than 4")
    elif marks <0 or marks >100:
        raise ValueError("Marks can't be negative or greater than 100")
    elif ' ' in name:
        raise ValueError("Name should not contain any space")
    elif name ==  "":
        raise ValueError("Name should not be empty")
except ValueError as e:
    print("Error:",e)
else:
    print("Yes, This student is valid")
finally:
    print("Program Finished")
    

    