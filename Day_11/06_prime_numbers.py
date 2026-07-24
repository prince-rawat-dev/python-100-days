# Bonus program
n = int(input("Enter a no.(greater than 1) to check its prime or not: "))
for i in range (2 , n):
    if(n % i == 0):
        print("Not a prime")
        break
else:
    print("Gotchaaa! , it's a prime")
