# Program 5 — writelines() + readlines() Complete Cycle
# thing we use here - (list, writelines(), write mode, readlines(), read mode, for, enumerate(), strip(), with)
students = ["Prince\n",
            "Ravi\n",
            "Kishan\n",
            "Shankar\n"]

with open("students.txt","w",encoding = "utf-8")as f:
    f.writelines(students)

with open("students.txt","r",encoding = "utf-8")as file:
    file.readline()

print("Students List:")
for ginti, student in enumerate(students, start = 1):
    print(ginti, student.strip())