# Updated version of Exercise 2(Greet Good Morning/Afternoon/Evening/Night according to current time)




name = input("Enter your name: ")

import time
# hour = int(time.strftime('%H'))
hour = int(input("Enter any hour: "))

if(hour >= 00 and hour < 11):
    print("Good Morning",name)
elif(hour >= 12 and hour < 17):
    print("Good Afternoon",name)
elif(hour > 17 and hour < 20):
    print("Good Evening",name)
else:
    print("Good Night",name)
