# Read Entire File
# Covers -[r, read(), reading complete file, with]

with open("Student.txt", "r")as file:
    data = file.read()

print(data)