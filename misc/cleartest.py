import os
import keyboard

def clear() -> None:
    os.system("cls")

while True:
    print("\na"*100)
    if keyboard.read_key():
        clear()
