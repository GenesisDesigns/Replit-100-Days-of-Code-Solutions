#Title: Replit Day  - Day32 - List - Make A List - v1


import random

#say hello in different languages

greetings_list = [
  'السلام عليكم', '你好', 'Hallo', 'Bonjour', 'Guten Tag', 'नमस्ते', 'Ciao',
  'こんにちは', '안녕하세요', 'Cześć', 'Olá', 'Здравствуйте', 'Hola', 'Hej', 'สวัสดี',
  'Merhaba', 'Вітаю', 'Xin chào', 'Helô', 'Bawo ni'
]

greetings_dict = {
  'Arabic': 'السلام عليكم',
  'Chinese (Mandarin)': '你好',
  'Dutch': 'Hallo',
  'French': 'Bonjour',
  'German': 'Guten Tag',
  'Hindi': 'नमस्ते',
  'Italian': 'Ciao',
  'Japanese': 'こんにちは',
  'Korean': '안녕하세요',
  'Polish': 'Cześć',
  'Portuguese': 'Olá',
  'Russian': 'Здравствуйте',
  'Spanish': 'Hola',
  'Swedish': 'Hej',
  'Thai': 'สวัสดี',
  'Turkish': 'Merhaba',
  'Ukrainian': 'Вітаю',
  'Vietnamese': 'Xin chào',
  'Welsh': 'Helô',
  'Yoruba': 'Bawo ni'
}

#generate random greetings from the list
while True:
  generate_greeting = input("Generate a greeting list (Y/N): ")
    if generate_greeting.capitalize() == "Y":
      random_greeting = random.choice(greetings_list)
      print(random_greeting)
      print()
      continue
    else:
      break
      
  print("\n\n")

#generate random greetings from the dictionary
while True:
  generate_greeting = input("Generate a greeting from dictionary (Y/N): ")

