# "global" Keyword

count = 100

def increase_count():
    global count
    count = count + 1

    print("Inside function:", count)

print("Count value before function call:", count)

increase_count()

print("Count value after function call:", count)
