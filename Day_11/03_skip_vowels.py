n = input("Enter a string: ")
for ch in n:
    if ch.lower() in "aeiou":
        continue
    print(ch)