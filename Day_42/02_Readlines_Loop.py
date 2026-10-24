# Program 2 — readlines() + Loop
# (first readlines se data nikalna jo ki list form mai hoga then osse
# loop ki help se har ek line print karna):-
with open("data.txt","r",encoding = "utf-8")as file:
    lines = file.readlines()

print("Data of .txt file:")
for line in lines:
    print(line.strip())
