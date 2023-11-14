"""EX03 - Strucuted Wordle."""

__author__ = "730705343"


def contains_char(guess: str, single_characters: str) -> bool:
    """Returns a boolean for if a letter is found in input_guess."""
    assert len(single_characters) == 1
    # Function ensuring that the input_guess is one letter
    counter: int = 0
    while counter < len(guess):
        if guess[counter] == single_characters:
            return True
        counter += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns string of emoji colors."""
    emoji_string = ""
    counter: int = 0
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # Creating the string of emojis that will eventually be printed out
    while len(emoji_string) < len(guess):
        if guess[counter] == secret_word[counter]:
            emoji_string += GREEN_BOX
        elif contains_char(secret_word, guess[counter]):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        counter += 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Make user guess the correct length of word."""
    guess = input(f"Enter a {expected_length} character word: ")
    # making sure that the length of the guess is the expected length that should be inputted
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try Again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    attempts: int = 1
    attempts_bool = True
    secret_word: str = "codes"
    # setting the number of attempts that the user can have
    while attempts_bool is True and attempts <= 6:
        print(f"=== Turn {attempts}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        attempts += 1
        if guess == secret_word:
            attempts_bool = False
    if attempts <= 6 and guess == secret_word:
        print(f"You won in {attempts - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


# Calling the main function
if __name__ == "__main__":
    main()