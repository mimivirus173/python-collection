import keyboard

while True:
    key = keyboard.read_key()

    if keyboard.read_key() == key:
        print("You pressed:",key)
    continue