wordslist = input("Enter a list of spaces: ").split()
maxlength = 0
for word in wordslist:
    if len(word) > maxlength:
        maxlength = len(word)
print(f"The length of word is: {maxlength}")
