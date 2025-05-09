import os
import keyboard

def clear_console() -> None:
    os.system("cls")

while True:
    print("\na"*100)
    if keyboard.read_key():
        clear_console()
