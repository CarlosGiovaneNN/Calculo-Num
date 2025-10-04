def run_lagrange():
    print("Lagrange solver")

    print("\1. Interpolation")
    # print("2. Extrapolation")
    print("2. Exit")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        print("Interpolation")

        x = list(map(float, input("Enter the values of x: ").split()))

        y = list(map(float, input("Enter the values of y: ").split()))

        x0 = float(input("Enter the value of x0: "))

        interpolation(x, y, x0)

    # elif choice == 2:
    #     print("Extrapolation")

    elif choice == 2:
        return

    return


def interpolation(x, y, x0):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x0 - x[j]) / (x[i] - x[j])
        result += term

    print(f"P({x0}) = {result:.3f}")

    return result
