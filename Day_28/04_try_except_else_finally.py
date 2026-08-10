try:
    n1 = int(input("\nEnter numerator: "))
    n2 = int(input("Enter denominator: "))

    result = n1/n2

except Exception as e:
    print("Error:",e)

else:
    print("Here(else:) you will get the result")
    print("Result:",result)

finally:

    print("Program Finished\n")