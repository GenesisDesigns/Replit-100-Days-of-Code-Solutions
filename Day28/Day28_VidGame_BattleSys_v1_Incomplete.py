#Title: Replit Day  - Day28 - Character Battle System - Epic Character Battle - v1

import os, time, random

MENU = ("------------| Battle Simulator |----------",
        "- Battle to the death!                   -",
        "- Character with most pts wins the game  -",
        "- May the Luck be with you!              -",
        "-------------------------------------------")

#list of char background()

def character_background():
  char_faction = [
    "Elf", "Human", "Orc", "Demon", "Troll", "Beast", "Shadow", "Celestials",
    "DemiGod"
  ]

  char_class = [
    "Elementals", "Thief", "Warrior", "Swordsman", "Ninja", "Magicians",
    "Necromancer", "Blacksmith", "Assassin", "Angel", "Devil"
  ]
