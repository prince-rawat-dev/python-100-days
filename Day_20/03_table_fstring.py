a = int(input("Enter first number: "))

print(f"\n--Table of {a}--")
for i in range(10):
    print(f"{a} x {(i+1)} = {a * (i+1)}")