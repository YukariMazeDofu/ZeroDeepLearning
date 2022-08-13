import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    y = x > 0
    # np.intだとdeprecatedとなったのでint64に改変。
    return y.astype(np.int64)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)

# https://python.atelierkobato.com/linestyle/


x = np.arange(-5., 5., 0.1)
y = step_function(x)
plt.plot(x, y, linestyle="dashed")
plt.ylim(-0.1, 1.1)
plt.savefig("./newral1.jpg")

y2 = sigmoid(x)
plt.plot(x, y2, linestyle="dashdot")
plt.savefig("./sigmoid1.jpg")

y3 = relu(x)
plt.plot(x, y3)
plt.savefig("./relu1.jpg")

# 活性化関数(ここではステップ関数やシグモイド関数)は、
# 「入力信号が重要な情報であれば大きな値を出力し、
# 　入力信号が重要でなければ小さな値を出力する」
# 「入力値がいかなり値を取ろうとも[0,1]で表現する」
