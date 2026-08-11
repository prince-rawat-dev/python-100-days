try:
    n1 = int(input("Enter numerator: "))
    n2 = int(input("Enter denomerator: "))
    result = n1/n2
except ZeroDivisionError:
    print("Zero se divide nhi ho sakta")

else:
    print("if error -> except runs (OR) if no error -> else runs")
    print("Result:",result)
    
finally:
    print("Program Finished")