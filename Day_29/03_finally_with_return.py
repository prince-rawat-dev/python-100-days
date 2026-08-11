def test():
    try:
        return "try\n"
    finally:
        print("\nProgram Executed")

print(test())