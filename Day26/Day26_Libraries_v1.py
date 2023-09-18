#Title: Replit Day  - Day26 - Libraries - The Power Of Libraries In Games - v1


from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')


MENU = ('------------------------', '----| Music Player |----',
        '--- Press 1 to play ----', '--- Press 2 to pause ---',
        '------------------------')

while True:
  os.system("clear")
  for line in MENU:
    time.sleep(0.1)
    print(line)
  print()
  while True:
    choice = int(input("press 1 to play or press 2 to stop: "))
    if choice == 1:
      play()
    elif choice == 2:
      os.system("clear")
      exit()
    elif choice not in [1, 2]:
      print("invalid choice. Tryagain")
      continue
    else:
      exit()
