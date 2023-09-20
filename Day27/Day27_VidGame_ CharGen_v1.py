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
