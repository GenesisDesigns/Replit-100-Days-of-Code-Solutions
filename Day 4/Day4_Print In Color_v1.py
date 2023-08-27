#Title: Replit Day 4 - Print In Color V1

print("=== Your Adventure Simulator ===")
heroName = input("What is the hero's name?: ").title()
villainName = input("What is the villain's name?: ").title()
heroWeapon = input("What is the hero's weapon of choice?: ").title()
villainWeapon = input("What is the villain's weapon of choice?: ").title()
heroElement = input ("What is the hero's element?: ").title()
villainElement = input ("What is the villain's element?: ").title()
print("\n\n")

print("Once upon a time, there were two gods, \033[91m", heroName, "\033[0m and", villainName + ".")
print(heroName, "was the god of", heroElement, "while", villainName, "was the god of", villainElement + ".")

print()

print("""They were complete \033[94mopposites\033[0m of each other. 
They have been waging war with each other for many years, perhaps for eons. 
Finally on the last day of their battle, they both fell to their 
knees and perished.""")
print("The End.. to be continued!")