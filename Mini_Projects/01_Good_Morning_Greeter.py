# Mini Project 01
# Greeting(Greet Good Morning/Afternoon/Evening/Night according to current time)
# Built using Python Fundamentals



name = input("Enter your name: ")
import time
timestamp = int(time.strftime('%H'))
print("It's",timestamp)

if(timestamp >= 00 and timestamp < 12):
    print("Good Morning!",name)
elif(timestamp >= 12 and timestamp < 18 ):
    print("Good Afternoon!",name)
elif(timestamp >= 18 and timestamp < 20):
    print("Good Evening!",name)
else:
    print("Good Night!",name)