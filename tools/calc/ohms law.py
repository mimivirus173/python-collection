# function checks if input is float
def to_float(n):
    try:
        return float(n)
    except ValueError:
        return None

def main():
    choice = input("Solve for V/I/R?: ").strip().upper()
    if choice == 'V':
        if (I := to_float(input("I = "))) is not None and (R := to_float(input("R = "))) is not None:
            print(f"V = {I * R} V")
        else:
            print("Invalid input!")
            exit(0)
    elif choice == 'I':
        if (V := to_float(input("V = "))) is not None and (R := to_float(input("R = "))) is not None:
            print(f"I = {V / R} A")
        else:
            print("Invalid input!")
            exit(0)
    elif choice == 'R':
        if (V := to_float(input("V = "))) is not None and (I := to_float(input("I = "))) is not None:
            print(f"R = {V / I} Ω")
        else:
            print("Invalid input!")
            exit(0)
    else:
        print("Invalid input!")
        exit(0)

if __name__ == '__main__':
    main()