#Title: Replit Day  - Day16 - WhileLoops Break - Make It Stop - Day16 - v1


print("Lyrics to Take Care by Drake... Fill in the Blank")
print("-----------------------------------")

attempts = 0
while True:
    print()
    print('''
  I know you've been __1__ by someone else. 
  I can tell by the way you carry __2__.
  If you let __3__, here's what I'll do
  ''')
    blank1 = input("Fill in the blank 1: ")
    blank2 = input("Fill in the blank 2: ")
    blank3 = input("Fill in the blank 3: ")
    print()
    attempts += 1
    if blank1.lower() == "hurt" and blank2.lower(
    ) == "yourself" and blank3.lower() == "me":
        break
    else:
        print()
        print("Try again: ")
        print(f'Attempts: {attempts}')
        print()

print(f'Great Job! It only took you {attempts} attempts to get it right!')
