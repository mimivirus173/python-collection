import numbers
import random

# Variables
points = 0

# Game
while True:
    num = int(input("Write a number between 1 and 99: "))
    if num <= 99 and num > 0:
        # Random number
        roll = random.randint(1,100)
    
        if roll >= num:
            print("You win!")
        
            print("You gain",num,"points.")
            points += num

            print("Current score:",points)
            print("--------------------")
        else:
            print("You lost!")

            print("Final score:",points)
            print("--------------------")
            points == 0
    else:
        print("Invalid input!")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Game over.")