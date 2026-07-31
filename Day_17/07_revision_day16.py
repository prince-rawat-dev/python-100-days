# revision of day-16 (lec-24)(tuples)
# tuple slicing
tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
print(tup)

nes = tup[2:6]
print("nes:",nes)
nes1 = tup[6:2:-1]
print("nes1:",nes1)
nes2 = tup[::-1]
print("nes2:",nes2)
nes3 = tup[-1:-6:-1]
print("nes3:",nes3)
nes4 = tup[2:-2:2]
print("nes4:",nes4)
nes5 = tup[:5:2]
print("nes5:",nes5)
nes6 = tup[2:10:2]
print("nes6:",nes6)

# search city
city = ("delhi","NCR","dehradun")

new = input("Enter a city name: ")
if new in city:
    print("City Found")
else:
    print("Not Found")



# Tuple to list
# manual method
tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
print("its a tuple:",tup)
lst = []
for i in tup:
    lst.append(i)
print("tuple to list:",lst)

# direct method
# tup = (1,2,3,4,11,22,33,11,44,11,55,11,6,33,44,33,100)
# print("its a tuple:",tup)
# lst = list(tup)
# print("tuple to list:",lst)