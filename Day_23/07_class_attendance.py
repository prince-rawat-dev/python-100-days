# present_students = {"prince","alok","sagar","ravi","mayank","kishan","angad"}
present_students = ["prince","alok","sagar","ravi","mayank","kishan","angad"]

enter = input("\nEnter Student Name: ")
if enter in present_students:
  print("Present\n")
else:
  print("Absent\n")