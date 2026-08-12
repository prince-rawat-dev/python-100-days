# Custom Validation Function(using functions,if-elif, try,except,else,raise,finally)

def validate_username(username):
    try:
       username = input("Enter Username: ")
       if len(username) <5:
           raise ValueError("Username must contain at least 5 characters")
       elif ' ' in username:
           raise ValueError("Username should not contain any space")
    except ValueError as e:
        print("Error:",e)
    else:
        print("Username is valid")
    finally:
        print("Program Finished")

validate_username("Prince")
