import math
import numpy as np


# ==========================================
# EXERCÍCIO 2: Integração Numérica
# ==========================================
def exercicio_2():
    print("\n" + "=" * 40)
    print("EXERCÍCIO 2: Integração Numérica")
    print("=" * 40)

    f1 = lambda x: math.exp(-(x**2)) * math.cos(2 * x)
    f2 = lambda x: math.log(x + math.sqrt(x + 1))

    problemas = [
        (f1, 0, 2, "a) Integral de e^(-x^2)*cos(2x) em [0, 2]"),
        (f2, 1, 2, "b) Integral de ln(x + sqrt(x+1)) em [1, 2]"),
    ]

    tolerance = 1e-3

    for f, a, b, desc in problemas:
        print(f"\nResolvendo: {desc}")

        # --- Regra dos Trapézios (Busca Automática de n) ---
        n = 1
        old_val = float("inf")
        while True:
            h = (b - a) / n
            s = f(a) + f(b)
            for k in range(1, n):
                s += 2 * f(a + k * h)
            result = (h / 2) * s

            if abs(result - old_val) < tolerance:
                print(f"  [Trapézios] Convergiu com n={n}. Resultado = {result:.6f}")
                break
            old_val = result
            n *= 2
            if n > 20000:
                break

        # --- Regra de Simpson (Busca Automática de n) ---
        n = 2
        old_val = float("inf")
        while True:
            h = (b - a) / n
            s = f(a) + f(b)
            for i in range(1, n, 2):
                s += 4 * f(a + i * h)
            for i in range(2, n - 1, 2):
                s += 2 * f(a + i * h)
            result = (h / 3) * s

            if abs(result - old_val) < tolerance:
                print(f"  [Simpson]   Convergiu com n={n}. Resultado = {result:.6f}")
                break
            old_val = result
            n *= 2
            if n > 20000:
                break


# ==========================================
# EXERCÍCIOS 3 e 4: PVI (Euler, RK2, RK4)
# ==========================================
def exercicio_3_4():
    print("\n" + "=" * 40)
    print("EXERCÍCIOS 3 e 4: PVI (y' = y/x - (y/x)^2)")
    print("=" * 40)

    f_ode = lambda x, y: (y / x) - (y / x) ** 2
    y_analitica = lambda x: x / (1 + math.log(x))

    x0, y0 = 1.0, 1.0
    x_final = 3.0
    steps_h = [0.25, 0.1, 0.05]

    for h in steps_h:
        n_steps = int((x_final - x0) / h)
        print(f"\n--- Para h = {h} ({n_steps} passos) ---")

        res_euler = y0
        res_rk2 = y0
        res_rk4 = y0

        xe, ye = x0, y0
        xk2, yk2 = x0, y0
        xk4, yk4 = x0, y0

        print(
            f"{'Iter':<5} | {'x':<6} | {'Euler':<9} | {'RK2':<9} | {'RK4':<9} | {'Analítica':<9}"
        )
        print("-" * 65)

        for i in range(n_steps):
            x_next = x0 + (i + 1) * h
            y_exact = y_analitica(x_next)

            # --- Euler ---
            slope = f_ode(xe, ye)
            ye = ye + h * slope
            xe += h

            # --- RK2 ---
            k1 = h * f_ode(xk2, yk2)
            k2 = h * f_ode(xk2 + h, yk2 + k1)
            yk2 = yk2 + (k1 + k2) / 2
            xk2 += h

            # --- RK4 ---
            k1_4 = h * f_ode(xk4, yk4)
            k2_4 = h * f_ode(xk4 + h / 2, yk4 + k1_4 / 2)
            k3_4 = h * f_ode(xk4 + h / 2, yk4 + k2_4 / 2)
            k4_4 = h * f_ode(xk4 + h, yk4 + k3_4)
            yk4 = yk4 + (k1_4 + 2 * k2_4 + 2 * k3_4 + k4_4) / 6
            xk4 += h

            print(
                f"{i+1:<5} | {x_next:<6.2f} | {ye:<9.4f} | {yk2:<9.4f} | {yk4:<9.4f} | {y_exact:<9.4f}"
            )


# ==========================================
# EXERCÍCIO 5: PVC (Diferenças Finitas)
# ==========================================
def exercicio_5():
    print("\n" + "=" * 40)
    print("EXERCÍCIO 5: PVC (Diferenças Finitas)")
    print("=" * 40)

    P = lambda x: 1.0
    Q = lambda x: -x
    R = lambda x: -math.exp(x) * (x**2 + 1)

    x_start, y_start = 0.0, 0.0
    x_end, y_end = 1.0, math.e

    hs = [0.1, 0.05, 0.01]

    for h in hs:
        n = int((x_end - x_start) / h)
        print(f"\n--- Para h = {h} (n = {n}) ---")

        x_vals = np.linspace(x_start, x_end, n + 1)
        dim = n + 1
        A = np.zeros((dim, dim))
        b = np.zeros(dim)

        A[0, 0] = 1.0
        b[0] = y_start
        A[-1, -1] = 1.0
        b[-1] = y_end

        for i in range(1, n):
            xi = x_vals[i]

            pi, qi, ri = P(xi), Q(xi), R(xi)

            term_minus = 1 + (h / 2) * pi
            term_center = -2 - (h**2) * qi
            term_plus = 1 - (h / 2) * pi

            A[i, i - 1] = term_minus
            A[i, i] = term_center
            A[i, i + 1] = term_plus
            b[i] = (h**2) * ri

        try:
            y_vals = np.linalg.solve(A, b)
            print(f"{'x':<6} | {'y (approx)':<10}")
            print("-" * 20)
            step_print = max(1, n // 10)
            for k in range(0, n + 1, step_print):
                print(f"{x_vals[k]:<6.2f} | {y_vals[k]:<10.6f}")
            if (n % step_print) != 0:
                print(f"{x_vals[-1]:<6.2f} | {y_vals[-1]:<10.6f}")

        except np.linalg.LinAlgError:
            print("Erro: Matriz singular.")


if __name__ == "__main__":
    exercicio_2()
    exercicio_3_4()
    exercicio_5()
