marks = {"maths":98,"physics":97,"chemistry":95,"CS":92}
print(marks.values())
total =0
for value in marks.values():
    total += value
print(f"Total Marks: {total}\n")
