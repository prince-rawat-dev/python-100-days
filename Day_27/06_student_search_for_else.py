students = {
    "Prince": 98,
    "Alok": 99,
    "Ravi": 95,
    "Sagar": 92
}

search = input("Enter student name you want to find: ").lower()
for name in students:
    if name.lower() == search:
        print("Student Found")
        print(f"Marks : {students[name]}")
        break
else:
    print("Student Not Found")
