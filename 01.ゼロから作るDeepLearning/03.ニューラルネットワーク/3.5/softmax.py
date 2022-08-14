import numpy as np


def softmax_deprecated(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a


def softmax(a):
    exp_a = np.exp(a - np.max(a))  # オーバーフロー対策。よく考えられてる。
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))

a = np.array([1010, 1000, 990])
y1 = softmax_deprecated(a)
# Pythonはオーバーフローで警告出してくれるの偉い。
# RuntimeWarning: overflow encountered in exp
# RuntimeWarning: invalid value encountered in divide
y2 = softmax(a)
print(y1)
print(y2)
