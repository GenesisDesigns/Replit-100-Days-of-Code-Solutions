#Title: Replit Day  - Day8 - Affirmation Generator - Day8 - v1


  
"""---------- Affirmation Generator ----------"""

username = input("What is your name?: ")
if username == 'Aaron' or username == 'aaron':
  dayOfWeek = input("What is the current day of the week (e.g Monday, Tuesday...)?: ").capitalize()
  favFood = input("what is your favorite food?: ")
  favDrink = input("What is your favorite beverage?: ")
  print()
  print(f'Hi {username}! It is {dayOfWeek}')
  print(f'Your favorite food is: {favFood} and favorite drink is: {favDrink}.')

elif username == 'Kobe' or username == 'kobe':
  print(f'Hello {username}! You\'re the goat!')
else:
  print(
    f"Hello {username}! I don\'t know you."
  )
