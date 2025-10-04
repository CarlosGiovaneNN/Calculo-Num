from sympy import *


def run_newton_raphson():
    print("\nInput function (use 'x' as variable): ")
    f_str = input("f(x) = ")

    f = lambda x: eval(f_str)

    print("\nInitial guess: ")
    x0 = float(input("x0 = "))

    print("\nCalculate by: ")
    print("1. Tolerance")
    print("2. Number of iterations")
    print("3. General")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        calculate_by_tolerance(f, x0)

    elif choice == 2:
        calculate_by_number_of_iterations(f, x0)

    elif choice == 3:
        newton_raphson(f, x0)

    else:
        print("Invalid choice")
        return

    return


def calculate_by_tolerance(f, x0):
    tolerance = float(input("Tolerance = "))

    newton_raphson(f, x0, tolerance=tolerance, max_iterations=1000)

    return


def calculate_by_number_of_iterations(f, x0):
    iterations = int(input("Number of iterations = "))

    newton_raphson(f, x0, tolerance=1e-6, max_iterations=iterations)

    return


def newton_raphson(f, x0, tolerance=1e-6, max_iterations=100):
    x = Symbol("x")
    f_diff = diff(f(x), x)

    for i in range(max_iterations):
        x_next = x0 - f(x0) / f_diff.subs(x, x0)

        if abs(x_next - x0) < tolerance:
            x0 = x_next
            break

        x0 = x_next

    if i == max_iterations - 1:
        print("\nMaximum iterations reached.")

    print("\nRoot: " + str(x0))

    return x0
