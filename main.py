from bisection_method.solver import run_bisection
from false_position_method.solver import run_false_position
from newton_raphson_method.solver import run_newton_raphson

while True:
    print("\nSelect the method:")
    print("1. Bisection")
    print("2. False Position")
    print("3. Newton Raphson")
    print("4. Secant")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("Bisection")
        run_bisection()

    elif choice == 2:
        print("False Position")
        run_false_position()

    elif choice == 3:
        print("Newton Raphson")
        run_newton_raphson()

    elif choice == 4:
        print("Secant")

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice")
