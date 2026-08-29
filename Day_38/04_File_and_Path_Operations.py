# work of ([os.path.join() - (join paths)],
# [os.path.abspath() - (gives absolute path like(C:\Users\Prince\...\Day_38\data.txt))],
# [os.path.basename() - (gives base name like(test.py))],
# [os.path.dirname() - gives directory name or its path name like(C:\Projects\Python)],
# [os.path.splitext() - split text like(name = report, extension = .pdf))] function in os module.

# its useful in handling path in REAL Projects

import os

file_name = "sample.txt"

with open(file_name, "w") as file:
    file.write("This is an OS module Practice file.")

print("File Exists:", os.path.exists(file_name))
print("Is File:", os.path.isfile(file_name))
print("Is directory:", os.path.isdir(file_name))

print("Absolute path:", os.path.abspath(file_name))
print("File name:", os.path.basename(os.path.abspath(file_name)))
print("Directory name:", os.path.dirname(os.path.abspath(file_name)))

name, extension = os.path.splitext(file_name)

print("Name:", name)
print("Extension:", extension)