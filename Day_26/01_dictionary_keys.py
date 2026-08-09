# Starting lecture - 34(dictionary methods)
student = {"name":"prince","roll":21,"marks":99,"college":"saitm"}
print(student.keys())
for key in student.keys():
    print(key)



# # practice - lecture - 34(dictionary methods)
# # first dict basics: -
# # dict accessing
# ep1 = {111 : 91,112 : 92,113 : 93}
# print(ep1[112])
# print(ep1.get(113))
# # for accesing multiple value 
# # for keys
# print(ep1.keys())
# # for values
# print(ep1.values())
# # accessing vlaues using iteration
# for keys in ep1.keys():
#     print(ep1[keys])
# # for both keys and values
# print(ep1.items())
# # accessing keys, values using iteration
# for key, value in ep1.items():
#     print(key, value)
# # adding key and value
# ep1[114] = 94
# print(ep1)
# # updateing key and value
# ep1[113] = 95
# print(ep1)
# # use of (in)
# print(114 in ep1) 
# print(116 in ep1) 
# # nested dictonary
# student = {"student1" : {"name" : "prince","marks" : 99},
#            "student2" : {"name":"alok","marks" : 98}}
# print(student)
# print(student["student1"]["marks"])
# print(student["student2"]["marks"])