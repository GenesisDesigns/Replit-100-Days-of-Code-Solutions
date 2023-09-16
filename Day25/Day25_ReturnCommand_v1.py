#Title: Replit Day  - Day25 - ReturnCommand - Send It Back - v1

print("-----| character Stat Generator | ------")
print("-------------------------------------------")

import random

def rollDice():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 8)
  return dice1 * dice2

while True:
  charName = input("Character Name: ").title()
  print(charName)
  healthBar = rollDice()
  print(f"Character's health is (HP): {healthBar}")
  tryAgain = input("Name another character? (Y/N): ").capitalize()

  if tryAgain == "Y":
    continue
  else:
    break
