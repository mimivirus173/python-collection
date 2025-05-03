import math

# manual calculation of solutions
def quadratic_solver(a, b, c):
    d = float((b**2) - (4*a*c))

    if d < 0:
        return "No real solution"
    elif d == 0:
        x = float(-b / (2*a))
        return x
    else:
        x_1 = float(((-b) + math.sqrt(d)) / (2*a))
        x_2 = float(((-b) - math.sqrt(d)) / (2*a))
        return x_1, x_2

## the program
# intro text
print("Calculator for quadratic equations with form ax² + bx + c = 0")
print("--------------------")

while True:
    # define the variables of the equation and check if they are numbers
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))    
    except ValueError:
        print("Invalid input! 'a', 'b' and 'c' must be numbers.")
        print("--------------------")
        continue
    
    # check for valid quadratic equation
    if a == 0:
        print("Invalid input! 'a' cannot be zero.")
        print("--------------------")
    else:
        # print the solution to the polynomial
        solution = quadratic_solver(a, b, c)
        print(solution)
        print("--------------------")