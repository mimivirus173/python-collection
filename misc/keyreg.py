import keyboard

def main():
    while True:
        key = keyboard.read_key()

        if keyboard.read_key() == key:
            print("You pressed:",key)
        continue

if __name__ == '__main__':
    main()