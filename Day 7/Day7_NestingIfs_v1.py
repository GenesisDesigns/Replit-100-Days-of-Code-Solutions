#Title: Replit Day  - Day7 - Nesting Dolls Code - Nesting If Statements within if Statements - v1



print("Fake Fan Finder")
print("--------------------")
favAnime = input("What's your favorite anime?: ").title()
if favAnime == "One Piece":
    otherChar = input("Oh really?! Name any of the characters?: ").capitalize()
    if otherChar == "Nami":
        shipJob = input(
            "You got that by pure chance. Okay then, what is her job on the ship?: "
        ).capitalize()
        if shipJob == "Navigator":
            pirateBounty = input("Hmph! What was her first bounty then?: ")
            if pirateBounty == "ummm...":
                print("ummm...")
            else:
                print("See! FAKE One Piece Fan!")
        else:
            print("See! FAKE One Piece Fan!")
    else:
        print("See! FAKE One Piece Fan!")
else:
    print("See! FAKE One Piece Fan!")