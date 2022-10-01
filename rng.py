import numbers
import random
import os

# Variables
points = 0

# Game
while True:
    # Player's input
    num = int(input("Write a number between 1 and 99: "))
    
    # Check if input is valid
    if num <= 99 and num > 0 and type(input) == int:
        # Random number
        roll = random.randint(1,100)

        # Decides if you win or lose
        if roll >= num:
            print("You win!")

            # Gain points
            print("You gain",num,"points.")
            points += num

            print("Current score:",points)
            print("--------------------")
        else:
            os.system('cls')
            print("You lost!")

            print("Final score:",points)
            print("--------------------")
            points == 0
    else:
        print("Invalid input!")
    continue