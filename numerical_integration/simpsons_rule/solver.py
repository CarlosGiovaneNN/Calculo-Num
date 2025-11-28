def run_simpsons_rule():
    print("Simpson's Rule Solver")

    n_points = int(input("\nNumber of data points (should be odd): "))

    if n_points % 2 == 0:
        print(
            "Warning: Simpson's 1/3 rule requires an odd number of points (even intervals)."
        )
        print("Calculations may be inaccurate or require Simpson's 3/8 rule.")

    points = []

    print("Enter each point as 'x y' (must be equally spaced):")

    for i in range(n_points):
        x, y = map(float, input(f"Point {i+1}: ").split())
        points.append([x, y])

    print("\nData points:")
    for p in points:
        print(f"x = {p[0]:.1f}, y = {p[1]:.4f}")

    result = simpsons_rule(points)

    if result is not None:
        print(f"\nApproximate Integral = {result:.6f}")

    return


def simpsons_rule(points):
    n = len(points)

    if n < 3:
        print("Error: Need at least 3 points for Simpson's Rule.")
        return None

    h = points[1][0] - points[0][0]

    sum_y = points[0][1] + points[-1][1]

    for i in range(1, n - 1):
        y = points[i][1]

        if i % 2 != 0:
            sum_y += 4 * y
        else:
            sum_y += 2 * y

    integral = (h / 3) * sum_y

    return integral
