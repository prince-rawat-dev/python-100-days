def sum_numbers(*args):
    sum = 0
    for i in args:
        sum = sum +i
    # print("Sum of all the numbers is : ", sum)
    return sum

# sum_numbers(2,3,4,6,11,22)
print("Sum of all the numbers is : ",sum_numbers(2,3,4,5))