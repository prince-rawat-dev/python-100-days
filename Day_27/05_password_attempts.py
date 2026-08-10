correct_password = "python123"
n =1
while(n<=3):
    n = n+1
    password = input("\nEnter password(it has (python) and any 3 no.'s): ")
    if password == correct_password:
        print("Correct Password")
        print("Login Successful\n")
        break
else:
    print("Account Locked\n")
        
