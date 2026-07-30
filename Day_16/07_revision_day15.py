# STUDENT Manager
student = ["prince","alok","aniket"]
print(student)

student.append("sagar")
print(student)

student.remove("aniket")
print(student)

# UNIQUE numbers
lst = [2,3,2,5,6,5,22,7,8,7,22]
mlst = []

for i in lst:
    if i not in mlst:
      mlst.append(i)

print(mlst)


# TUPLE Slicing
tup = (11,22,33,44,55,66,77,88,99,100)
print(tup)

tup2 = tup[:5]
tup3 = tup[-5:]
tup4 = tup[::-1]
print(tup2)
print(tup3)
print(tup4)
