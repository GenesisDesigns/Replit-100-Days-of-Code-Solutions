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
