try:
    age = int(input("\nEnter your age: "))

    if(age<0 or age == 0):
        raise ValueError("Age neither can be negative nor zero")

except ValueError as e:
    print("Invalid Age:",e)

else:
    print(f"{age} is a valid age")

finally:
    print("Program Finished")
    

