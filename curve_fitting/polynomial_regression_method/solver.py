from matplotlib import pyplot as plt
import numpy as np

from curve_fitting.solve_equations import solve_normal_equations


def run_polynomial_regression():
    print("Polynomial Regression solver")

    n = int(input("Number of data points: "))
    degree = int(input("Polynomial degree (m): "))

    x = []
    y = []

    print("Enter points as 'x y':")
    for i in range(n):
        row = list(map(float, input(f"Point {i+1}: ").split()))
        x.append(row[0])
        y.append(row[1])

    x = np.array(x)
    y = np.array(y)

    X_mat = np.zeros((n, degree + 1))

    for i in range(degree + 1):
        X_mat[:, i] = x**i

    coeffs, r2 = solve_normal_equations(X_mat, y)

    if coeffs is not None:
        print("\n--- Results ---")
        print(f"Coefficients (a0, a1, ... am): {coeffs}")

        eq_str = f"y = {coeffs[0]:.4f}"
        for i in range(1, len(coeffs)):
            term = f"{coeffs[i]:.4f}*x^{i}"
            if coeffs[i] >= 0:
                eq_str += f" + {term}"
            else:
                eq_str += f" {term}"

        print(f"Equation: {eq_str}")
        print(f"R^2: {r2:.6f}")

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="red", label="Data points")

    x_curve = np.linspace(min(x), max(x), 200)
    y_curve = np.zeros_like(x_curve)

    for i in range(len(coeffs)):
        y_curve += coeffs[i] * (x_curve**i)

    plt.plot(
        x_curve, y_curve, color="green", linewidth=2, label=f"Polynomial (m = {degree}"
    )

    plt.title(f"Polynomial Regression ( m = {degree} )")
    plt.legend()
    plt.grid(True)
    plt.show()
