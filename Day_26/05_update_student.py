student = {"name":"prince","course":"CS","College":"saitm"}
s_key = input("Enter key(string): ")
s_value = int(input("Enter new value(int): "))

# update() ko key-value pair ek dictionary/form me dena hota hai.
student.update({s_key:s_value})
print(student)