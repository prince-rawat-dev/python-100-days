def calculate_percentage(marks):
    total = sum(marks)
    percentage = total/len(marks)
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A++"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

print("\nValue of __name__:", __name__)

if __name__ == "__main__":
    marks = [78,45,68,90,34,88]
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("Percentage:", percentage)
    print("Grade:", grade)
