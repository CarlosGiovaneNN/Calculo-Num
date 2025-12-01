from matplotlib import pyplot as plt
import numpy as np
from curve_fitting.solve_equations import solve_normal_equations


def run_power_regression():
    print("Power Regression Solver (y = a * x^b)")

    n = int(input("Number of data points: "))
    x = []
    y = []

    print("Enter points as 'x y' (Original Data):")
    for i in range(n):
        row = list(map(float, input(f"Point {i+1}: ").split()))
        x.append(row[0])
        y.append(row[1])

    x = np.array(x)
    y = np.array(y)
    x_log = np.log(x)
    y_log = np.log(y)

    X_mat_log = np.vstack([np.ones(len(x_log)), x_log]).T

    coeffs_log, r2_linearized = solve_normal_equations(X_mat_log, y_log)

    if coeffs_log is not None:
        alpha = np.exp(coeffs_log[0])
        beta = coeffs_log[1]

        y_pred = alpha * (x**beta)
        y_mean = np.mean(y)
        SQt = np.sum((y - y_mean) ** 2)
        SQr = np.sum((y - y_pred) ** 2)
        r2_real = 1.0 - (SQr / SQt)

        print("\n--- Results ---")
        print(f"Linearized Equation: ln(y) = {coeffs_log[0]:.4f} + {beta:.4f} * ln(x)")
        print(f"Original Equation:   y = {alpha:.4f} * x^{beta:.4f}")
        print(f"Coefficients: alpha (a) = {alpha:.4f}, beta (b) = {beta:.4f}")
        print(f"R^2 (Original Data): {r2_real:.6f}")

        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, color="red", label="Data Points")

        x_line = np.linspace(min(x), max(x), 100)
        y_line = alpha * (x_line**beta)

        plt.plot(
            x_line,
            y_line,
            color="green",
            linewidth=2,
            label=f"Power Fit ($y={alpha:.2f}x^{{{beta:.2f}}}$)",
        )

        plt.title(f"Power Regression ($R^2={r2_real:.4f}$)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.show()
