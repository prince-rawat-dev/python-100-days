# Read Line-by-Line
# Covers - [file iteration,for loop,read mode,strip(),large-file-friendly reading pattern]

with open("student.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
        # Why .strip()? :-
        # Without it, newline characters can create extra spacing.
        # strip() removes surrounding whitespace/newline.
