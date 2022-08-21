import numpy as np
import sys
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)
from common.functions import softmax, cross_entropy_error  # noqa
from common.gradient import numerical_gradient  # noqa


class simpleNet:
    def __init__(self) -> None:
        # self.W = np.random.randn(2, 3)  # Gauss
        # 本の値を入力しチェック
        self.W = np.array([[0.47355232, 0.9977393, 0.84668094], [
                          0.85557411, 0.03563661, 0.69422093]])

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        return cross_entropy_error(y, t)


net = simpleNet()
print(net.W)
x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
print(np.argmax(p))
t = np.array([0, 0, 1])
print(net.loss(x, t))

dW = numerical_gradient(lambda w: net.loss(x, t), net.W)
print(dW)
