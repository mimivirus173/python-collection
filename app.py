import numbers
import random

# Variables
rand = random.randint(1,100)
points = 0

# Game
while True:
    input = int(input("Write a number between 1 and 99: "))
    if input <= 99 and input >= 0:
        # Random number
        roll = random.randint(1,100)
    
        if roll >= input:
            print("You win!")
        
            print("You gain",input,"points.")
            points += input

            print("Current score:",points)
            print("--------------------")
        else:
            print("You lost!")

            print("Final score:",points)
            print("--------------------")
            points == 0

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Game over.")