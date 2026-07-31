import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp >= 00 and timestamp < 12):
    print("Good Morning Sir!")
elif(timestamp >= 12 and timestamp < 18 ):
    print("Good Afternoon Sir!")
elif(timestamp >= 18 and timestamp < 20):
    print("Good Evening")
else:
    print("Good Night Sir!")