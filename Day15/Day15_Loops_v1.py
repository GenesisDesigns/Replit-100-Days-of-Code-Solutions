#Title: Replit Day  - Day15 - Loops - All About The Loop - Day15 - v1


animalSounds = {
  'cat' : 'meow',
  'dog' : 'woof',
  'cow' : 'moo',
  'duck' : 'quack',
  'sheep' : 'baa',
  'goat' : 'meee',
  'frog' : 'ribbit',
  'donkey' : 'yeeee - haw'
}

print()
moreSounds = input("Do you want to pick an animal? (Y/N): ").upper()
while moreSounds == 'Y':
  animal = input("Pick an animal: ")
  animal = animal.lower()
  sounds = animalSounds.get(animal)
  
  if animal not in animalSounds:
    animal = input("Pick another animal: ")
  else:
    print()
    print(f'Your animal is a {animal} and it goes {sounds}.')
    print()
    more = input("exit or not? (Y/N): ").upper()
    if more == 'Y':
      break

  

