import numpy as np


def solve_normal_equations(X, y):
    XT = X.T
    XTX = np.dot(XT, X)
    XTy = np.dot(XT, y)

    try:
        beta = np.linalg.solve(XTX, XTy)
    except np.linalg.LinAlgError:
        print("\nError: Singular matrix. The data may be collinear or insufficient.")
        return None, None

    y_mean = np.mean(y)

    SQt = np.sum((y - y_mean) ** 2)

    y_pred = np.dot(X, beta)

    SQr = np.sum((y - y_pred) ** 2)

    if SQt == 0:
        r2 = 1.0
    else:
        r2 = 1.0 - (SQr / SQt)

    return beta, r2
