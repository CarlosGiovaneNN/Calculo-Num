import math


def run_simpsons_rule():
    print("Simpson's Rule Solver (Equation Mode)")

    print("\nInput function (use 'x' as variable):")
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
    n = int(input("Number of subintervals (n, must be even): "))

    if n % 2 != 0:
        print("Warning: n must be even for Simpson's 1/3 Rule. Adding 1 to n.")
        n += 1

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

    result = simpsons_rule(points)

    if result is not None:
        print(f"\nApproximate Integral = {result:.6f}")

    return


def simpsons_rule(points):
    n = len(points)
    if n < 3:
        print("Error: Need at least 3 points.")
        return None

    h = points[1][0] - points[0][0]
    sum_y = points[0][1] + points[-1][1]

    for i in range(1, n - 1):
        y = points[i][1]
        if i % 2 != 0:
            sum_y += 4 * y
        else:
            sum_y += 2 * y

    integral = (h / 3) * sum_y
    return integral
