students = {
    "101": {
        "name": "Prince",
        "age": 20,
        "course": "CSE",
        "marks": 85
    },

    "102": {
        "name": "Alok",
        "age": 21,
        "course": "CSE",
        "marks": 90
    },

    "103": {
        "name":"Sagar",
        "age":22,
        "course":"BA",
        "marks":86
    }
}

print(f"\nwhole dictionary: {students}\n")
id = input("Enter the id no.: ")
if id in students:
    print(f"students information based on id you enter: {students[id]}")
else:
    print("Id not present")