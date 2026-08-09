employee = {"name":"prince","course":"CS","College":"saitm","age":21}
key = input("Enter key to remove: ")

if key in employee:
    removed = employee.pop(key)
    print(f"Removed information: {removed}")
else:
    print("key not found")

print(employee)
