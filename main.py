from root_finding.bisection_method.solver import run_bisection
from root_finding.false_position_method.solver import run_false_position
from root_finding.newton_raphson_method.solver import run_newton_raphson
from root_finding.secant_method.solver import run_secant

while True:
    print("\nSolvers")

    print("1. Root Finding")
    print("2. Linear System")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print("\nRoot Finding")
        print("1. Bisection Method")
        print("2. False Position Method")
        print("3. Newton-Raphson Method")
        print("4. Secant Method")
        print("5. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            run_bisection()
        elif choice == 2:
            run_false_position()
        elif choice == 3:
            run_newton_raphson()
        elif choice == 4:
            run_secant()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
            continue

    elif choice == 2:

        break

    elif choice == 3:
        break

    else:
        print("Invalid choice")
        continue
