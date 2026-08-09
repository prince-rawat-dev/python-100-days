student = {"prince":98,"alok":99,"ravi":95,"sagar":92}

def stud():
    name = input("Enter student name: ").lower()

    if name in student:
        print(f"His marks: {student[name]}")
    else:
        print("Student not found")
    stud()

stud()