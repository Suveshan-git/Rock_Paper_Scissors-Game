# ROCK, PAPER, SCISSORS
import random

# Welcome Player and explain what to do
print("Welcome Player! Type out one of the following: Rock, Paper or Scissors")

# Ask the user to select between Rock, Paper or Scissors
player = input("Player 1: ")

# Validate the user input is valid
if player == "Rock" or player == "Paper" or player == "Scissors":
    # Determine and display the CPUs choice
    numeric_choice = random.randint(1, 3)
    if numeric_choice == 1:
        cpu = "Rock"
    elif numeric_choice == 2:
        cpu = "Paper"
    elif numeric_choice == 3:
        cpu = "Scissors"

    print(f"CPU shows {cpu}")

    # Determine and display the winner
    if player == "Rock" and cpu == "Rock":
        print("It is a draw!")
    elif player == "Rock" and cpu == "Paper":
        print("CPU wins!")
    elif player == "Rock" and cpu == "Scissors":
        print("Player wins!")
    elif player == "Paper" and cpu == "Rock":
        print("Player wins!")
    elif player == "Paper" and cpu == "Paper":
        print("It is a draw!")
    elif player == "Paper" and cpu == "Scissors":
        print("CPU wins!")
    elif player == "Scissors" and cpu == "Rock":
        print("CPU wins!")
    elif player == "Scissors" and cpu == "Paper":
        print("Player wins!")
    elif player == "Scissors" and cpu == "Scissors":
        print("It is a draw!")

else:
    print("Invalid entry! Please only use the words: Rock, Paper or Scissors")


