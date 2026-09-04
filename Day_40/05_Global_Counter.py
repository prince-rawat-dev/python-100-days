# Practical Counter Program(combination of all programs of Day_40)
# Here you will learn that multiple functions can share and modify a global variable.


count = 1

def add_student():
    global count
    count = count + 1

    print("Student added")


def total_count():
    print("Total students:", count)

add_student()
add_student()
add_student()

total_count()