#Title: Replit Day  - Day33 - Dynamic Lists - Getting Dynamic - v1

print("------------------------")
print("-----| To Do List |-----")
print("------------------------")

myToDoList = ["swim", "eat", "sweep"]

def myToDoList_func():
  for index, item in enumerate(myToDoList):
      print(index, item)

while True:
  #view, add, edit (remove) to do list
  whatToDo = input("""
    1. View List (V), 
    2. Add to List (A),
    3. Remove from List (R)
    4. Exit (E)
  """)

  if whatToDo.capitalize() == "V":
    myToDoList_func()
  elif whatToDo.capitalize() == "A":  #Add - add to the end
    addToList = input("What do you want to add?: ")
    myToDoList.append(addToList)
    print()
    myToDoList_func()
    print()
  elif whatToDo.capitalize() == "R":  #Edit - remove
    removeList = input("What do you want to remove?: ")
    print()
    if removeList in myToDoList:
      myToDoList.remove(removeList)
      print()
      myToDoList_func()
      print()
    else:
      print("What you want to remove is not in the list")
      print()
      tryAgain = input("Try Again? (Y/N): ")
