# rock paper scissor game

#  Write a Python program for the Rock, Paper, Scissors game. 
# The program should allow the user to play against the computer.
# The computer's choice should be randomly generated. After each round, the program should display the user's choice, 
# the computer's choice, and the result of the game (win, lose, or tie). 
# The program should continue to play until the user decides to quit.

# Let's play Rock, Paper, Scissors!
# Enter 'rock' for Rock, 'paper' for Paper, or 'scissors' for Scissors: rock
# You chose: rock
# Computer chose: scissors
# You win!

# Do you want to play again? (yes/no): yes
# Enter 'rock' for Rock, 'paper' for Paper, or 'scissors' for Scissors: paper
# You chose: paper
# Computer chose: rock
# You win!

# Do you want to play again? (yes/no): no
# Thanks for playing!

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")

