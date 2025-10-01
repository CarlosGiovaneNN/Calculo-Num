def run_gauss():
    print("Gauss solver")

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

    gauss(matrix, variables)

    return


def gauss(matrix, variables):

    for i in range(variables):

        if matrix[i][i] == 0:
            print("Zero pivot encountered! (Need partial pivoting)")
            return

        pivot = matrix[i][i]
        for col in range(i, variables + 1):
            matrix[i][col] /= pivot

        for row in range(i + 1, variables):
            factor = matrix[row][i]

            for col in range(i, variables + 1):
                matrix[row][col] -= factor * matrix[i][col]

    x = [0] * variables

    for row in range(variables - 1, -1, -1):
        x[row] = matrix[row][variables]

        for col in range(row + 1, variables):
            x[row] -= matrix[row][col] * x[col]

    print("\nSolution:")
    for i in range(variables):
        print(f"x{i + 1} = {x[i]}")

    return
