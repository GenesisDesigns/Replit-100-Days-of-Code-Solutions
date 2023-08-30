#Title: Replit Day  - Day6 - What The Elif Is This? - v1



print("SECURE LOGIN")
username = input("Username: ")
password = input("password: ")
capName = username.capitalize()


if username == "mark" and password =="letmein1":
  print("Why hello there " + capName + " what a nice day. You could've charmed your way in here even without a password!")
  print("have a great day and don't forget to wear a hat")
elif username == "cherry" and password == "cherlord":
  print("Why hello there " + capName + " what a nice day. You could've charmed your way in here even without a password!")
  print("have a great day and don't forget to wear a hat")

elif username == "jackie" and password == "beet23":
  print("Why hello there " + capName + " what a nice day. You could've charmed your way in here even without a password!")
  print("have a great day and don't forget to wear a hat")
else:
  print("Incorrect. Please try again.")
