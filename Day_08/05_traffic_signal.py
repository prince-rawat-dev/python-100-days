n = input("Enter the traffic signal colour: ")

match n:
    case "red":
        print("Stop Please")
    case "yellow":
        print("Ready To GO")
    case "green":
        print("Gooooooooooooooooooooo")
    case _:
        print("Invalid Signal")