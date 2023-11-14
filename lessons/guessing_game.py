"""Program that loops until correct number is guessed"""

from random import randint

secret_number: int = randint(1,10)
guess: int = int(input("Guess a mumber between 1 and 10: "))

attempts = 1
max_attempts = 3

while guess != secret_number and attempts < max_attempts:
    print("Wrong!")
    if guess > 10 or guess < 1:
        print("Not in the range")
#ask for another guess
    if guess < secret_number:
        print("guess higher")
    elif guess > secret_number:
        print("guess lower")
    guess = int(input("Guess Again: "))
    attempts += 1
if attempts == max_attempts:
    print("you lose!")
    exit()
#if I've reached this point, guess == secret
print("you guessed correctly")
