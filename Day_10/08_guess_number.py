n = int(input("Guess any no. from between 1 - 20: "))
if(n>0 and n<=20):
    while(n != 7):
        n = int(input("Guess any no. from between 1 - 20: "))
    else:
        print("Congratulations! You guessed correctly.")
else:
    print("The no. is not in the range of 1 - 20")