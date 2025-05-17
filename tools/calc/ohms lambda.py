def main():
    var_choice = input("Solve for V/I/R?: ").strip().upper()
    if var_choice == 'V':
        try:
            I = float(input("I = "))
            R = float(input("R = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        V = lambda I, R: I * R
        print("V =", V(I, R), "V")
    elif var_choice == 'I':
        try:
            V = float(input("V = "))
            R = float(input("R = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        I = lambda V, R: V / R
        print("I =", I(V, R), "A")
    elif var_choice == 'R':
        try:
            V = float(input("V = "))
            I = float(input("I = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        R = lambda V, I: V / I
        print("R =", R(V, I), "Ω")
    else:
        print("Invalid input!")
        exit(0)

if __name__ == '__main__':
    main()