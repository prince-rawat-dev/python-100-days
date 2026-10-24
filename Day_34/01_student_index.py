# Starting lecture - 42(Enumerate Function)
students = ["Prince","Alok","Ravi","Sagar"]

for index, student in enumerate(students):
    print(f"{index} -> {student}")





# Practice lecture 42
# enumerate function example with start index
# n = ["A", "B", "C"]
# for index, value in enumerate(n, start = 1):
#     print(index, value)



# tranning :-

# students = ["prince","alok","ravi","kishan","ram"]
# for index,student in enumerate(students, start = 1):
#     # if index == 3:
#     #     print("here is my index")
#     print(f"{index} --> {student}")
#     if index == 3:
#             print("here is my index")



# another example
# students = ["prince","alok","ravi","kishan","ram"]
# letter = ["a","b","c","d","e"]
# for index,student in enumerate(students):
#     print(f"{student} --> {letter[index]}")


# searching using enumerate
# students = ["prince","alok","ravi","prince","kishan","ram","prince"]
# name = input("enter one name: ")

# for index,student in enumerate(students,start=1):
#     if student == name:
#         print("student found!")
#         print(f"at index: {index}")
#         break
#     # break for loop ke ander if ke ander lagate hai
#     # agr break for pe laga to else nhi chalega
# else:
#     print("not found")

# real world menu/list numbering:-
#  - without enumerate, by normal:-
# menu = ["Add","remove","search","exit"]
# for i in range (len(menu)):
#     print(i+1,menu[i])

# - with enumerate:-
# menu = ["Add","remove","search","exit"]
# for i,option in enumerate(menu, start=1):
#     print(i,option)

# enumerate with string,letter and other iterables
# values = "python"
# values = ("os","dbms","ai","aiml")
# for i,value in enumerate(values,start=1):
#     print(i,value)


              
