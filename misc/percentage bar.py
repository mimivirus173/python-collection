import math

def percentage_bar(bar_length, percent):
    filled_bar = math.ceil(
        bar_length * (percent / 100)
    )
    return f"[{'#'*filled_bar}{'-'*(bar_length-filled_bar)}]"
    # return "[" + "#"*filled_bar + "-"*(bar_length-filled_bar) + "]"

def main():
    while True:
        try:
            bar_length = int(input("Bar length: "))
            if bar_length <= 0:
                print("Invalid size")
                print("--------------------")
                continue
            else:
                try:
                    percent = float(input("Percentage filled: "))
                except ValueError:
                    print("Percentage must be a number!")
                    print("--------------------")
                    continue
                if percent < 0 or percent > 100:
                    print("Invalid percentage")
                    print("--------------------")
                else:
                    final_bar = percentage_bar(bar_length, percent)
                    print(final_bar)
                    print("--------------------")
        except ValueError:
            print("Bar length must be an integer!")
            print("--------------------")
            continue

if __name__ == '__main__':
    main()