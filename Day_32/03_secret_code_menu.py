# ============================================================
# SECRET CODE LANGUAGE — MENU VERSION
#
# Features:
# Code | Decode | Quit
#
# Concepts:
# while True | match-case | break | functions
# Lists | Strings | Loops | Slicing
# ============================================================


def code_message(message):

    words = message.split()
    coded_words = []

    for word in words:
        if len(word) >= 3:
            new_word = word[1:] + word[0]

            # Fixed padding for the exercise
            new_word = "abc" + new_word + "xyz"

            coded_words.append(new_word)
        else:
            coded_words.append(word[::-1])

    return " ".join(coded_words)


def decode_message(message):

    words = message.split()
    decoded_words = []

    for word in words:
        if len(word) < 3:
            decoded_words.append(word[::-1])
        else:
            word = word[3:-3]
            new_word = word[-1] + word[:-1]

            decoded_words.append(new_word)

    return " ".join(decoded_words)


while True:

    message = input("\nEnter message: ")
    print("\n1. Code")
    print("2. Decode")
    print("3. Quit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))

    except ValueError:
        print("Please enter any one from (1/2/3).")
        continue

    match choice:

        case 1:
            result = code_message(message)
            print("\nEncoded Message:", result)

        case 2:
            result = decode_message(message)
            print("\nDecoded Message:", result)

        case 3:
            print("\nThank you! Goodbye.")
            break

        case _:
            print("\nInvalid choice. Please choose any one from (1/2/3).")