# Starting (Day 40)Lecture - 48(Local vs Global Variables in Python)

# Local Variable
# correct code:-
def student_details():
    name = "Prine"
    marks = 99

    print ("Name:", name)
    print ("Marks:", marks)

student_details()

# this will give error because its a local variable 
# print(name)