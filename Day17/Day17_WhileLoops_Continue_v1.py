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

    if player1_choice == player2_choice:
        print("It's a tie")
    elif player1_choice == "R" and player2_choice == "S" or \
        player1_choice == "P" and player2_choice == "R" or \
        player1_choice == "S" and player2_choice == "P":
        print("Player1 Wins!")
        player1_score += 1

    else:
        print("Player2 Wins!")
        player2_score += 1

    print()
    print(f"\
        Player1's score is: {player1_score},\
        Player2's Score is: {player2_score}\
  ")
    print()
