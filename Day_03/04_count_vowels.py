Name = input("Enter your name:")

count = 0

for letter in Name.lower():
    if letter in "aeiou":
        count = count + 1

print("Total vowels =", count)        