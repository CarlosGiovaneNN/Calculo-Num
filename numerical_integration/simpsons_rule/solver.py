import math


def run_simpsons_rule():
    print("Simpson's Rule Solver (Equation Mode)")

    print("\nInput function (use 'x' as variable, e.g., 'exp(-x**2) * cos(2*x)'):")
    f_str = input("f(x) = ")

    f = lambda x: eval(
        f_str,
        {
            "__builtins__": None,
            "math": math,
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
        },
    )

    a = float(input("Start of interval (a): "))
    b = float(input("End of interval (b): "))

    print("\nCalculate by:")
    print("1. Tolerance (Precision)")
    print("2. Number of subintervals (n)")

    choice = int(input("Enter your choice (1-2): "))

    n = 2

    if choice == 1:
        tolerance = float(input("Enter tolerance (epsilon): "))

        def quick_simpson(current_n):
            h_step = (b - a) / current_n
            s = f(a) + f(b)

            for i in range(1, current_n, 2):
                s += 4 * f(a + i * h_step)

            for i in range(2, current_n - 1, 2):
                s += 2 * f(a + i * h_step)

            return (h_step / 3) * s

        n = 2
        old_val = quick_simpson(n)
        print(f"Iterating to find n for tolerance {tolerance}...")

        while True:
            n *= 2
            new_val = quick_simpson(n)
            error = abs(new_val - old_val)

            if error < tolerance:
                print(f"Converged at n = {n} with estimated error = {error:.6e}")
                break

            old_val = new_val

            if n > 20000:
                print(
                    "Warning: Reached maximum limit of intervals without full convergence."
                )
                break

    elif choice == 2:
        n = int(input("Number of subintervals (n, must be even): "))
        if n % 2 != 0:
            print("Warning: n must be even for Simpson's 1/3 Rule. Adding 1 to n.")
            n += 1
            print(f"New n = {n}")

    else:
        print("Invalid choice. Defaulting to n=10.")
        n = 10

    points = []
    h = (b - a) / n

    print_table = n <= 20

    for i in range(n + 1):
        xi = a + i * h
        yi = f(xi)
        points.append([xi, yi])

    if print_table:
        print("\nGenerated points used:")
        print(f"{'x':<10} | {'y':<10}")
        print("-" * 25)
        for p in points:
            print(f"{p[0]:<10.4f} | {p[1]:<10.6f}")
    else:
        print(f"\nSkipping point table display (n={n} is too large).")

    result = simpsons_rule(points)

    if result is not None:
        print(f"\nApproximate Integral = {result:.6f}")

    return


def simpsons_rule(points):
    n_points = len(points)

    if n_points < 3:
        print("Error: Need at least 3 points (2 intervals) for Simpson's Rule.")
        return None

    h = points[1][0] - points[0][0]

    sum_y = points[0][1] + points[-1][1]

    for i in range(1, n_points - 1):
        y = points[i][1]

        if i % 2 != 0:
            sum_y += 4 * y
        else:
            sum_y += 2 * y

    integral = (h / 3) * sum_y
    return integral
