# No common subjects(using isdisjoint())

student_A_subjects = {"maths","physics","chemistry"}
student_B_subjects = {"accounts","GK","bussiness","economics"}

print(f"\nStudent A Subjects: {student_A_subjects}\nStudent B Subjects : {student_B_subjects}")

if(student_A_subjects.isdisjoint(student_B_subjects) == True):
  print(f"\nNo common subjects\n")
else:
  print(f"\nCommon subjects exist\n")
  