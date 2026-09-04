# Local vs Global Same Name
name = "Prince"

def show_name():
    name = "Alok"

    print("Inside function:", name)

show_name()

print("Outside function:", name)