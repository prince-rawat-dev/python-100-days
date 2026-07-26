n = int(input("Enter a no.:"))

def table(a):
    i = 0
    while(i<10):
        print(a,"x",i+1,"=",a*(i+1))
        i =i+1

table(n)
