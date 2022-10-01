import keyboard
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#¤%&/()=?@£${[]}+,.-'*"

string = lower + upper + numbers + symbols

while True:
    if keyboard.read_key():
        length = random.randint(16,56)
        stringle = "".join(random.sample(string,length))
        print(stringle)
        continue