lst = [87,89,76,98,99,78]
highest = lst[0]
lowest = lst[0]
sum = 0
average = 0
for i in lst:
    if(i>highest):
        highest = i
print("Highest number is",highest)

for i in lst:
    if(i<lowest):
        lowest = i
print("Lowest number is",lowest)

for i in lst:
    sum += sum +i
print("Total marks:",sum)

for i in lst:
    average = sum/len(lst)
print("Average Marks:",average)
