username = input("Enter username(contains only alpha ch.): ")
password = input("Enter password(contains alphanum ch. only): ")

if(username.isalpha() and password.isalnum()):
    print("Login Successful")

else:
    print("Invalid Username or Password")