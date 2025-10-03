import math


def run_divided_differences():
    print("Divided Differences solver")

    n = int(input("\nNumber of data points: "))
    points = []

    print("Enter each point as 'x y':")

    for i in range(n):
        x, y = map(float, input(f"Point {i+1}: ").split())
        points.append([x, y])

    print("\nData points:")

    for p in points:
        print(f"x = {p[0]:.1f}, y = {p[1]:.1f}")

    table = divided_differences(points)

    x_val = float(input("\nEnter x to evaluate the polynomial: "))

    evaluate_newton_polynomial(points, table, x_val)

    return


def divided_differences(points):

    n = len(points)
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = points[i][1]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (
                points[i + j][0] - points[i][0]
            )

    print("\nDivided Differences Table:")

    for row in table:
        print("  ".join(f"{val:.3f}" for val in row))

    return table


def evaluate_newton_polynomial(points, table, x):

    n = len(points)
    result = table[0][0]
    product = 1.0

    for i in range(1, n):
        product *= x - points[i - 1][0]
        result += table[0][i] * product

    print(f"P({x}) = {result:.3f}")

    return
