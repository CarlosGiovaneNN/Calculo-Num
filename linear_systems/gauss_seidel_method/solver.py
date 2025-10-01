def run_gauss_seidel():
    print("Gauss-Seidel solver")

    variables = int(input("\nNumber of variables: "))

    print(f"\nEnter the augmented matrix ({variables} rows, {variables+1} columns):")

    matrix = []
    for i in range(variables):
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        if len(row) != variables + 1:
            print(f"Invalid row size, must have {variables+1} numbers.")
            return

        matrix.append(row)

    print("\nMatrix entered:")
    for row in matrix:
        print(row)

    print("\nCalculate by:")
    print("1. Tolerance")
    print("2. Number of iterations")
    print("3. General")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        calculate_by_tolerance(matrix, variables)

    elif choice == 2:
        calculate_by_number_of_iterations(matrix, variables)

    elif choice == 3:
        gauss_seidel(matrix, variables)

    else:
        print("Invalid choice")
        return

    return


def calculate_by_tolerance(matrix, variables):
    tolerance = float(input("Tolerance = "))

    gauss_seidel(matrix, variables, tolerance=tolerance, max_iterations=1000)

    return


def calculate_by_number_of_iterations(matrix, variables):
    iterations = int(input("Number of iterations = "))

    gauss_seidel(matrix, variables, max_iterations=iterations)

    return


def gauss_seidel(matrix, variables, tolerance=1e-6, max_iterations=100):
    x = [0.0 for _ in range(variables)]

    for it in range(max_iterations):
        x_old = x.copy()

        for i in range(variables):

            s = sum(matrix[i][j] * x[j] for j in range(variables) if j != i)

            x[i] = (matrix[i][variables] - s) / matrix[i][i]

        error = max(abs(x[i] - x_old[i]) for i in range(variables))

        print(f"Iteration {it+1}: {x}, Error = {error}")

        if error < tolerance:
            print("\nConverged solution:")

            for i in range(variables):
                print(f"x{i+1} = {x[i]}")

            return

    print("\nDid not converge within max iterations.")
    print("Approximate solution:")

    for i in range(variables):
        print(f"x{i+1} = {x[i]}")

    return
