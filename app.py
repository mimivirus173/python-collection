import numbers
import random

# Variables
rand = random.randint(1,100)
points = 0

# Game
while 1==1:    
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
            continue
        else:
            print("You lost!")
        
            points == 0
            continue