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
    

    # trannning
# exception handling inside functions
# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Can't divide by zero")
#     else:
#         print("Result:",result)
#     finally:
#         print("Program finished")

# print(divide(100,2))
# print(divide(25,0))

# raising custom errors
# def division(a,b):
#     b = int(input("Enter any number: "))
#     try:
#         # result = a/b
#         if b == 0:
#             raise ZeroDivisionError("Can't divide by zero")
#         if b>9 or b<0:
#             raise ValueError("dekhlo bhai, Value should be between 0-10")
#         result = a/b
#     except Exception as e:
#         print("Error:",e)
#     else:
#         print("Result is :",result)
#     finally:
#         print("Program is finished")

# print(division(100,0))

# short hand if-else:
# 1.Temporary operator expression
# a=300
# b=350
# print("A")if a>b else print("po") if a==b else print("No")

# print(9)if a>b else print("@")
# c = 100 if a<b else 0
# print(c)

# # 2.assigning the result to a variable
# greater = a if a>b else b
# print("Greater:",greater)

# # 3.Printing directly
# age = 21
# print("Eligible to vote" if age > 18 else "Not Eligible to vote")

# # 4.nested/Combined short-hand expression
# marks =99
# result = "Excellent" if marks>=80 else "Good" if marks >=60 else "needs improvment"
# print(result)