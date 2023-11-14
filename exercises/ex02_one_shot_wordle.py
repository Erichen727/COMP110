"""EX02 - One Shot Wordle."""

__author__ = "730705343"

secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess?")
counter = 0
attempts: int = 0
result: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess_word) != len(secret_word):    
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# when the letters are correct, the code prints the green box
while counter < len(secret_word):
    if guess_word[counter] == secret_word[counter]:
        result += GREEN_BOX
    else:
        counter2 = 0
        # creating a bool for if the guess_word letter is in the secret_word
        statement = False
        while statement is False and counter2 < len(secret_word):
            if guess_word[counter] == secret_word[counter2]:
                statement = True
            else:
                counter2 += 1
        if statement is True:
            # if the letter in the guess_word is in a different location than in the secret_word, it concatonates a yellow box to the final string
            result += YELLOW_BOX
        if statement is False:
            # if the letter in the guess_word is not in the secret_word at all, it concatonates a white box to the final string
            result += WHITE_BOX
    counter += 1
print(result)
if str(guess_word) == str(secret_word):
    print("Woo! You got it")
else:
    print("Not quite. Play again later.")

    
    

    
        
