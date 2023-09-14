#Title: Replit Day  - Day24 - RollDice - Roll In The Parameters - v1

print("-----| Infinity Dice Game |------")
print()

import random

def infinityDice():
  while True:
    numSides = int(input("How many sides?: "))
    randomSide = random.randint(1, 10)
    if numSides == randomSide:
      tryAgain = input("Correct! Try again? (Y/N): ")
      if tryAgain.upper() == "Y":
        continue
      else:
        exit()
    elif numSides > randomSide:
      print("Sides are lower, try again")
      continue
    else:
      print("Sides are are higher, try again")
      continue

infinityDice()
