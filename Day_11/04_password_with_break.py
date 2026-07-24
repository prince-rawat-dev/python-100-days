password = "something"

for string in password:
    password = input("Enter a password(contain 'python' and any 3 numbers): ")
    if(password == "python123"):
        print("Access Granted")
        break
    print(" It's wrong")