def numerical_diff_test(f, x, h):
    # 前方差分
    return (f(x + h) - f(x)) / h


# f = lambda i: i*2 と書いたらlintされた。
def f(i): return i*2


print(numerical_diff_test(f, 2, 1e-50))
# h = 1e-50 -> 0.0
print(numerical_diff_test(f, 2, 1e-4))
# h = 1e-4  -> 2.0000000000042206

# hの値は小さければ小さいほどよいのだが、計算機上では丸め誤差が発生する。
# h = 1e-4程度が良いことが経験則として分かっている。


def numerical_diff_mod(f, x, h):
    # 中心差分
    return (f(x + h) - f(x - h)) / (2 * h)


print(numerical_diff_mod(f, 2, 1e-50))
# h = 1e-50 -> 0.0
print(numerical_diff_mod(f, 2, 1e-4))
# h = 1e-4  -> 2.000000000002
