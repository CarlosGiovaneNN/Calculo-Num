def run_jordan():
    print("Jordan solver")

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
        A = "  ".join(f"{val:8.1f}" for val in row[:-1])
        b = f"{row[-1]:8.1f}  "
        print(f"[ {A} | {b} ]")

    jordan(matrix, variables)

    return


def jordan(matrix, variables):

    for i in range(variables):

        if matrix[i][i] == 0:
            print("Zero pivot encountered! (Need partial pivoting)")
            return

        pivot = matrix[i][i]

        for col in range(i, variables + 1):
            matrix[i][col] /= pivot

        for row in range(variables):

            if row != i:
                factor = matrix[row][i]

                for col in range(i, variables + 1):
                    matrix[row][col] -= factor * matrix[i][col]

    x = [matrix[i][variables] for i in range(variables)]

    print("\nSolution:")

    for i in range(variables):
        print(f"x{i+1} = {x[i]:.1f}")

    return
