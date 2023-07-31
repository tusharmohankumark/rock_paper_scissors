import random

options = ("rock", "paper", "scissors") #tuple that consists of the components of the game
running=True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Rock, Paper or Scissors ? ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You Win :)")
    elif player == "paper" and computer == "rock":
        print("You Win :)")
    elif player == "scissors" and computer == "paper":
        print("You Win :)")
    else:
        print("You Lose :(")

    if not input("Play Again ? (y/n)").lower() == "y":
        running = False

print("Thanks For Playing :)")