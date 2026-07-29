lst = list(map(int, input("Enter numbers(giving spaces) for a list: ").split()))

square_lst = [i*i for i in lst]
print("Original list :",lst)
print("Squared list :",square_lst)