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
    elif yourGuess < secretNumber:
        print("Too low. Try again!")
    elif yourGuess == secretNumber:
        print(f"You guess {yourGuess}. CORRECT!")
        print(f"You guessed {score} times to get it right")
        tryAgain = input("Try again? (Y/N): ")
        if tryAgain.upper() == "Y":
            score = 0
            continue
        else:
            break

    if yourGuess >= guessChances:
        print("You guessed way too many times. GameOVER!")
        break

print(f"Attempts: {score}")
