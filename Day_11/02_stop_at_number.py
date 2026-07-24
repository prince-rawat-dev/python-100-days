n = int(input("Enter a no. (under 100) till you want numbering from 1: "))
i = 1
for i in range(100):
    i = i + 1
    print(i)
    if(i == n):
        break