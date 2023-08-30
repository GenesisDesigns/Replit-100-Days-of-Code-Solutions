#Title: Replit Day  - Day12 - Debugging - Find The Bugs - v1

print("100 Days of Code QUIZ")
print()

      
answer1 = input("What programming language are we using?: ").capitalize()
if answer1 == "Python":
  print("Correct")
else:
  print("Nope")
answer2 = int(input("Which lesson number is this?: "))
if(answer2 > 12):
  print("We're not there yet")
elif(answer2 == 12):
  print("Correct!")
else:
  print("We are way past that!")