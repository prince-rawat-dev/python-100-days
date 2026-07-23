# emulate Do-while in python (it will keep asking untill user enters zero, then it will print it one time like in Do{} and then go outside of while loop)
i = int(input("Enter a no. : "))
print(i)
while(i>0):
    i = int(input("Enter a no. : "))
    print(i)
else:
    print("Ohhhhhhhhh finally! the loop is over ")

