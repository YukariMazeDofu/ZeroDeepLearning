import numpy as np
# どちらかというとpythonの勉強。


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
    # この書き方だと最終出力でidentity_functionを使えない。
    # 逆に言えば、活性化関数と恒等関数が同じならこれでいける。
    # けど3.5見る限りだとあまりなさそう？
    for W, B in zip(network['W'], network['B']):
        z = np.dot(x, W) + B
        x = sigmoid(z)
    return x


X = np.array([1.0, 0.5])
Y = forward(init_network(), X)
print(Y)
