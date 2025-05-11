import math

def percentage_bar(bar_length, percent):
    filled_bar = math.ceil(
        bar_length * (percent / 100)
    )
    return "[" + "#"*filled_bar + "-"*(bar_length-filled_bar) + "]"

while True:
    bar_length = int(input("Bar length: "))
    percent = int(input("Percentage filled: "))
    if percent < 0 or percent > 100:
        print("Invalid percentage")
        print("--------------------")
    else:
        final_bar = percentage_bar(bar_length, percent)
        print(final_bar)
        print("--------------------")