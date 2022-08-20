import numpy as np
import sys
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)
from dataset.mnist import load_mnist  # noqa

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10

batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]


def cross_entropy_error(y, t):
    # データが一つで、配列で渡された場合は1行 y.size 列に修正する。
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size
