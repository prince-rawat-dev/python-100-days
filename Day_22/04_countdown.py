# After Recursion(means calling function after printing - 
# thats means going downstairs while Printing)
def countdown(n):
    '''This function countdown like (5,4,3,2,1)'''
    if n == 0:
        return
    else:
        print(n)
        countdown(n-1)

print("\n---Countdown---\n")
countdown(10)