# age_checker
age = int(input("Enter your age: "))

if(age>0 and age<18):
    print("minor")
elif(age>=18 and age<60):
    print("Adult")
elif(age>=60 and age<=150):
    print("senior citizen")
elif(age<0 or age>150):
    print("Invalid age")
else:
    print("zero is not an age")






# n = int(input("Enter any integer no.: "))

# # if(n>=1):
# #     print(f"{n} is a natural no. and a whole no.")
# # elif(n==0):
# #     print(f"{n} is a whole no. but not a natural no.")
# # elif(n<0):
# #     print(f"{n} is a negative no.")
# # else:
# #     print(f"{n}is not a valid no.")


# if(n<0):
#         print("number is negative")
# elif(n>0):
#         if(n<=10):
#             print("number is in between 1 - 10")
#         elif(n>=11 and n<21):
#             print("number is in between 10 - 21")
#         else:
#             print("number is greater than 20")
# else:
#         print("number is zero")