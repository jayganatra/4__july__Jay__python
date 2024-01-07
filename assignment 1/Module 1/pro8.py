letter = input("Enter a single letter: ")
if len(letter) == 1 and letter.isalpha():
    vowels = "aeiouAEIOU"
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")
else:
    print("Please enter a valid single letter.")
