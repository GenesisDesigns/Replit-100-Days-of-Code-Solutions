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
  print(f"Player1's HP: {healthBar}")
  print(f"Player1's STR: {strength}")
  print()

  #player2
  player2_HP = healthBar
  player2_STR = strength
  print()
  return player1_HP, player2_HP, player1_STR, player2_STR

for line in MENU:
  print(line)
  time.sleep(0.1)
  print()

#PK points
player1_points = 0
player2_points = 0

#Num of Rounds
round = 0

while True:
  player1, player2 = char_names()

  while player1_points <= 3 or player2_points <= 3:
    player1_HP, player2_HP, player1_STR, player2_STR = player_stats()
    round += 1
          
    #Players Luck - decides who goes first
    player1_luck = luck()
    player2_luck = luck()
    print(f"Player1's Luck: {player1_luck}")
    print(f"Player2's Luck: {player2_luck}")
    print()
          
    #Luck determines who goes first
    if player1_luck == player2_luck:
      #os.system("clear")
      continue
    elif player1_luck > player2_luck:  #player1 goes first
      new_player2_HP = player2_HP - player1_STR  #player1 attacks player2
      if new_player2_HP > 0:
        print(f"Player1's char, {player1}, has {new_player1_HP} HP left.")
        print(f"""
        {player1} is not dead yet! 
        We must extinguish the flames my liege!
        Trample them while they are still on the ground!
        LFG!
        """)
        print()
        continue
      else:
        print(f"Player1's char, {player1}, is dead! Congrates you win!")
        player2_points += 1
        print()
      print(f"{player1} Points: {player1_points}")
      print(f"{player2} Points: {player2_points}")
      print(f"It took you {round} rounds to win!")
    playAgain = input("Play Again? (Y/N)")
    if playAgain.upper() == "Y":
      continue
    else:
        
