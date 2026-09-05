# Create File Using x

try:
    with open("new_file.txt", "x", encoding="utf-8")as file:
        file.write("This file was created using (x) mode.")

    print("File Created successfully")

except FileExistsError:
    print("File already exists.")