# Bonus Program(Student Report)

name = input("Enter your name: ")

# taking marks - method 1(manual method)
physics = int(input("Enter your Physics marks: "))
maths = int(input("Enter your Maths marks: "))
chemistry = int(input("Enter your Chemistry marks: "))
english = int(input("Enter your English marks: "))
cs = int(input("Enter your CS marks: "))

# taking marks - method 2(using list)
# marks = []

# for i in range(5):
#     marks.append(int(input(f"Enter marks of subject {i+1}: ")))

total = physics + maths + chemistry + english + cs
average = total/5
print(f"\n--Student Report--\nTotal = {total}\nAverage : {average}\n")

