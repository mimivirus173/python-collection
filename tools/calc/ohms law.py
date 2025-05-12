def solveForV(I, R):
    # V = I * R
    return I * R
def solveForI(V, R):
    # I = V / R
    return V / R
def solveForR(V, I):
    # R = V / I
    return V / I

def main():
    var_choice = input("Solve for V/I/R?: ").strip().upper()
    if var_choice == 'V':
        try:
            I = float(input("I = "))
            R = float(input("R = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        solution = solveForV(I, R)
        print("V =", solution, "V")
    elif var_choice == 'I':
        try:
            V = float(input("V = "))
            R = float(input("R = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        solution = solveForI(V, R)
        print("I =", solution, "A")
    elif var_choice == 'R':
        try:
            V = float(input("V = "))
            I = float(input("I = "))
        except ValueError:
            print("Invalid input!")
            exit(0)
        solution = solveForR(V, I)
        print("R =", solution, "Ω")
    else:
        print("Invalid input!")
        exit(0)

if __name__ == '__main__':
    main()