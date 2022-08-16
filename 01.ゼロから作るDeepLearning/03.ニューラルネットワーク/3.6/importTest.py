import sys
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)

# 特定の行のみlintを除外する場合、`# noqa` ファイル全体なら` #flake8: noqa`
# lint有効だと一番上に持っていかれ、append前に実行してしまうためNG
from dataset.mnist import load_mnist  # noqa

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
