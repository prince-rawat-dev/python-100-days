students = {
    "Prince": 85,
    "Alok": 90,
    "Sagar": 78,
    "Ravi": 92
}

enter_name = input("Enter the name you want to find: ")
if enter_name in students:
    print("Student Found")
else:
    print("Student Not Found")