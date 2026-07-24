# emulate Do-while in python (it will keep asking untill user enters zero, then it will print it one time like in Do{} and then go outside of while loop using break)
# uses if-else here to eliminate negative vaule entered by user 
i = int(input("Enter a no. : "))
print(i)
if(i>=0):
 while(i>=0):
    i = int(input("Enter a no. : "))
    print(i)
    if(i == 0):
      break
else:
  print("This is not greater than zero")
