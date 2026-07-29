# practice default argument
def details(name, age, course = "CSE"):
    print("Hello!!!,", name + ",", "your age is",age,"and your course is",course)

details("prince",20)
details("prince",20, "AIML")