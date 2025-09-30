def run_false_position():
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

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        calculate_by_tolerance(f, a, b)

    elif choice == 2:
        calculate_by_number_of_iterations(f, a, b)

    elif choice == 3:
        root = false_position(f, a, b)

        print("\nRoot: " + str(root))

    else:
        print("Invalid choice")
        return

    return


def calculate_by_tolerance(f, a, b):
    tolerance = float(input("Tolerance = "))
    root = false_position(f, a, b, tolerance=tolerance, max_iterations=1000)

    print("\nRoot: " + str(root))

    return


def calculate_by_number_of_iterations(f, a, b):
    iterations = int(input("Number of iterations = "))
    root = false_position(f, a, b, tolerance=1e-6, max_iterations=iterations)

    print("\nRoot: " + str(root))

    return


def false_position(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("\nNo root found in the given interval.")
        return None

    for i in range(max_iterations):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tolerance:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nMaximum iterations reached.")

    return (a + b) / 2
