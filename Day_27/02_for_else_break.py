numbers = [11,22,33,44,55]
n= int(input("Enter no.: "))

for i in numbers:
    if (i == n):
        print("Number Found")
        break
else:
    print("Number Not Found")