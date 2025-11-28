import math


def run_eulers():
    print("Euler's Method solver (y' = f(x, y))")

    print("Input function (use 'x' and 'y' as variables, e.g., 'x + y'): ")
    f_str = input("dy/dx = ")

    f = lambda x, y: eval(
        f_str,
        {
            "__builtins__": None,
            "math": math,
            "x": x,
            "y": y,
            "sin": math.sin,
            "cos": math.cos,
            "exp": math.exp,
        },
    )

    print("\nInitial values:")
    x0 = float(input("x0 = "))
    y0 = float(input("y0 = "))

    print("\nStep size:")
    h = float(input("h = "))

    print("\nNumber of steps:")
    n = int(input("n = "))

    eulers(f, x0, y0, h, n)

    return


def eulers(f, x0, y0, h, n):

    x = x0
    y = y0

    print(f"\nStep 0: x = {x:.4f}, y = {y:.4f}")

    for i in range(n):
        slope = f(x, y)

        y = y + h * slope

        x = x + h

        print(f"Step {i+1}: x = {x:.4f}, y = {y:.4f}")

    return
