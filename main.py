from root_finding.bisection_method.solver import run_bisection
from root_finding.false_position_method.solver import run_false_position
from root_finding.newton_raphson_method.solver import run_newton_raphson
from root_finding.secant_method.solver import run_secant

from linear_systems.gauss_method.solver import run_gauss
from linear_systems.jordan_method.solver import run_jordan
from linear_systems.gauss_seidel_method.solver import run_gauss_seidel

from interpolation.divided_differences.solver import run_divided_differences

while True:
    print("\nSolvers")

    print("1. Root Finding")
    print("2. Linear System")
    print("3. Divided Differences")
    print("4. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print("\nRoot Finding Methods:")

        print("1. Bisection Method")
        print("2. False Position Method")
        print("3. Newton-Raphson Method")
        print("4. Secant Method")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            run_bisection()
        elif choice == 2:
            run_false_position()
        elif choice == 3:
            run_newton_raphson()
        elif choice == 4:
            run_secant()
        else:
            print("Invalid choice")
            continue

    elif choice == 2:
        print("\nLinear Systems Methods:")

        print("1. Gauss")
        print("2. Jordan")
        print("3. Gauss-Seidel")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_gauss()
        elif choice == 2:
            run_jordan()
        elif choice == 3:
            run_gauss_seidel()
        else:
            print("Invalid choice")
            continue

    elif choice == 3:
        print("\nInterpolation Methods:")

        print("1. Divided Differences")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_divided_differences()
        else:
            print("Invalid choice")
            continue

    elif choice == 4:
        break

    else:
        print("Invalid choice")
        continue
