# n = int(input("Enter a no. for its table: "))
def table(n):
    '''\n---This prints the table---\n'''
    print(table.__doc__)

    for i in range(10):
        print(f"{n} x {i+1} = {n*(i+1)}")

table(7)