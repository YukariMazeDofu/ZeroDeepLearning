import numpy as np


def function_2(x): return x[0]**2 + x[1]**2  # == np.sum(x**2)


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        x1 = np.copy(x)
        x1[idx] = x1[idx] + h

        x2 = np.copy(x)
        x2[idx] = x2[idx] - h

        grad[idx] = (f(x1) - f(x2)) / (2 * h)
    return grad


def gradient_desent(f, init_x, lr=0.01, step_num=100):
    # 本では `x = init_x` となっているが、参照をコピーしてしまうので非常によくない。
    x = np.copy(init_x)

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x


init_x = np.array([-3.0, 4.0])

print("lr=0.1")
x1 = gradient_desent(function_2, init_x, 0.1)
print(x1)
print("lr=10.0")
x2 = gradient_desent(function_2, init_x, 10.0)
print(x2)
print("lr=1e-10")
x3 = gradient_desent(function_2, init_x, 1e-10)
print(x3)
