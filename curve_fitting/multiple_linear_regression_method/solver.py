from matplotlib import pyplot as plt
import numpy as np

from curve_fitting.solve_equations import solve_normal_equations


def run_multiple_linear_regression():
    print("Multiple Linear Regression solver")
    n_points = int(input("Number of data points (n): "))
    n_vars = int(input("Number of independent variables (p): "))

    X_mat = np.zeros((n_points, n_vars + 1))
    y = np.zeros(n_points)

    print(f"Enter data for each point: x1 x2 ... x{n_vars} y")

    for i in range(n_points):
        vals = list(map(float, input(f"Point {i+1}: ").split()))

        X_mat[i, 0] = 1.0

        for j in range(n_vars):
            X_mat[i, j + 1] = vals[j]

        y[i] = vals[-1]

    coeffs, r2 = solve_normal_equations(X_mat, y)

    if coeffs is not None:
        print("\n--- Results ---")
        eq_str = f"y = {coeffs[0]:.4f}"
        for j in range(1, len(coeffs)):
            eq_str += f" + {coeffs[j]:.4f}*x{j}"

        print(f"Equation: {eq_str}")
        print(f"Coefficients (b0, b1, ...): {coeffs}")
        print(f"R^2: {r2:.6f}")

    y_pred = np.dot(X_mat, coeffs)

    plt.figure(figsize=(8, 6))

    plt.scatter(y, y_pred, color="blue")

    min_val = min(min(y), min(y_pred))
    max_val = max(max(y), max(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], "r--", label="Perfect Fit")

    plt.title("Multiple Linear Regression")
    plt.xlabel("Y (Real)")
    plt.ylabel("Y (Predicted)")
    plt.legend()
    plt.grid(True)
    plt.show()
