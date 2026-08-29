# work of [(os.rename(old_name, new_name)) - {rename file name},
# (os.remove() - {remove file},
# (os.rmdir()) - {remove empty directory] function in os module.

# its useful to remove file/folders in REAL Projects

# Using rename function:-
import os

old_name = "old_file.txt"
new_name = "new_file.txt"

with open(old_name, "w") as file:
    file.write("testing rename operation")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully")

if os.path.exists(new_name):
    print("New file exists")

os.remove(new_name)

print("File removed successsfully")


# Empty folder removal:-
folder = "temporary_folder"

if not os.path.exists(folder):
    os.mkdir(folder)

if os.path.isdir(folder):
    os.rmdir(folder)
    print("Folder removed successfully")

