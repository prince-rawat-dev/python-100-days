students = ["Prince","Alok","Ravi","Sagar","Kishan","Shankar","Ganesh","Kartik"]

search = input("Enter student name: ")
for index, student in enumerate(students,start =1):
    if search.lower() == student.lower():
        print("Student Found")
        print(f"Position(index start from 1) of {student}: {index}")
        break
else:
    print("Student Not Found")
