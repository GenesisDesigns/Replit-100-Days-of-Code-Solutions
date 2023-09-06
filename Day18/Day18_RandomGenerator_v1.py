#Title: Replit Day  - Day18 - Random Generator - Guess Number - v1


import random

minNum = 1
maxNum = 5
secret_number = random.randint(minNum, maxNum)
attempts = 0

while True:
    print()
    yourGuess = int(input(f"Guess a number between {minNum} to {maxNum}: "))
    attempts += 1
    if yourGuess < minNum or yourGuess > maxNum:
        print("Game OVER! Thanks for playing!")
        exit()

