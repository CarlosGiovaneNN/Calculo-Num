import math


def run_trapezoidal_rule():
    print("Trapezoidal Rule solver (Equation Mode)")

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
        },
    )

    a = float(input("Start of interval (a): "))
    b = float(input("End of interval (b): "))

    print("\nCalculate by:")
    print("1. Tolerance")
    print("2. Number of iterations")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        tolerance = float(input("Enter tolerance (epsilon): "))

        def quick_calc(current_n):
            h_step = (b - a) / current_n
            s = f(a) + f(b)
            for k in range(1, current_n):
                s += 2 * f(a + k * h_step)
            return (h_step / 2) * s

        n = 1
        old_val = quick_calc(n)
        print(f"Iterating to find n for tolerance {tolerance}...")

        while True:
            n *= 2
            new_val = quick_calc(n)
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
        n = int(input("Number of subintervals (n): "))

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

    result = trapezoidal_rule(points)

    if result is not None:
        print(f"\nApproximate Integral = {result:.6f}")

    return


def trapezoidal_rule(points):
    n = len(points)
    if n < 2:
        print("Error: Need at least 2 points.")
        return None

    h = points[1][0] - points[0][0]
    sum_y = points[0][1] + points[-1][1]

    for i in range(1, n - 1):
        sum_y += 2 * points[i][1]

    integral = (h / 2) * sum_y
    return integral
