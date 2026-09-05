# Starting (Day 41)Lecture - 49(File IO or file handling in Python)

# Basic File Write, it covers[open(),w,write(),text mode,with,newline,encoding]

with open("student.txt", "w", encoding = "utf-8")as file:
    file.write("Name: Prince\n")
    file.write("Course: B.Tech Cse\n")
    file.write("Language: Python\n")
    file.write("College: Saitm\n")
    file.write("Semester: 5th\n")
    file.write("Goal: Top Placement\n")

print("File written successfully.")