import math
import matplotlib.pyplot as plt


def run_second_order_rk():
    print("Second-order Runge-Kutta method solver")

    f_str = input("dy/dx = ")

    context = {
        "__builtins__": None,
        "math": math,
        "x": 0,
        "y": 0,
        "sin": math.sin,
        "cos": math.cos,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
    }

    f = lambda x, y: eval(f_str, context | {"x": x, "y": y})

    print(
        "\n(Optional) Input analytical solution (use 'x' and 'y' as variables, e.g., 'x + y'): "
    )
    analytical_str = input("y(x) = ")

    f_analytical = None
    if analytical_str.strip():
        f_analytical = lambda x: eval(analytical_str, context | {"x": x})

    print("\nInitial values:")
    x0 = float(input("x0 = "))
    y0 = float(input("y0 = "))
    h = float(input("h = "))
    x_final = float(input("x_final = "))

    n = int((x_final - x0) / h)

    second_order_rk(f, x0, y0, h, n, f_analytical)
    return


def second_order_rk(f, x0, y0, h, n, f_analytical=None):
    x = x0
    y = y0

    x_vals = [x0]
    y_num_vals = [y0]
    y_exact_vals = []
    errors = []

    if f_analytical:
        y_exact = f_analytical(x0)
        y_exact_vals.append(y_exact)
        errors.append(abs(y - y_exact))

        print(
            f"\n{'Step':<5} | {'x':<8} | {'y_RK2':<10} | {'y_Exata':<10} | {'Erro':<10}"
        )
        print("-" * 55)
        print(f"{0:<5} | {x:<8.4f} | {y:<10.4f} | {y_exact:<10.4f} | {0.0:<10.6f}")
    else:
        print(f"\n{'Step':<5} | {'x':<8} | {'y_RK2':<10}")
        print("-" * 30)
        print(f"{0:<5} | {x:<8.4f} | {y:<10.4f}")

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)

        y = y + (k1 + k2) / 2
        x = x + h

        x_vals.append(x)
        y_num_vals.append(y)

        if f_analytical:
            y_exact = f_analytical(x)
            error = abs(y - y_exact)
            y_exact_vals.append(y_exact)
            errors.append(error)
            print(
                f"{i+1:<5} | {x:<8.4f} | {y:<10.4f} | {y_exact:<10.4f} | {error:<10.6f}"
            )
        else:
            print(f"{i+1:<5} | {x:<8.4f} | {y:<10.4f}")

    if f_analytical:
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(x_vals, y_num_vals, "o--", label="RK2 (Numerical)")
        plt.plot(x_vals, y_exact_vals, "r-", label="Analytical (Exact)", alpha=0.7)
        plt.title(f"Solution: RK2 (h={h})")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(x_vals, errors, "k-o", color="orange")
        plt.title("Absolute Error")
        plt.xlabel("x")
        plt.ylabel("Error")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    return
