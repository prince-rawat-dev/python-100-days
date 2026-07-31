tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
print(tup)

n = int(input("Enter a no.: "))
if n in tup:
    print(tup.index(n))
else:
    print("Not Found")