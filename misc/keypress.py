import math
import os
import keyboard

keypresses = 0

print("Press any key (or multiple keys) that is not enter on the keyboard.")
print("Press enter to print how many times you pressed keys.")

while True:
    if keyboard.read_key() != "enter":
        keypresses += 1
    elif keyboard.read_key() == "enter":
        print("You pressed keys",int(keypresses//2),"times.")
        keypresses = 0
        print("--------------------")