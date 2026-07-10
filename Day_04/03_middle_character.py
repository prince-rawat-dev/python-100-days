word = input("Enter any word: ")

length = len(word)

if length % 2 != 0:
    middle = length // 2
    print("Middle character:", word[middle])

else:
    middle1 = (length // 2) - 1
    middle2 = length // 2
    print("Middle characters:", word[middle1] + word[middle2])