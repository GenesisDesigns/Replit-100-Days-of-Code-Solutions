#Title: Replit Day  - Day14 - Rock, Paper, Scissors - v1



print("Game: Rock, Paper, Scissors")
from getpass import getpass as input #hides the input

print('''
  R = Rock
  P = Paper
  S = Scissors 
  ''')

options = ["R", "P", "S"]

#function to determine the winner


def deterWinner(player1, player2):
    if player1 == player2:
        print("Tie")
    elif player1 == "R" and player2 == "S":
        print("Player1 wins!")
    elif player1 == "P" and player2 == "R":
        print("Player1 wins!")
    elif player1 == "S" and player2 == "P":
        print("Player1 wins!")
    else:
        return "Player2 wins!"


player1 = input("Player1 choose R, P, S: ").upper()
player2 = input("Player2 choose R, P, S: ").upper()

# player1 = player1.upper()
# player2 = player2.upper()

while player1 not in options or player2 not in options:
    print("Invalid choice. Please choose 'R', 'P', 'S'")
    player1 = input("Player1 choose R, P, S: ")
    player2 = input("Player2 choose R, P, S: ")

result = deterWinner(player1, player2)

print(result)
