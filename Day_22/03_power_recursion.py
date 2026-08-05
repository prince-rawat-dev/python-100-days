def power(base,exponent):
    '''Gives value of (base^exponent)'''
    
    if((base == 0 and exponent == 0) or (base == 1 and exponent == 0) or (base == 0 and exponent == -1)):
        print("Not Defined")
    elif exponent == 0:
        return 1
    else:
        return base * power(base,exponent-1)

print(f"\nValue of power(3,4): {power(3,4)}\n")
