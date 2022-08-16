from copyreg import pickle
from PIL import Image
import numpy as np
import sys
import pickle
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)
from dataset.mnist import load_mnist  # noqa
from common.functions import sigmoid, softmax  # noqa


def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False, one_hot_label=False)
    return x_test, t_test


def init_network():
    dir = SOURCE_PATH + r"/ch03/"
    with open(dir + "sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)  # 最も確率の高い要素のインデックスを取得
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

# Accuracy:0.9207
# 出力結果が書籍と異なる。環境によるものか？下記のオーバーフローが影響していそう。2回出てた
# RuntimeWarning: overflow encountered in exp
#  return 1 / (1 + np.exp(-x))
