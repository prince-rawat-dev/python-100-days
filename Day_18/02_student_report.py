marks = [20,40,60,80,100]
sum = 0
for i in marks:
    sum += i
print("Total marks:",sum)

average = sum/len(marks)
print("Average:",average)

high = marks[0]
for i in marks:
    if(i>high):
      high = i
print("Highest:",high)

low = marks[0]
for i in marks:
   if(i<low):
     low = i
print("Lowest:",low)

if(average >= 40):
   print("Pass")
else:
   print("Fail")
