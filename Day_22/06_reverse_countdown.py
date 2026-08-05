def reverse_countdown(n):
    if n == 0:
        return 0
    else:
        print(n)
        reverse_countdown(n-1)
        print(n)

print("\n---Reverse Countdown---\n")
reverse_countdown(10)