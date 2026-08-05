# Before Recursion(means calling function before printing-
# thats means going downstairs first and print while coming upsatirs)
def countup(n):
    '''This function countup like (1,2,3,4,5)'''
    if n == 0:
        return

    else:
       countup(n-1)
       print(n)

print("\n---CountUp---\n")
countup(10)