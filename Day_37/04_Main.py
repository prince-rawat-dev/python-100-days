#  Now Properly making Reusable Module + Direct Testing
# File(Module used) is student_04.py

import student_04

marks = [98,90,88,77,45,59]

percentage = student_04.calculate_percentage(marks)
grade = student_04.calculate_grade(percentage)

print("Percentage:", percentage)
print("Grade:", grade)