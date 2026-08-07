# Take 10 numbers from the user (store in a list) and convert to set and print that set(removed dulipcate values).

lst =  []

for i in range(10):
    lst.append(int(input(f"Enter number for {i+1}: ")))

lst_set = set(lst)

print(f"\nOriginal list: {lst}")
print(f"Unique Values: {lst_set}\n")