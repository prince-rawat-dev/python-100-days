# Program 4 — Extract Specific Information

# First we make .txt file to store data for this program:-
# lines = ["Prince, CSE, 90\n",
#              "Rahul, CSE, 75\n",
#              "Aman, IT, 88\n",
#              "Rohit, CSE, 92\n"]
# with open("student.txt","w",encoding = "utf-8")as file:
#     file.writelines(lines)

#     print("data stored")

# Main Program:-
with open("student.txt","r",encoding = "utf-8")as file:
    for line in file:
        if "CSE" in line:
            print(line.strip())