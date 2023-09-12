#Title: Replit Day  - Day22 - Use Other People's Code - v1

import random

min = 1
max = 5
guessChances = 7
secretNumber = random.randint(min, max)
score = 0

for i in range(guessChances):
    yourGuess = int(input(f"Guess a number between {min} and {max}: "))
    score += 1
    if yourGuess > secretNumber:
        print("Too high. Try again!")
