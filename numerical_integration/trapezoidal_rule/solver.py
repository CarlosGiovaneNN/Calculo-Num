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
        },
    )

    a = float(input("Start of interval (a): "))
    b = float(input("End of interval (b): "))
    n = int(input("Number of subintervals (n): "))

    points = []
    h = (b - a) / n

    for i in range(n + 1):
        xi = a + i * h
        yi = f(xi)
        points.append([xi, yi])

    print("\nGenerated points used:")
    print(f"{'x':<10} | {'y':<10}")
    print("-" * 25)
    for p in points:
        print(f"{p[0]:<10.4f} | {p[1]:<10.6f}")

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
