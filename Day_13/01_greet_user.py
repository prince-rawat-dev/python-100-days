# Starting Lecture - 21(Function Agrument) practice
def greet(name,city):

    print("Hello,", name, " Welcome to", city + "!")

greet("Prince", "Delhi NCR")
       








# simple function making(from previous lecture)
# # def calculate_sum(a =1,b=4):
# #     sum = 0
# #     sum = a +b
# #     print(sum)

# # calculate_sum(b =2)

# # keyword agrument(means if you give (key/variable = value), then order doesn't matter)
# # def average(a=1,b=4):
# #     print("Average is:", (a+b)/2)

# # average(b =8,a=6)

# # Variable - length argument(1st type - Arbitary Argument) - (argument in form of tuple(*Argument_name))
# def average(*num):
#     sum =0
#     for i in num:
#         sum = sum +i
#     print("Average is:",sum/len(num))

# average(2,3,4,5,6)

# - variable - length argument(another example of 1st type)
# def name(*name):
#     print("Hellooooo!!!!,",name[0],name[1],name[2])

# name("Prince","Singh","Rawat")


# Variable - length argument(2st type - Keyword Arbitary Argument) - (argument in form of dictionary(**Argument_name))
# def name(**name):
#     print("Hellooooo!!!!,",name["fname"],name["mname"],name["lname"])

# name(lname = "Rawat", mname = "Singh", fname = "Prince")


# Return Statement Example(how to use return instead of print)
# def vname(fname,mname,lname):
#     # print("Heyyyyy!!!!,",fname,mname,lname)
#     # (OR)
#     return "Heyyyy!!!!!!!!!!!!! " + fname + " " + mname + " " + lname
# c = vname("Prince","Singh","Rawat")
# print(c)


