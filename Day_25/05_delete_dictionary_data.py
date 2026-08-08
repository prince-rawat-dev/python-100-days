info = {"name":"Prince","age":20,"city":"gurugram","course":"CSE"}

print(f"\ndictionary before deleting items: {info}\n")
del info["city"]
print(f"\ndictionary before deleting items: {info}\n")
del info["helth"]
print(info)
