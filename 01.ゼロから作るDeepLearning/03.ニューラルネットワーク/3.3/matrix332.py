import numpy as np

# 3.3.2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("1shape")
print(A.shape)
print(B.shape)
print("dot")
print(np.dot(A, B))

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
print("2shape")
print(A.shape)
print(B.shape)
print("dot")
print(np.dot(A, B))

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])
# B = np.array([[7], [8]])  これをnumpyがよしなに取り扱ってくれている。
print("3shape")
print(A.shape)
print(B.shape)
print("dot")
print(np.dot(A, B))
