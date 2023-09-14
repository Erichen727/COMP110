"""EX01 - Chardle - """
__author__ = "730705343"

user_word = input("Enter a 5-character word: ")
letter_instance = 0
if len(user_word) == 5:
    ("Enter a single character: ")
    letter = input("Enter a single character: ")
    print("searching for " + letter + " in word")
if letter == (user_word[0]):
        print(letter, "found at index 0")
        letter_instance += 1
if letter == (user_word[1]):
        print(letter, "found at index 1")
        letter_instance += 1
if letter == (user_word[2]):
        print(letter, "found at index 2")
        letter_instance += 1
if letter == (user_word[3]):
        print(letter, "found at index 3")
        letter_instance += 1
if letter == (user_word[4]):
        print(letter, "found at index 4")
        letter_instance += 1
if letter_instance == 0:
        print("No instances of " + letter + " is found in the word")
        exit()
if letter_instance == 1:
     print(letter_instance, "instance of", letter , "is found in", user_word)
     exit()
if letter_instance > 1:
    print(letter_instance, "instances of", letter , "is found in", user_word)
    exit()
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if " " in user_word:
    print("Error: Character must me a single character.")
    exit()