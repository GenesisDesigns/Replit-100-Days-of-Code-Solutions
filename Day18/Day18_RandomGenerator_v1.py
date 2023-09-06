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
    elif yourGuess == secret_number:
        print("Congrats! you got it right!")
        print(f'Your attempts so far: {attempts}')
        tryAgain = input("Would you like to try again? (Y/N): ").upper()
        if tryAgain.upper() == "Y":
            continue
        else:
            break
    elif yourGuess < secret_number:
        print("Your guess is less than the secret number")
        continue
    else:
        print("Your guess is higher than the secret number")
        continue
