# Phase-1
# Project Title: Rock, Paper, Scissor Game
# Imported the random module.
import random
# Introduced Infinite loop to keep the game running until the user decides to exit

while True:
    # Prompted the user to continue or exit
    n = input("Press 1 to Continue and 3 to Exit\n")
    if n == "1":
        # Asked for the user's choice
        u_choice = int(
            input('Enter your Choice: Press 1 for ROCK, 2 for Paper, 3 for SCISSOR: '))

# Validated that the user's input is valid (1, 2, or 3)
        if u_choice >= 4 or u_choice < 0:
            print("Invalid Input")
        else:
            # Generated the computer's choice randomly (1, 2, or 3)
            c_choice = random.randint(1, 3)

# Displayed the computer's choice
            print("Computer Choice: ", c_choice)

# If both choices are the same, it's a draw
            if c_choice == u_choice:
                print("DRAW\n")

# If the computer chooses ROCK and the user chooses SCISSOR, the computer wins
            elif c_choice == 1 and u_choice == 3:
                print("You Lose\n")

# If the user chooses SCISSOR and the computer chooses ROCK, the user wins
            elif u_choice == 3 and c_choice == 1:
                print("You Won\n")

# If the computer's choice is greater than the user's, the computer wins
            elif c_choice > u_choice:
                print("You Lose\n")

# If the user's choice is greater than the computer's, the user wins
            elif u_choice > c_choice:
                print("You Won\n")

    else:
        print("-------------------------------------------------------------Exiting the Application-------------------------------------------")
# Exit the loop and terminate the program

        break
