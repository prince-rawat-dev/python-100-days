lst = [2,3,2,5,6,5,22,7,8,7,22]
mlst = []
for i in lst:
    if i not in mlst:
        mlst.append(i)
print(mlst)
