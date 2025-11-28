import math


def run_second_order_rk():
    print("Second-order Runge-Kutta method solver")

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

    second_order_rk(f, x0, y0, h, n)

    return


def second_order_rk(f, x0, y0, h, n):

    x = x0
    y = y0

    print(f"\nStep 0: x = {x:.4f}, y = {y:.4f}")

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)

        y = y + (k1 + k2) / 2

        x = x + h

        print(f"Step {i+1}: x = {x:.4f}, y = {y:.4f}")

    return
