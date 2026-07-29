lst = [2, 3, 4, 11, 22, 7, 99, 100]

reverse_lst = []
for i in range(len(lst)-1,-1,-1):
    reverse_lst.append(lst[i])

print("Original list :",lst)
print("Reversed list :",reverse_lst) 

