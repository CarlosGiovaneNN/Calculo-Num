from root_finding.bisection_method.solver import run_bisection
from root_finding.false_position_method.solver import run_false_position
from root_finding.newton_raphson_method.solver import run_newton_raphson
from root_finding.secant_method.solver import run_secant

from linear_systems.gauss_method.solver import run_gauss
from linear_systems.jordan_method.solver import run_jordan
from linear_systems.gauss_seidel_method.solver import run_gauss_seidel

from interpolation.divided_differences.solver import run_divided_differences
from interpolation.finite_differences.solver import run_finite_differences
from interpolation.lagrange.solver import run_lagrange

from numerical_integration.simpsons_rule.solver import run_simpsons_rule
from numerical_integration.trapezoidal_rule.solver import run_trapezoidal_rule

from differential_equations.eulers_method.solver import run_eulers
from differential_equations.second_order_rk_method.solver import run_second_order_rk
from differential_equations.fourth_order_rk_method.solver import run_fourth_order_rk
from differential_equations.ivps_finite_differences.solver import (
    run_ivp_finite_differences,
)
from differential_equations.bvps_finite_differences.solver import (
    run_bvp_finite_differences,
)

from curve_fitting.simple_linear_regression_method.solver import (
    run_simple_linear_regression,
)
from curve_fitting.multiple_linear_regression_method.solver import (
    run_multiple_linear_regression,
)
from curve_fitting.polynomial_regression_method.solver import run_polynomial_regression


while True:
    print("\nSolvers")

    print("1. Root Finding")
    print("2. Linear System")
    print("3. Interpolation")
    print("4. Curve Fitting")
    print("5. Numerical Integration")
    print("6. Differential Equations")
    print("7. Exit")

    choice = int(input("Enter your choice (1-6): "))

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
        print("2. Finite Differences")
        print("3. Lagrange")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_divided_differences()
        elif choice == 2:
            run_finite_differences()
        elif choice == 3:
            run_lagrange()
        else:
            print("Invalid choice")
            continue

    elif choice == 4:
        print("\nCurve Fitting Methods:")

        print("1. Simple Linear Regression")
        print("2. Multiple Linear Regression")
        print("3. Polynomial Regression")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_simple_linear_regression()
        elif choice == 2:
            run_multiple_linear_regression()
        elif choice == 3:
            run_polynomial_regression()
        else:
            print("Invalid choice")
            continue

    elif choice == 5:
        print("\nNumerical Integration Methods:")

        print("1. Trapezoidal Rule")
        print("2. Simpson's Rule")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_trapezoidal_rule()
        elif choice == 2:
            run_simpsons_rule()
        else:
            print("Invalid choice")
            continue

    elif choice == 6:
        print("\nDifferential Equations Methods:")

        print("1. Euler's")
        print("2. Runge-Kutta (2nd Order)")
        print("3. Runge-Kutta (4th Order)")
        print("4. Solving IVPs using Finite Differences")
        print("5. Solving BVPs using Finite Differences")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            run_eulers()
        elif choice == 2:
            run_second_order_rk()
        elif choice == 3:
            run_fourth_order_rk()
        elif choice == 4:
            run_ivp_finite_differences()
        elif choice == 5:
            run_bvp_finite_differences()
        else:
            print("Invalid choice")
            continue

    elif choice == 7:
        break

    else:
        print("Invalid choice")
        continue
