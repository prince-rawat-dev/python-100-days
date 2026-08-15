# ============================================================
# SECRET CODE LANGUAGE — FUNCTIONS VERSION
#
# Concepts:
# Functions | Lists | Loops | Strings | Slicing
# split() | join() | len() | return
# ============================================================


def code_message(message):

    words = message.split()
    coded_words = []

    for word in words:

        if len(word) >= 3:

            new_word = word[1:] + word[0]

            # Fixed padding for learning
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


message = input("Enter message: ")

coded = code_message(message)

print("\nCoded Message:", coded)

decoded = decode_message(coded)

print("Decoded Message:", decoded)