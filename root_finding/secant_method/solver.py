from sympy import *


def run_secant():
    print("\nInput function (use 'x' as variable): ")
    f_str = input("f(x) = ")

    f = lambda x: eval(f_str)

    print("\nInitial guesses:")
    x0 = float(input("x0 = "))
    x1 = float(input("x1 = "))

    print("\nCalculate by: ")
    print("1. Tolerance")
    print("2. Number of iterations")
    print("3. General")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        calculate_by_tolerance(f, x0, x1)

    elif choice == 2:
        calculate_by_number_of_iterations(f, x0, x1)

    elif choice == 3:
        secant(f, x0, x1)

    else:
        print("Invalid choice")
        return

    return


def calculate_by_tolerance(f, x0, x1):
    tolerance = float(input("Tolerance = "))

    secant(f, x0, x1, tolerance=tolerance, max_iterations=1000)

    return


def calculate_by_number_of_iterations(f, x0, x1):
    iterations = int(input("Number of iterations = "))

    secant(f, x0, x1, tolerance=1e-6, max_iterations=iterations)

    return


def secant(f, x0, x1, tolerance=1e-6, max_iterations=1000):
    for i in range(max_iterations):
        if f(x1) - f(x0) == 0:
            print("Division by zero encountered.")
            return

        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(x_next - x1) < tolerance:
            x1 = x_next

            break

        x0, x1 = x1, x_next

    if i == max_iterations - 1:
        print("\nMaximum iterations reached.")

    print("\nRoot: " + str(x1))

    return x1
