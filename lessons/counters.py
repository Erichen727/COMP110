"""Practicing Counters"""

number_string = "133"
odds: int = 0

if int(number_string[0]) % 2 == 1:
    odds += 1
if int(number_string[1]) % 2 == 1:
    odds += 1
if int(number_string[2]) % 2 == 1:
    odds += 1
print(odds)
