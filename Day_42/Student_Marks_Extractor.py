# Mini Challenge:-

# Program ko:
# 1. File read karni hai
# 2. Loop use karna hai
# 3. Har student ka naam aur marks extract karna hai
# 4. Sirf 80+ marks wale students print karne hain

# this code is to update add marks with name present in students.txt file:-
# with open("students.txt","r",encoding = "utf-8")as file:
#     lines = file.readlines()
# with open("students.txt","w",encoding = "utf-8")as file:
#     for line in lines:
#         name = line.strip().split(",")[0]

#         if name == "Prince":
#             file.write("Prince,90\n")
#         elif name == "Ravi":
#             file.write("Ravi,65\n")
#         elif name == "Kishan":
#             file.write("Kishan,82\n")
#         elif name == "Shankar":
#             file.write("Shankar,45\n")

#         else:
#             file.write(line)

# Main challenge code:-
with open("students.txt","r",encoding = "utf-8")as file:
    lines = file.readlines()

    for line in lines:
        name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 80:
            print("Students with good marks:")
            print(name,marks)
# with open("students.txt","w",encoding)
