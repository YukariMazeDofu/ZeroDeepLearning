import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x


def init_network():
    return {
        'W': [
            np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
            np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
            np.array([[0.1, 0.3], [0.2, 0.4]]),
        ],
        'B': [
            np.array([0.1, 0.2, 0.3]),
            np.array([0.1, 0.2]),
            np.array([0.1, 0.2]),
        ]
    }


def forward(network, x):
    for i in [0, 1, 2]:
        z = np.dot(x, network['W'][i]) + network['B'][i]
        x = sigmoid(z) if i != 2 else identity_function(z)
    return x


X = np.array([1.0, 0.5])
Y = forward(init_network(), X)
print(Y)
