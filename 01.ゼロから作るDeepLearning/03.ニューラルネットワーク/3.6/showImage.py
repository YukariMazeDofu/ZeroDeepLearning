from PIL import Image
import numpy as np
import sys
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)
from dataset.mnist import load_mnist  # noqa


def img_show(img):
    pil_image = Image.fromarray(np.uint8(img))
    # pil_image.show()
    # CUI環境では動作しないので、次のように変更
    pil_image.save("./image.jpg")


(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
