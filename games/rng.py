import random
import os

def main():
    # Variables
    points = 0

    # Game
    while True:
        # Check if input is valid
        try:
            # Input gets checked if it's an integer or not
            num = int(input("Write a number inbetween 0 and 100: "))
        except ValueError:
            print("Invalid input!")
            print("Your input must be an integer!")
            print("--------------------")
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
                    print("You gain",num,"point(s).")
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
                    points = 0
            else:
                print("Invalid input!")
                print("Your number must be inbetween 0 and 100!")
                print("--------------------")
            continue

if __name__ == '__main__':
    main()