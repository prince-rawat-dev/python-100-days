words = ["apple","banana","orange","grape","Umbrella","python"]

vowel_words = [word for word in words if word[0].lower() in "aeiou"]
print(vowel_words)