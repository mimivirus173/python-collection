# helped by ChatGPT
# this is still wack tho

import time
import threading

hunger = 10

def reset_hunger():
    global hunger
    hunger = 10

def input_thread():
    global hunger
    while hunger > 0:
        input_value = input()
        if input_value == 'eat':
            reset_hunger()

print("Enter 'eat' to reset the hunger level at any time:")

thread = threading.Thread(target=input_thread)
thread.start()

while hunger >= 0:
    print("Hunger level:", hunger)
    hunger -= 1
    time.sleep(1)