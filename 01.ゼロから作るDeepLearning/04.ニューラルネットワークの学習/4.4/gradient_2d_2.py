import numpy as np


def function_2(x): return x[0]**2 + x[1]**2  # == np.sum(x**2)


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        # 本よりこちらの方が意味が分かりやすい。
        x1 = np.copy(x)
        x1[idx] = x1[idx] + h

        x2 = np.copy(x)
        x2[idx] = x2[idx] - h

        grad[idx] = (f(x1) - f(x2)) / (2 * h)
    return grad


print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))
