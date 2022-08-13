import numpy as np
import matplotlib.pyplot as plt
# 1.5と同様、対話形式でのみ動作する。

# データの作成
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
# plt.show()

# <stdin>:1: UserWarning: Matplotlib is currently using agg,
#  which is a non-GUI backend, so cannot show the figure.
# WSLではコンソールのみなのでこのような表示に。保存することで対応する。
# [matplotlibの図を表示できないエラーを解決する方法 | にわこま ブログ]
# (https://niwakomablog.com/matplotllib-figure-show-errorhandling/)

plt.savefig("./plot.jpg")
