def solveForV(I, R):
    # V = I * R
    V = float(I * R)
    return V
def solveForI(V, R):
    # I = V / R
    I = float(V / R)
    return I
def solveForR(V, I):
    # R = V / I
    R = float(V / I)
    return R

varChoice = input("Solve for V/I/R?: ")
if varChoice.upper() == 'V':
    try:
        I = float(input("I = "))
        R = float(input("R = "))
    except ValueError:
        print("Invalid input!")
        exit(0)
    solution = solveForV(I, R)
    print("V =", solution, "V")
elif varChoice.upper() == 'I':
    try:
        V = float(input("V = "))
        R = float(input("R = "))
    except ValueError:
        print("Invalid input!")
        exit(0)
    solution = solveForI(V, R)
    print("I =", solution, "A")
elif varChoice.upper() == 'R':
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