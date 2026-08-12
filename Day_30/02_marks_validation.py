try:
    marks = int(input("\nEnter marks: "))
    if marks <0 :
        raise ValueError("Marks can't be negative")
    elif marks >100:
        raise ValueError("Marks cannot be greater than 100")

except ValueError as e:
    print("Error:",e)

else:
    print("Valid Marks")

finally:
    print("Program Finished\n")