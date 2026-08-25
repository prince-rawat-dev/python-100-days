# this program depends on - (Why We Need if __name__ == "__main__")
# File(Module used) is Calculator_03.py

import calculator_03

print("Using calculator module")

n1 = int(input("Enter 1st no.:"))
n2 = int(input("Enter 2nd no.:"))

print("Addition:", calculator_03.add(n1,n2))
print("Multiplication:", calculator_03.multiply(n1,n2))