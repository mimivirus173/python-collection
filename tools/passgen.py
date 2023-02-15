import keyboard
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#¤%&/()=?@£${[]}+,.-'*"

string = lower + upper + numbers + symbols

print("Press any key:")

while True:
    if keyboard.read_key():
        length = random.randint(8,64)
        stringle = "".join(random.sample(string,length))
        print(stringle)
        continue