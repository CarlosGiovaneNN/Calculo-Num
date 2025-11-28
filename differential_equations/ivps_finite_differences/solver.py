import math


def run_ivp_finite_differences():
    print("IVP Finite Differences Solver (Forward Difference)")
    print("Solves y' = f(x, y)")

    print("Input function (use 'x' and 'y', e.g., 'x - y + 2'): ")
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

    print("\nStep size (h):")
    h = float(input("h = "))

    print("\nTarget x (to stop):")
    x_final = float(input("x_final = "))

    n_steps = int((x_final - x0) / h)

    ivp_finite_difference(f, x0, y0, h, n_steps)

    return


def ivp_finite_difference(f, x0, y0, h, n):

    x = x0
    y = y0

    print(f"\n{'Iter':<5} | {'x':<10} | {'y (approx)':<10}")
    print("-" * 35)
    print(f"{0:<5} | {x:<10.4f} | {y:<10.4f}")

    for i in range(n):
        derivative = f(x, y)
        y = y + h * derivative
        x = x + h

        print(f"{i+1:<5} | {x:<10.4f} | {y:<10.4f}")

    return
