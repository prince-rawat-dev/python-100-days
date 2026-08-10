# Student Marks System(using try,except,raise,else,finally, for loop with else, if, break)
# This program combines Lecture 33 + 34 + 35 + 36.


students = {
    "Prince": 98,
    "Alok": 99,
    "Ravi": 95,
    "Sagar": 92
}

try:
    name = input("Enter student name: ")

    for key in students:
        if key.lower() == name.lower():
            name = key
            break
    else:
            raise KeyError(f"{name} not present in dictionary")

except KeyError as e:
    print("Key Error:",e)
# (OR)
# except Exception as e:
#     print("Error:",e)

else:
    print(f"Marks: {students[name]}")
    print(f"Percentage: {students[name]}%")

finally:
    print("Program Finished")

