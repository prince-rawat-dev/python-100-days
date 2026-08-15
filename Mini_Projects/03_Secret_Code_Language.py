# ============================================================
# SECRET CODE LANGUAGE — PYTHON MINI PROJECT
# ============================================================
#
# An interactive message coding and decoding program based on
# Exercise 4, extended with a user-controlled random-character
# key and an interactive menu.
#
# FEATURES:
# • Code complete messages word-by-word
# • Decode coded messages
# • User-controlled padding key
# • Random characters at the beginning and end
# • Special handling for words shorter than 3 characters
# • Code / Decode / Quit menu
# • Input validation and exception handling
#
# CONCEPT OF "key":
# The "key" is NOT an encryption/password key.
# It represents the NUMBER OF RANDOM CHARACTERS added to
# BOTH the beginning and end of every word containing at least
# 3 characters.
#
# Example with key = 3:
#
# prince
#   ↓
# rincep
#   ↓
# abc + rincep + xyz
#   ↓
# abcrincepxyz
#
# During decoding, the same key (3) tells the program to remove
# 3 characters from the beginning and 3 from the end.
#
# For words shorter than 3 characters:
# The word is simply reversed.
#
# PYTHON CONCEPTS:
# Strings | Lists | Loops | Functions | Slicing
# split() | join() | len() | random | match-case
# while True | break | continue | try-except | raise
# ============================================================


import random
import string

# RANDOM CHARACTER GENERATOR

def generate_padding(key):

    return "".join(random.choices(string.ascii_lowercase,k=key))

# CODE ONE COMPLETE MESSAGE

def code_message(message, key):

    words = message.split()
    coded_words = []

    for word in words:

        if len(word) < 3:
            coded_word = word[::-1]

        else:
            coded_word = word[1:] + word[0]

            coded_word = (generate_padding(key) + coded_word + generate_padding(key))

        coded_words.append(coded_word)

    return " ".join(coded_words)


# DECODE ONE COMPLETE MESSAGE

def decode_message(message, key):

    words = message.split()
    decoded_words = []

    for word in words:

        if len(word) < 3:
            decoded_word = word[::-1]

        else:
            core = word[key:-key]
            decoded_word = core[-1] + core[:-1]

        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


# GET VALID KEY FROM USER

def get_key():

    try:
        key = int(
            input("Enter key (number of random characters on each side): "))

        if key <= 0:
            raise ValueError("Key must be greater than 0.")

        return key

    except ValueError as e:

        print("Invalid key:", e)
        return None


# MAIN MENU

def menu():

    while True:

        print("\n" + "=" * 55)
        print("           🔐 SECRET CODE LANGUAGE")
        print("=" * 55)

        print("\n1. Code Message")
        print("2. Decode Message")
        print("3. Quit")

        try:

            choice = int(input("\nEnter your choice (1/2/3): "))

        except ValueError:

            print("\n❌ Please enter a valid number.")
            continue


        # CODE

        if choice == 1:

            message = input("\nEnter message to code: ")

            key = get_key()

            if key is None:
                continue

            coded = code_message(message,key)

            print("\n🔐 Coded Message:")
            print(coded)


        # DECODE

        elif choice == 2:

            message = input("\nEnter coded message to decode: ")

            key = get_key()

            if key is None:
                continue

            decoded = decode_message(message,key)

            print("\n🔓 Decoded Message:")
            print(decoded)



        # QUIT

        elif choice == 3:
            print("\nThank you for using Secret Code Language! 👋\n")

            break


        # INVALID OPTION
        else:

            print("\n❌ Invalid choice. Please select 1, 2 or 3.")



# START PROGRAM

menu()