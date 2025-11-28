def run_trapezoidal_rule():
    print("Trapezoidal Rule solver")

    n_points = int(input("\nNumber of data points: "))

    points = []

    print("Enter each point as 'x y':")

    for i in range(n_points):
        x, y = map(float, input(f"Point {i+1}: ").split())
        points.append([x, y])

    print("\nData points: ")
    for p in points:
        print(f"x = {p[0]:.1f}, y = {p[1]:.4f}")

    result = trapezoidal_rule(points)

    if result is not None:
        print(f"\nApproximate Integral = {result:.6f}")

    return

def trapezoidal_rule(points):
    n = len(points)

    if n < 2:
        print("Error: Need at least 2 points for Trapezoidal Rule.")
        return None

    h = points[1][0] - points[0][0]

    sum_y = points[0][1] + points[-1][1]

    for i in range(1, n - 1):
        sum_y += 2 * points[i][1]

    integral = (h / 2) * sum_y

    return integral