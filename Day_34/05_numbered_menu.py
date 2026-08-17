# Menu/List Numbering(Using = enumerate function, exception handling , if-elif-else, for loop)



students = [
    "Prince", "Alok", "Ravi", "Sagar",
    "Kishan", "Shankar", "Ganesh", "Kartik"
]

menu = [
    "Add Student",
    "Remove Student",
    "Search Student",
    "Show Students",
    "Exit"
]

print("\nStudents list:", students)


def Menu():

    while True:

        print("\n---------- MENU ----------")

        for index, option in enumerate(menu, start=1):
            print(f"{index}. {option}")

        try:
            choice = int(input("Enter your choice no.: "))

            if choice < 1 or choice > len(menu):
                raise ValueError("Invalid Choice! Please enter a number from 1 to 5.")

        except ValueError as e:
            print("Error:", e)
            continue

        else:
            print("It's a valid choice\n")


        # Add Student
        if choice == 1:

            student = input("Enter student name to add: ")

            students.append(student)

            print("Student Added Successfully!")
            print("Students:", students)


        # Remove Student
        elif choice == 2:

            student = input("Enter student name to remove: ")

            if student in students:
                students.remove(student)

                print("Student Removed Successfully!")
                print("Students:", students)

            else:
                print("Student Not Found")


        # Search Student
        elif choice == 3:

            search = input("Enter student name to search: ")

            for index, student in enumerate(students):

                if search.lower() == student.lower():

                    print("Student Found!")
                    print(f"Index(default indexing): {index}")
                    print(f"Student Name: {student}")

                    break

            else:
                print("Student Not Found")


        # Show Students
        elif choice == 4:

            print("\n---------- STUDENTS ----------")

            for index, student in enumerate(students, start=1):
                print(f"{index}. {student}")


        # Exit
        elif choice == 5:

            print("\nThank-You!!!")
            print("Program Finished.")

            # return
            # OR
            break


Menu()


