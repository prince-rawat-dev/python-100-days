# Dictionary Toolkit(Dictionary Management)

student = {"1":"prince","2":"alok","3":"sagar","4":"ravi","5":"kishan"}
while True:
  print("""\n----- Dictionary Management -----\n
  1. Show Keys
  2. Show Values
  3. Show Items
  4. Search using get()
  5. Update Data
  6. Remove Data
  7. Remove Last Item
  8. Clear Dictionary
  9. Exit""")
  choice = int(input("Enter Choice number: "))
  match choice:
    case 1:
      print(student.keys())

    case 2:
      print(student.values())

    case 3:
      print(student.items())

    case 4:
      key = input("Enter key value: ")
      if key in student:
        print("Key Found")
      else:
        print("Key Not Found")

    case 5:
      key = input("Enter key you want to add: ")
      value = input("Enter value of that key: ")
      student.update({key:value})
      print(f"Dict after update : {student}")

    case 6:
      key = input("Enter the key you want to remove: ")
      removed = student.pop(key)
      print(f"Removed Information: {removed}")

    case 7:
      student.popitem()
      print(f"student after last item removed: {student}")

    case 8:
      student.clear()
      print(f"student dict after clearing all items: {student}")

    case 9:
      print("Thank-You!")
      break

    case _:
      print("Invalid choice")
    
