# print sum from 1 to n (using recursion)

def sum_recursion(n):
    if(n == 0):
        return 0
    else:
        return n + sum_recursion(n-1)


print("\n---sum_n_recursion gives sum from 1 to n---\n")

print(f"\nif n = 0\n\nAnswer = {sum_recursion(0)}\n")
print(f"\nif n = 1\n\nAnswer = {sum_recursion(1)}\n")
# sum_recursion(2)
# sum_recursion(3)
# sum_recursion(4)
print(f"\nif n = 5\n\nAnswer = {sum_recursion(5)}\n")