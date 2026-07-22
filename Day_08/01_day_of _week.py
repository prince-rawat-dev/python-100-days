n = int(input("Enter the day no. you want: "))

match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")




# Just lecture 16(match case) practice

# x = int(input("Enter value of x: "))

# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("x is 4")
#     case _ if (x>=0 and x<=50):
#         print("x is less than 51")
#     case _ if x>50:
#         print("x is greater than 50")
#     case _ if x<0:
#         print("x is a negative value")