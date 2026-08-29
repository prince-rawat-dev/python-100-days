# work of (os.mkdir(),
# os.makedirs(),
# os.path.exists(),
# os.path.isdir()) function in os module.

# this program creates (Practice_Folder)


# creating Single folder:-
import os

folder_name = "Practice_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully")
else:
    print("folder already exists")

print("Exists:", os.path.exists(folder_name))
print("Is directory:", os.path.isdir(folder_name))


# creating nested folders or multiple folders:-
import os

folder_path = os.path.join("practice_folder","python","OS_Module")

os.makedirs(folder_path, exist_ok=True)

print("Nested folders created.")
print("Exists:", os.path.exists(folder_path))