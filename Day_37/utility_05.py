# Final Mini Project: Utility Module

def is_even(number):
    return number % 2 == 0

def square(number):
    return number * number

def maximum(a,b):
    return max(a,b)

def minimum(a,b):
    return min(a,b)

def show_result(number):
    print("Number:", number)
    print("Is even:", is_even(number))
    print("Square:", square(number))


print("\nValue of __name__:", __name__)


if __name__ == "__main__":
    print("Using Utility Module")

    number = int(input("Enter a no.: "))

    show_result(number)

    print("Maximum:", maximum(78,23))
    print("Minimum:", minimum(2345,6562))