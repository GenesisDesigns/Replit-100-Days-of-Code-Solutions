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

  #generates char factions and class
  random_char_faction = random.choice(char_faction)
  random_char_class = random.choice(char_class)
  print(f"Faction: {random_char_faction}")
  print(f"Class: {random_char_class}")

#random generates dice roll sides
def dice_roll():
  dice6 = random.randint(1, 6)
  dice8 = random.randint(1, 8)

def luck():
  lucky_dice = random.randint(1, 12)
  return lucky_dice

def char_stats():
  #Calls dice_roll()
  dice6, dice8, dice12 = dice_roll()

  #char stats formula
  healthBar = (dice6 * dice12) / 2 + 10
  strength = (dice6 * dice8) / 2 + 12

  #print(f"HP: {healthBar}")

  #print(f"STR: {strength}")
  return healthBar, strength

def char_names():
  player1 = input("Player1's Character Name: ")
  character_background()  #player1
  print()
  player2 = input("Player2's character name: ")
  character_background()  #player2
  return player1, player2

#enter char names and generate player stats
def player_stats():
  healthBar, strength = char_stats()

  #player1
  player1_HP = healthBar
  player1_STR = strength
