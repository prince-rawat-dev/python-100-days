# Program 3 — Directly Extract Content Using Loop
# (This pattern is usefull in large file in future even better then readlines())
with open("data.txt","r",encoding = "utf-8")as file:
    for line in file:
        print(line.strip())
