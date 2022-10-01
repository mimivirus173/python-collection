import numbers
import random
import os

# Variables
points = 0

# Game
while True:
    # Check if input is valid
    try:
        # Player input gets checked if it's an integer or no
        num = int(input("Write a number inbetween 0 and 100: "))
    except ValueError:
        # When eror
        print("Invalid input!")
        print("Your input must be an integer!")
        continue
    else:
        # Check if the number is between 0 and 100
        if num <= 99 and num > 0:
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
                # Clear screen
                os.system('cls')
            
                # Print loss text
                print("You lost!")
                print("Final score:",points)
                print("--------------------")
                points == 0
        else:
            print("Invalid input!")
            print("Your number must be inbetween 0 and 100! (from 1-99)")
        continue