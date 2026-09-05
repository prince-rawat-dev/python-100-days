# readline() and readlines()

with open("student.txt", "r", encoding="utf-8")as file:
    first_line = file.readline()
    # now first line readed

    # now, for reading remaining lines:-
    remaining_lines = file.readlines()

    # This is because - "reading position" of file moves
    # means "remaining_lines = file.readlines()" will read only remaining lines

print("First line:", first_line)
print("Remaining lines:", remaining_lines)