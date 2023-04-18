# made entirely by discor'd clyde ai bot

import time
import random

print("Welcome to the Yhurr Counting Program!\n")

while True:
    count = 0
    time_start = time.time()
    while True:
        text = input("\nPlease enter some text: ")
        if text.lower() == "yhurr":
            count += 1
        elif text.lower() == "stop":
            time_end = time.time()
            duration = time_end - time_start
            print("\nExiting program...")
            print(f"Total time elapsed: {duration:.2f} seconds")
            print(f"Total yhurr count: {count}")
            print(f"Rate of yhurr/second: {count/duration:.2f}")
            break
        elif text.lower() == "help":
            print("\n*** Yhurr Counting Program Help ***")
            print("Enter 'yhurr' to add to the yhurr count.")
            print("Enter 'description' to view a physical definition of what a yhurr is.")
            print("Enter 'stop' to end the program and see the final results.")
            print("Enter 'help' to display this help message again.")
        elif text.lower() == "random":
            print("\nGenerating random text...")
            for i in range(random.randint(1, 10)):
                print(
                    f"Random text {i + 1}: {''.join(random.choices(['y', 'h', 'u', 'r', 'r'], k=random.randint(3, 10)))}")
        elif text.lower() == "description":
            print("\nA 'yhurr' is the sound made by a cat when it sees a laser pointer. It is a high-pitched chirp or trill, often accompanied by excitement and playfulness. In this program, we count the number of times the word 'yhurr' is used as input.")
        else:
            print("\nInvalid input. Enter 'help' for program instructions.")
