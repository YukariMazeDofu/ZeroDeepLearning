import numpy as np
import sys
SOURCE_PATH = r"/home/user/ZeroDeepLearning/01.ゼロから作るDeepLearning/99.source"
sys.path.append(SOURCE_PATH)
from common.functions import softmax, cross_entropy_error  # noqa
from common.gradient import numerical_gradient  # noqa
