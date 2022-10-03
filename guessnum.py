import numbers
import random
import os

# Variables
points = 0

while True:
    # Check for valid input
    try:
        lim1 = int(input("Lower limit for the random number: "))
        lim2 = int(input("Upper limit for the random number: "))
    except ValueError:
        print("Invalid input!")
        print("--------------------")
    else:
        # The computer's number
        num = random.randint(lim1, lim2)
        
        # Check for valid input
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input!")
            print("--------------------")
        else:
            # The game
            if guess == num and guess >= lim1 and guess <= lim2:
                print("You win!")
                
                # Points
                print("You gain 1 point.")
                points += 1
                
                print("Current score:",points)
                print("--------------------")
            elif guess != num:
                os.system('cls')
                print("You lost!")
                print("The number was:",num)

                print("Final score:",points)
                print("--------------------")
                points = 0
            else:
                print("Invalid input!")
                print("--------------------")
            continue