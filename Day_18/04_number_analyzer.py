n=int(input("Enter a number:"))

# check even/odd
if(n%2==0):
    print(n,"is an even number")
else:
    print(n,"is an odd number")

# check no. is positive/negative/zero
if(n>0):
    print("it's positive")
elif(n==0):
    print("it's zero")
else:
    print("it's negative")

# divisible by 5
if(n%5==0):
    print("It's divisible by 5")
else:
    print("not divisible by 5")

# divisible by 10
if(n%10==0):
    print("It's divisible by 10")
else:
    print("not divisible by 10")