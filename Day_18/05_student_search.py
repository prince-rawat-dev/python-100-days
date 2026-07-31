student = ("prince","alok","sagar")
name = input("Enter a student name: ")

if name in student:
    print("Student Found")
    print("It's index:",student.index(name))
else:
    print("Student Not Found")