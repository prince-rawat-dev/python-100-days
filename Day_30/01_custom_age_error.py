# Lecture - 37(rasing custom errors("raising" keyword(a short topic from lecture - 36))

try:
    age = int(input("Enter any age: "))
    if age <0 or age == 0:
        raise ValueError("Age can't be zero or negative")

except ValueError as e:
    print("Error:",e)

else:
    print("Its a valid Age")

finally:
    print("Program Finished")
