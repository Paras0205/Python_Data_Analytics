#rock,paper,scissor

import random

choices = ["rock", "paper", "scissors"]

while True:

    computer_choice = random.choice(choices)

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice in choices:
            break
        else:
            print("Enter a valid choice.")

    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        result = "Tie"

    elif user_choice == "rock" and computer_choice == "paper":
        result = "Computer wins"

    elif user_choice == "paper" and computer_choice == "scissors":
        result = "Computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        result = "Computer wins"

    elif user_choice == "paper" and computer_choice == "rock":
        result = "User wins"

    elif user_choice == "scissors" and computer_choice == "paper":
        result = "User wins"

    elif user_choice == "rock" and computer_choice == "scissors":
        result = "User wins"

    print("Result:", result)

    choice = input("Play Again? (yes/no): ").lower()

    if choice != "yes":
        print("Game Over!")
        break