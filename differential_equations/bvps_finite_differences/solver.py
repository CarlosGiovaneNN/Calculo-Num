import numpy as np
import math


def run_bvp_finite_differences():
    print("--- BVP Finite Differences Solver ---")
    print("Equation: y'' = P(x)y' + Q(x)y + R(x), e. g., R(x) = -math.exp(x)*(x**2 + 1)")

    try:
        p_str = input("P(x) = ")
        q_str = input("Q(x) = ")
        r_str = input("R(x) = ")

        funcs = {
            "P": get_math_function(p_str),
            "Q": get_math_function(q_str),
            "R": get_math_function(r_str),
        }

        print("\nBoundary Conditions:")
        x0 = float(input("x(start) = "))
        y0 = float(input("y(start) = "))
        xn = float(input("x(end)   = "))
        yn = float(input("y(end)   = "))

        n = int(input("\nNumber of internal intervals (n): "))

    except Exception as e:
        print(f"Input Error: {e}")
        return

    x_vals = np.linspace(x0, xn, n + 1)

    A, b = build_finite_difference_system(funcs, x_vals, y0, yn)

    y_vals = solve_system(A, b)

    if y_vals is not None:
        print(f"\n{'x':<10} | {'y (approx)':<10}")
        print("-" * 25)
        for x, y in zip(x_vals, y_vals):
            print(f"{x:<10.4f} | {y:<10.6f}")
    else:
        print("\nError: Singular matrix. System cannot be solved.")

    return


def get_math_function(expression_str):
    context = {"__builtins__": None, "math": math, "np": np}
    return lambda x: eval(expression_str, context, {"x": x})


def build_finite_difference_system(funcs, x_vals, y_start, y_end):
    n_points = len(x_vals)
    h = x_vals[1] - x_vals[0]

    A = np.zeros((n_points, n_points))
    b = np.zeros(n_points)

    A[0, 0] = 1.0
    b[0] = y_start
    A[-1, -1] = 1.0
    b[-1] = y_end

    P, Q, R = funcs["P"], funcs["Q"], funcs["R"]

    for i in range(1, n_points - 1):
        xi = x_vals[i]

        pi = P(xi)
        qi = Q(xi)
        ri = R(xi)

        term_minus = 1 + (h / 2) * pi
        term_center = -2 - (h**2) * qi
        term_plus = 1 - (h / 2) * pi

        A[i, i - 1] = term_minus
        A[i, i] = term_center
        A[i, i + 1] = term_plus

        b[i] = (h**2) * ri

    return A, b


def solve_system(A, b):
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return None
