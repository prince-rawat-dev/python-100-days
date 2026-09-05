# Append Data

with open("student.txt", "a", encoding="utf-8") as file:
    file.write("\nPlacement Goal: Top Product Company")

print("Data appended successfully.")