#Title: Replit Day  - Day31 - Create User Interface (UI) - v1



from termcolor import colored

def interface1():
  center_align_title = 50
  left_align1 = 20
  left_align2 = 40
  right_algin3 = 20
  print(colored(f"{'Music APP' : ^{center_align_title}}", "yellow"))
  print("\n\n")
  
  print(f"🔥▶️ Radio Gaga")
  print(colored(f"    Queen", "yellow"))
  print("\n\n")
  
  print(f"PREV")
  print(colored(f"{'NEXT' : ^{left_align1}}", "green"))
  print(colored(f"{'PAUSE' : ^{left_align2}}", "red"))

def interface2():
  center_align_title = 50
  right_align = 50
  print(f"{'WELCOME TOP' : ^{center_align_title}}")
  print(colored(f"{'--    ARMBOOK    --' : ^{center_align_title}}", "blue"))
  print("\n\n")

  print(colored(f"{'Definitely not a rip off' : >{right_align}}", "yellow"))
  print(colored(f"{'of a certain other social' : >{right_align}}", "yellow"))
  print(colored(f"{'networking site.' : >{right_align}}", "yellow"))
  print()

  print(colored(f"{'Honest' : ^{center_align_title}}", "red"))
  print("\n\n")
  print(f"{'Username:' : ^{center_align_title}}")
  print(f"{'Password:' : ^{center_align_title}}")

center_align = 50
print("Interface1:")
print()
interface1()
print("\n\n")
print(f"{'=============================================' : ^{center_align}}")
print("\n\n")
print(f"{'=============================================' : ^{center_align}}")
