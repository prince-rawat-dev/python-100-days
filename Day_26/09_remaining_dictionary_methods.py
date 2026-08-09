# Extra — setdefault(), copy(), fromkeys()
# setdefault() :-

student = {"name": "Prince"}

student.setdefault("age", 20)
print(f"\nUsing setdefault() : {student}")

# copy() :-

new_student = student.copy()
print(f"Using copy() : {new_student}")

# fromkeys() :-
new = dict.fromkeys(student)
print(f"Using fromkeys() : {new}")
new = dict.fromkeys(student,"Not Given")
print(f"Using fromkeys() : {new}\n")