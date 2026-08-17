students = ["Prince","Alok","Ravi","Sagar","Kishan","Shankar","Ganesh","Kartik"]
marks = [98, 99, 95, 92, 100, 100, 100, 100]

for index, student in enumerate(students, start = 1):

    # in this print - in marks[index] , the index here always default(means start from 0)
    print(f"{index}. {student} -> {marks[index-1]}")