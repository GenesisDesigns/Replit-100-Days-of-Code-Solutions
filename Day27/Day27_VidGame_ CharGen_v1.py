#Title: Replit Day  - Day27 - Character Generator - Video Game Characters - v1

""" 
Requirements:
1. first name and character type (human, elf, wizard, orc) 
2. must capitalize the first letter of each word
3. color the name and color the hp, strength
4. dice rolls (6, 8, 12 sides)
5. must be wrapped in a loop to ask if you want to generate a new character 

Formulas: 
  HP = (6SidedDiceRoll x 12SidedDiceRoll)/2 + 10
  str =  (6SidedDiceRoll x 8SidedDiceRoll)/2 + 12


"""

import os, time, random

MENU = (
  "------| Character Generator |------",
  "- Generate the best character ever-",
  "- ONLY 1 Gold to generate 1 coin  -",
  "- May the Luck be with you!        -",
  "-----------------------------------"
)

def character_backgrounds():
  #list of char traits 
  char_faction = ["Elf", "Human", "Orc", "Demon", "Troll", "Beast", "Shadow", "Celestials", "DemiGod"]
  char_specialization = ["Elementals", "Thief", "Warrior", "Swordsman", "Ninja", "Magicians", "Necromancer", "Blacksmith","Assassin", "Angel", "Devil"]

  #generates random char trait 
  random_char_faction = random.choice(char_faction)
  random_char_specialization = random.choice(char_specialization)

  print(f"Character Faction: {random_char_faction}")
  print(f"Character Specialization: {random_char_specialization}")

def dice_rolls():
  #generate a random float number for each dice roll 
  dice6 = random.uniform(1,6)
  dice8 = random.uniform(1,8)
  dice12 = random.uniform(1,12)
  return dice6, dice8, dice12


def char_stats():
  #calling dice_roll() function variables
  dice6, dice8, dice12 = dice_rolls()

  #formulas 
  healthBar = (dice6 * dice12)/2 + 10
  strength = (dice6 * dice8)/2 + 12

  #print HP and Str and round to 2 decimal places
  print(f"HP: {round(healthBar, 2)}")
  print(f"Stength: {round(strength, 2)}")

while True:
  for line in MENU:
    print(line)
    time.sleep(0.1)
  print()
  
  char_name = input("Character Name: ").title()
  os.system("cls")
  print(f"Character Name: {char_name}")
  character_backgrounds()
  char_stats()

  print()
  tryAgain = input("Generate another character? (Y/N): ")
  print()
  if tryAgain.capitalize() == "Y":
    os.system("cls")
    continue
  else:
    os.system("cls")
    break
