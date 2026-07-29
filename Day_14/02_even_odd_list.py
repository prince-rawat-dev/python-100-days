lst = [1,2,3,4,5,6,7,8]

even_lst = [i for i in lst if i%2 == 0]
odd_lst = [i for i in lst if i%2 != 0]
print(even_lst)
print(odd_lst)