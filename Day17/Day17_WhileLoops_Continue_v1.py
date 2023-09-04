#Title: Replit Day  - Day17 - WhileLopps Continue - Lets Cheat Continue - v1


player1_score = 0
player2_score = 0
choices = ['R', 'P', 'S']

while player1_score <= 3 or player2_score <= 3:
    print()
    player1_choice = input("Player1, please choose (R, P, S): ")
    player1_choice = player1_choice.upper()

    player2_choice = input("Player2, please choose (R, P, S): ")
    player2_choice = player2_choice.upper()

    if player1_choice and player2_choice not in choices:
        print("Invalid choice, please try again")
        continue
