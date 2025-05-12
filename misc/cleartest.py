import os
import keyboard

def clear_console() -> None:
    os.system("cls")

def main():
    while True:
        for x in "banana":
            print(x)

        answer = input('Clear console Y/N: ')
        if answer == 'Y' or answer == 'y':
            clear_console()
        else:
            exit(0)
        #if keyboard.read_key():
            #clear_console()

if __name__ == '__main__':
    main()