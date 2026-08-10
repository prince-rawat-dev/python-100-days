try:
    n1 = int(input("\nEnter numerator: "))
    n2 = int(input("Enter denominator: "))

    print(n1/n2)
except Exception as e:
    print("Error:",e)
    
print("Program Finished\n")