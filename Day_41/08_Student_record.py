# File Based Student Record
# Its an integration challenge

name = input("Enter your name: ")
course = input("Enter your course: ")
marks = int(input("Enter your marks: "))

with open("student.txt", "a", encoding="utf-8") as file:
    file.write(f"Name: {name} | Course: {course} | Marks: {marks}\n")

print("\nStudent record added successfully.\n")

with open("student.txt", "r", encoding="utf-8") as file:
    data = file.read()

print("All Student Records:")
print(data)

# testing writelines():-
lines = ["Python\n", "Java\n", "C++\n"]

with open("langauge.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)