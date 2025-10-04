def run_bisection():
    print("\nInput function (use 'x' as variable): ")
    f_str = input("f(x) = ")

    f = lambda x: eval(f_str)

    print("\nInterval: ")
    a = float(input("a = "))
    b = float(input("b = "))

    print("\nCalculate by:")
    print("1. Tolerance")
    print("2. Number of iterations")
    print("3. General")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        calculate_by_tolerance(f, a, b)

    elif choice == 2:
        calculate_by_number_of_iterations(f, a, b)

    elif choice == 3:
        bisection(f, a, b)

    else:
        print("Invalid choice")
        return

    return


def calculate_by_tolerance(f, a, b):
    tolerance = float(input("Tolerance = "))

    bisection(f, a, b, tolerance=tolerance, max_iterations=1000)

    return


def calculate_by_number_of_iterations(f, a, b):
    iterations = int(input("Number of iterations = "))

    bisection(f, a, b, tolerance=1e-6, max_iterations=iterations)

    return


def bisection(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("\nNo root found in the given interval.")
        return None

    for i in range(max_iterations):
        c = (a + b) / 2

        if abs(f(c)) < tolerance:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    if i == max_iterations - 1:
        print("\nMaximum iterations reached.")

    print("\nRoot: " + str(c))

    return c
