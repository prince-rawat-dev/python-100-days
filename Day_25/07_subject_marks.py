marks = {
    "Maths": 85,
    "Physics": 78,
    "Chemistry": 90,
    "English": 88,
    "CS": 95
}

subject = input("\nEnter any subject: ")
if subject in marks:
    print(f"Marks : {marks[subject]}\n")
else:
    print("subject not present\n")