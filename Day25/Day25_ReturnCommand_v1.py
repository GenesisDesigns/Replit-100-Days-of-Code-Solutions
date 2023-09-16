#Title: Replit Day  - Day25 - ReturnCommand - Send It Back - v1

print("-----| character Stat Generator | ------")
print("-------------------------------------------")

import random

def rollDice():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 8)
  return dice1 * dice2
