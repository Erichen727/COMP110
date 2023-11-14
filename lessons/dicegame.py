"""Randomly rolls dice and sums total"""
from random import randint


roll1: int = randint(1,6)
roll2: int = randint(1,6)
roll3: int = randint(1,6)

dice_rolls: list[int] = [roll1, roll2, roll3]
dice_index: int = 0
dice_sum: int = 0

while dice_index <= len(dice_rolls) - 1:
    print(dice_rolls[dice_index])
    dice_sum += 1
    dice_index += 1
print(dice_sum)
 