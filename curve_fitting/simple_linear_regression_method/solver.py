from matplotlib import pyplot as plt
import numpy as np

from curve_fitting.solve_equations import solve_normal_equations


def run_simple_linear_regression():
    print("Simple Linear Regression solver")
    n = int(input("Number of data points: "))

    x = []
    y = []

    print("Enter points as 'x y':")
    for i in range(n):
        row = list(map(float, input(f"Point {i+1}: ").split()))
        x.append(row[0])
        y.append(row[1])

    x = np.array(x)
    y = np.array(y)

    X_mat = np.vstack([np.ones(len(x)), x]).T

    coeffs, r2 = solve_normal_equations(X_mat, y)

    if coeffs is not None:
        print("\n--- Results ---")
        print(f"Equation: y = {coeffs[0]:.4f} + {coeffs[1]:.4f}x")
        print(
            f"Coefficients: a (intercept) = {coeffs[0]:.4f}, b (slope) = {coeffs[1]:.4f}"
        )
        print(f"R^2: {r2:.6f}")

    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, color="red", label="Data Points")

    x_line = np.linspace(min(x), max(x), 100)
    y_line = coeffs[0] + coeffs[1] * x_line

    plt.plot(
        x_line,
        y_line,
        color="blue",
        linewidth=2,
        label=f"Regression Line ($R^2={r2:.4f}$)",
    )

    plt.title("Simple Linear Regression")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
