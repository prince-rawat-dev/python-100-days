# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode



# main code(The Final Version)

# ============================================================
# SECRET CODE LANGUAGE — FINAL VERSION
# Exercise 4
#
# This program can:
# • Encode a complete message
# • Decode an encoded message
# • Allow the user to choose the padding key
# • Add random characters to encoded words
# • Handle words with less than 3 characters
# • Repeat the menu until the user chooses Quit
#
# CONCEPT of "Key":
# The key tells the program how much random padding/random characters
# was added/needs to be removed from BOTH sides of every word 
# having 3 or more characters..

# Concepts Used:
# Strings | Lists | Loops | Functions | Slicing
# split() | join() | len() | random | match-case
# while True | break | continue | try-except
# ============================================================

import random
import string

# Generate random characters according to the key
def generate_random_chars(key):
    return "".join(
        random.choices(string.ascii_lowercase, k=key)
    )

# Encode complete message
def code_message(message, key):

    words = message.split()
    coded_words = []

    for word in words:
        if len(word) < 3:
            coded_word = word[::-1]

        else:
            coded_word = word[1:] + word[0]

            random_start = generate_random_chars(key)
            random_end = generate_random_chars(key)

            coded_word = (random_start + coded_word + random_end)

        coded_words.append(coded_word)

    return " ".join(coded_words)


# Decode complete message
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


# MAIN MENU
while True:

    print("\n" + "=" * 50)
    print("          SECRET CODE LANGUAGE")
    print("=" * 50)

    print("\n1. Code")
    print("2. Decode")
    print("3. Quit")

    try:
        choice = int(input("\nEnter your choice (1/2/3): "))

    except ValueError:
        print("\nPlease enter only 1, 2 or 3.")
        continue

    
    # CODE

    if choice == 1:

        message = input("\nEnter message to code: ")

        try:
            key = int(
                input("Enter key(number of random characters on each side): "))

            if key <= 0:
                raise ValueError("Key must be greater than 0.")

        except ValueError as e:
            print("Invalid key:", e)
            continue

        result = code_message(message, key)

        print("\nCoded Message:")
        print(result)


    # DECODE

    elif choice == 2:

        message = input("\nEnter message to decode: ")

        try:
            key = int(input("Enter the same key used during coding: "))

            if key <= 0:
                raise ValueError(
                    "Key must be greater than 0."
                )

        except ValueError as e:
            print("Invalid key:", e)
            continue

        result = decode_message(message, key)

        print("\nDecoded Message:")
        print(result)


    # QUIT

    elif choice == 3:

        print("\nThank you for using Secret Code Language!")
        break


    # INVALID CHOICE
   
    else:

        print("\nInvalid choice. Please select 1, 2 or 3.")






# lecture - 40(final practice)

# while True:
    
#     message = input("Enter message you want to code/decode: ")

#     try:
#         choice = int(input("Choices:-\n1. Code\n2. Decode\n3. Quit\nEnter your Choice(1/2/3): "))
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#     # except Exception as e:
#     #     print("Error: ",e)

#     words = message.split(" ")

#     match choice:
#         case 1:
#             # code
#             lst = []
#             for word in words:
#                 if(len(word)>=3):
#                     code1 = "psh"
#                     code2 = "skj"
#                     newword = code1 + word[1:] + word[0] +code2
#                     # words = newword.join(" ")
#                     lst.append(newword)
#                     new_message = " ".join(lst)
#                 else:
#                     new_word = word[::-1]
#                     lst.append(new_word)
#                     new_message = " ".join(lst)

#         case 2:
#             # decode
#             lst = []

#             for word in words:
#                 if(len(word)>=3):
#                     code1 = "psh"
#                     code2 = "skj"
#                     word = word[3:-3]
#                     newword = word[-1] + word[0:-1]
#                     # words = newword.join(" ")
#                     lst.append(newword)
#                 else:
#                     new_word = word[::-1]
#                     lst.append(new_word)
                    
#         case 3:
#             print("thank-you")
#             break
#             # quit
#         case _:
#             print("Invalid Choice!")
#             continue
    
#     new_message = " ".join(lst)
#     print(f"Encripted code : {new_message}")
#     print("\n")


