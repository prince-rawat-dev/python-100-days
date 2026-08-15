# ============================================================
# SECRET CODE LANGUAGE — BASIC VERSION
# Exercise 4: Secret Code Language
#
# Concepts:
# Strings | Lists | for loop | len() | slicing | split() | join()
# ============================================================


message = input("Enter a message: ")

words = message.split()
coded_words = []

for word in words:
    if len(word) >= 3:
        new_word = word[1:] + word[0]

        # Fixed 3-character padding for learning the concept
        new_word = "abc" + new_word + "xyz"

        coded_words.append(new_word)
    else:
        new_word = word[::-1]
        coded_words.append(new_word)

coded_message = " ".join(coded_words)
print("\nCoded Message:", coded_message)


# ---------------- DECODING ----------------

coded_words = coded_message.split()
decoded_words = []

for word in coded_words:

    if len(word) < 3:

        new_word = word[::-1]
        decoded_words.append(new_word)

    else:
        word = word[3:-3]
        new_word = word[-1] + word[:-1]

        decoded_words.append(new_word)


decoded_message = " ".join(decoded_words)

print("Decoded Message:", decoded_message)