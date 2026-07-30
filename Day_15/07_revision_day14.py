# 1.REVERSE LIST
lst = [2,3,4,5]
print(lst)

# using manual way
mlst = []
for i in range(len(lst)-1,-1,-1):
    mlst.append(lst[i])

print(mlst)


# using reverse() method
# lst.reverse()
# print(lst)


# 2.SEARCH Student
names = ["prince","alok","sagar"]
n = input("Enter yours friend name:")
if n in names:
    print("Student found")
else:
    print("Student not found")


# 3.LIST Comprehension Squares
lst = [2,3,4,5]

mlst = [i*i for i in lst]
print(mlst)


