# starting(lecture-25)(operations on tuples)
tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
print(tup)

n = int(input("Choose any one no. from this tuple: "))
freq = tup.count(n)
print("it comes",freq,"times")
        




# # lecture-25(operations on tuple)practice
# # conversion from tuple to list and vice-versa for manipulating tuple
# tup = ("Prince","alok")
# print(tup)

# # converting tuple to list
# lst = list(tup)
# lst.append("sagar")
# lst.pop(0)
# lst[1] = "ravi"

# # converting list to tuple 
# tup = tuple(lst)

# print(tup)


# # tuple indexing
# tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
# # indexing syntax = tuple.index(element, start,end)
# res = tup.index(11, 3,10)
# print(res)



# # tuple packing and unpacking
# # packing
# student = "Prince", 20, "CSE"
# print(student)
# # unpacking
# name, age, course = student
# # behind the scene python do this :
# # name = student[0]
# # age = student[1]
# # course = student[2]
# print(name)
# print(age)
# print(course)