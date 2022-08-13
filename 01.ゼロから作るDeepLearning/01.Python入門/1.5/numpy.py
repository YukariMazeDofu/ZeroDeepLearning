# 1.5.1
import numpy as np

# 1.5.2
x = np.array([1.0, 2.0, 3.0])
# 対話形式では正しく動作するが、ファイルを実行するとうまくいかない。
# おそらくnumpy以外にもいろいろとimportが必要で対話形式だとよしなにやってくれている？
# partially initialized module 'numpy' has no attribute 'array'
# (most likely due to a circular import)

print(x)
print(type(x))

# 1.5.3
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x / y)
print(x / 2.0)

# 1.5.4
A = np.array([[1.0, 2.0], [3.0, 4.0]])
print(A)
A.shape
A.dtype
B = np.array([[3.0, 0.0], [0.0, 6.0]])
print(A + B)
print(A * B)
print(A * 10)

# 1.5.5 Broadcast
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

# 1.5.6 Access
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])
X = X.flatten()
print(X)
print(X[np.array([0, 2, 4])])
print(X > 15)
print(X[X > 15])
