import numpy as np
import matplotlib.pylab as plt


def function_1(x): return 0.01 * x ** 2 + 0.1 * x
def numerical_diff(f, x): return (f(x + 1e-4) - f(x - 1e-4)) / (2e-4)


def tangent_line(f, x):
    # source よりコピペ、切片を計算してラムダで返してる。
    d = numerical_diff(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.savefig("./gradient_1d-1.jpg")

print(numerical_diff(function_1, 5))
# numeric: 0.1999999999990898, actual: 0.2
print(numerical_diff(function_1, 10))
# numeric: 0.2999999999986347, actual: 0.3

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y2)
plt.savefig("./gradient_1d-2.jpg")
